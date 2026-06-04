# Diagnose and Fix App Crashes Using AI-Assisted Analysis

In this exercise, you'll download a sample app with intentional crashes, build and run it on your Fire TV device, then use the Amazon Devices Builder Tools MCP server to diagnose and fix the crashes through automated stack trace analysis.

## Prompts at a Glance

This exercise requires **4 prompts** to your AI agent:

| # | Prompt | What It Does |
|---|--------|--------------|
| 1 | `Checkout the crash-demo branch, clean and build the Release variant via npm, then install and launch the app on my Fire TV device` | Builds and deploys the crash demo app |
| 2 | `Why did my app crash?` | Runs the full crash-analysis sequence and explains the root cause (run after triggering a crash on the Advanced Features screen) |
| 3 | `Before changing anything, explain what fix you would apply for each crash and why.` | Has the agent describe its planned fixes before touching code |
| 4 | `Please fix it` | Applies defensive fixes and redeploys |

## Prerequisites

Before starting this exercise, make sure you have:

- [ ] Completed [Build, Run, and Manage the App](2_build_run_manage_app_using_prompts.md)
- [ ] Completed [Prerequisites](0_prerequisites.md) and verified the MCP server is connected
- [ ] A Fire TV Stick HD or 4K Select running Vega OS with Developer Mode enabled

---

## Step 1: Build and Run the Crash Demo App

The `crash-demo` branch of the VegaWorkshopApp contains intentional JavaScript runtime crashes that demonstrate common crash patterns in TV apps.

### 🤖 Prompt 1

Copy and paste this into your AI agent's chat:

```
Checkout the crash-demo branch, clean and build the Release variant via npm, then install and launch the app on my Fire TV device
```

The AI agent will:
1. Checkout the `crash-demo` branch
2. Run `npm install` and build the app in Release mode
3. Deploy and launch the app on your connected Fire TV device

> **Note:** Release builds are required to generate ACR (Amazon Crash Report) files, which contain the stack traces needed for crash analysis.
>
> **Important:** Even if you build via CLI, launch the app through Vega Studio (Play icon) to enable automatic crash report collection. Vega Studio automatically pulls ACR files from the device when crashes occur.

**🏁 Checkpoint:** The app launches and displays a home screen. Navigate to the **Advanced Features** screen.

<p align="center">
  <img src="https://github.com/user-attachments/assets/c3d68ab6-adc6-445d-a252-db062f05b2c7" width="640" alt="Advanced Features screen with three buttons">
  <br>
  <em>The Advanced Features screen</em>
</p>

You should see three buttons: **Play Video**, **Change Audio Track**, and **Select Subtitle**.

---

## Step 2: Trigger a Crash

Press any of the three buttons on the Advanced Features screen to trigger a crash:

- **▶ Play Video** - Triggers null reference error
- **🔊 Change Audio Track** - Triggers undefined property error
- **📝 Select Subtitle** - Triggers array bounds error

In a Release build, the app will close immediately.

> **Note:** Make sure your IDE (VS Code or Kiro) is open in the `VegaWorkshopApp` directory — this is required so Vega Studio can automatically pull ACR (crash report) files from the device when crashes occur. Otherwise, you can ask your coding agent manually why your app crashed — the agent will pull the latest ACR file and analyze it.

---

## Step 3: Ask the Coding Agent to Explain the Crash

### 🤖 Prompt 2

After the crash, copy and paste this into your AI agent's chat:

```
Why did my app crash?
```

This single prompt kicks off the full MCP crash-analysis sequence. The agent will:
1. Locate the ACR (Amazon Crash Report) file that Vega Studio pulled from the device
2. Symbolicate and analyze the stack trace to find the crash location
3. Explain the root cause in plain language
4. Scan for similar issues elsewhere in the codebase

**Expected Analysis:** The agent will provide a crash summary showing:
- Error type (TypeError, ReferenceError, etc.)
- Exact file and line number where the crash occurred
- Root cause explanation (e.g., accessing properties on null/undefined)
- Additional potential crashes found in the same file

---

## Step 4: Review the Proposed Fix

Before letting the agent change any code, have it explain *what* it will fix and *why*. This keeps you in control and helps you learn the defensive patterns it applies.

### 🤖 Prompt 3

Copy and paste this into your AI agent's chat:

```
Before changing anything, explain what fix you would apply for each crash and why.
```

The agent will walk through each of the three crashes and describe its planned fix:
- **Null reference** → add a guard so the handler returns early when no video is selected
- **Undefined property** → extend the TypeScript interface and check the property exists before use
- **Array bounds** → add a bounds check before indexing into the array

Read through the reasoning and confirm it matches the root causes from Step 3. When you're satisfied, move on to apply the fix.

---

## Step 5: Apply the Fixes

### 🤖 Prompt 4

Copy and paste this into your AI agent's chat:

```
Please fix it
```

The AI agent will:
1. Add null checks and bounds checks to prevent crashes
2. Update TypeScript interfaces if needed
3. Apply defensive programming patterns
4. Rebuild and redeploy the app to verify the fixes work

**🏁 Checkpoint:** After the fixes are applied:
- ✅ App launches without errors
- ✅ Pressing the buttons no longer crashes the app
- ✅ Console warnings appear instead of crashes when edge cases occur

## What Tools Does the MCP Server Use for Crash Analysis?

The Amazon Devices Builder Tools MCP server provides AI-assisted crash analysis for Vega app developers. It diagnoses crashes by analyzing stack traces, identifying root causes, and suggesting fixes.

**Current support:**
- JavaScript runtime crashes (TypeError, ReferenceError, etc.)
- `vega_analyze_anr_crash` — App Not Responding (UI thread frozen > 5s)
- `vega_analyze_lmk_crash` — Low Memory Killer (out of memory)
- Native crashes (C++ exceptions, segmentation faults)

The crash analysis workflow follows these steps:

<p align="center">
  <img src="https://github.com/user-attachments/assets/a23e5db3-286a-4045-88f5-a395006896c7" width="640" alt="Crash analysis workflow diagram">
  <br>
  <em>The MCP crash analysis workflow</em>
</p>


---

## Appendix: About the Crashes

<details>
<summary><strong>What crashes are in the crash-demo branch?</strong></summary>

The `crash-demo` branch contains three intentional JavaScript runtime crashes in `AdvancedFeaturesScreen.tsx`:

1. **Null Reference Error** - Accessing properties on a `null` object
2. **Undefined Property Error** - Accessing properties that don't exist in the interface
3. **Array Bounds Error** - Accessing array indices that are out of bounds

Here's what the problematic code looks like:

```tsx
export const AdvancedFeaturesScreen = ({navigation}: Props) => {
  const [selectedVideo, setSelectedVideo] = useState<VideoMetadata | null>(null);
  const [subtitles, setSubtitles] = useState<string[]>([]);

  // ❌ CRASH 1: Null reference - selectedVideo is null
  const handlePlayVideo = () => {
    console.log(`Playing video: ${selectedVideo.sources[0].url}`);
    const duration = selectedVideo.metadata.duration;
  };

  // ❌ CRASH 2: Undefined property - audioTracks doesn't exist
  const handleChangeAudioTrack = () => {
    const tracks = selectedVideo.audioTracks;
    const selectedTrack = tracks[0];
    console.log(`Switching to: ${selectedTrack.language}`);
  };

  // ❌ CRASH 3: Array bounds - subtitles array is empty
  const handleSelectSubtitle = (index: number) => {
    const subtitle = subtitles[index];
    console.log(`Selected subtitle: ${subtitle.toUpperCase()}`);
  };

  return (
    <View style={styles.container}>
      <TouchableOpacity onPress={handlePlayVideo}>
        <Text>▶ Play Video</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={handleChangeAudioTrack}>
        <Text>🔊 Change Audio Track</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={() => handleSelectSubtitle(5)}>
        <Text>📝 Select Subtitle</Text>
      </TouchableOpacity>
    </View>
  );
};
```

</details>

<details>
<summary><strong>What fixes will the AI agent apply?</strong></summary>

The AI agent will apply defensive programming patterns to prevent crashes:

**Fix 1: Add Null Checks**
```typescript
const handlePlayVideo = () => {
  if (!selectedVideo) {
    console.warn('No video selected');
    return;
  }
  console.log(`Playing video: ${selectedVideo.sources[0].url}`);
};
```

**Fix 2: Update Interface and Add Property Check**
```typescript
interface AudioTrack {
  language: string;
  label: string;
}

interface VideoMetadata {
  duration: number;
  title: string;
  sources: Array<{url: string; type: string}>;
  audioTracks?: AudioTrack[]; // Add optional property
}

const handleChangeAudioTrack = () => {
  if (!selectedVideo?.audioTracks?.length) {
    console.warn('No audio tracks available');
    return;
  }
  const selectedTrack = selectedVideo.audioTracks[0];
  console.log(`Switching to: ${selectedTrack.language}`);
};
```

**Fix 3: Add Bounds Check**
```typescript
const handleSelectSubtitle = (index: number) => {
  if (index >= subtitles.length) {
    console.warn(`Subtitle index ${index} out of bounds`);
    return;
  }
  const subtitle = subtitles[index];
  console.log(`Selected subtitle: ${subtitle.toUpperCase()}`);
};
```

---

**Previous:** [Build, Run, and Manage the App](2_build_run_manage_app_using_prompts.md) | **Next:** [Diagnose UI Fluidity](4_diagnose_ui_fluidity.md)
