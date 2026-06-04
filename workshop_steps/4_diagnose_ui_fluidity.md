# Diagnose and Fix UI Fluidity Issues

TV apps need smooth 60fps rendering for a good user experience. In this exercise, you'll use your AI agent to check out a branch with an intentional performance bug, build and run the app on your Fire TV device, then diagnose and fix the UI fluidity issue — all through chat prompts.

## Prompts at a Glance

| # | Prompt | What It Does |
|---|--------|--------------|
| 1 | `Checkout the perf-demo branch, clean previous builds (build and node_modules directories) and build the Debug variant via npm. Then install and launch the vega app on my Fire TV device using vega sdk` | Builds and deploys the perf demo app |
| 2 | `How is my app's UI fluidity performance?` | Measures UI fluidity and identifies the biggest fluidity drop |
| 3 | `Can you check and make improvements using vega workflow?` | Finds hot functions and applies optimizations |
| 4 | `Rebuild the Debug variant and reinstall the app on my Fire TV device.` | Rebuilds and redeploys so you can experience the fix |
| 5 | `Remeasure UI fluidity.` | Re-runs the KPI Visualizer to confirm the improved score |

## Prerequisites

Before starting this exercise, make sure you have:

- [ ] Completed [Build, Run, and Manage the App](2_build_run_manage_app_using_prompts.md)
- [ ] Completed [Prerequisites](0_prerequisites.md) and verified the MCP server is connected
- [ ] A Fire TV Stick HD or 4K Select running Vega OS with Developer Mode enabled

---

## Step 1: Check Out the Branch and Run

### 🤖 Prompt 1

Copy and paste this into your AI agent's chat:

```
Checkout the perf-demo branch, clean previous builds (build and node_modules directories) and build the Debug variant via npm. Then install and launch the vega app on my Fire TV device using vega sdk
```

The agent will:
1. Switch to the `perf-demo` branch (`git checkout perf-demo`)
2. Clean any previous build artifacts (`rm -rf build node_modules`)
3. Install npm dependencies (`npm install`)
4. Build the app in Debug mode (`npm run build:debug`)
5. Deploy and launch the app on your connected Fire TV device (`vega device install-app --dir . -b Debug`, then `vega device launch-app --dir .`)

**🏁 Checkpoint:** You're on the `perf-demo` branch with a clean build, and the app launches so you can navigate with the D-pad. You may notice some lag while scrolling — that's the bug we're about to diagnose.

---

## Step 2: Measure UI Fluidity

### 🤖 Prompt 2

Copy and paste this into your AI agent's chat:

```
How is my app's UI fluidity performance?
```

The agent follows the MCP server workflow. It will:
1. Read the workflow document `react_native_for_vega_diagnose_ui_fluidity`
2. Analyze the results and identify the time period with the biggest fluidity drop

You might see a report like this. This example is from Kiro — other coding agents may present the results in a different format:

<p align="center">
  <img src="https://github.com/user-attachments/assets/661e8fd3-e146-4474-ac7c-719b32769e83" width="400" alt="UI fluidity KPI report showing a failing score">
  <br>
  <em>UI fluidity KPI report (baseline — failing)</em>
</p>

**🏁 Checkpoint:** The agent reports the UI Fluidity KPI as **FAILING**.

---

## Step 3: Diagnose and Optimize

### 🤖 Prompt 3

Copy and paste this into your AI agent's chat:

```
Can you check and make improvements using vega workflow?
```

The agent continues the MCP server workflow. It will:
1. Identify hot functions in the problem time period using `get_app_hot_functions`
2. Apply code optimizations

You'll see hot-function analysis similar to this (results vary by coding agent):

```
# Hot Function Analysis Results

## Top 3 Hot Functions

### 1. ThumbnailItem
- **Duration**: 3ms (0.15% of total)
- **File**: /Volumes/workplace/VegaDeveloperWorkshop/reference/VegaWorkshopApp/src/screens/HomeScreen.tsx
- **Location**: Line 82, Column 7
- **App Function**: Yes

### 2. [anonymous]
- **Duration**: 15ms (0.75% of total)
- **File**: /Volumes/workplace/VegaDeveloperWorkshop/reference/VegaWorkshopApp/src/screens/HomeScreen.tsx
- **Location**: Line 77, Column 11
- **App Function**: Yes

### 3. ThumbnailItem
- **Duration**: 15ms (0.75% of total)
- **File**: /Volumes/workplace/VegaDeveloperWorkshop/reference/VegaWorkshopApp/src/screens/HomeScreen.tsx
- **Location**: Line 65, Column 24
- **App Function**: Yes
```

The agent then applies optimizations to `HomeScreen.tsx`. Here's an example fix from Kiro — the exact reporting will vary based on your coding agent:

<p align="center">
  <img src="https://github.com/user-attachments/assets/37fde8aa-661e-46a9-b56b-dd0982c7e81c" width="600" alt="Optimizations applied to HomeScreen.tsx">
  <br>
  <em>Example optimizations applied to HomeScreen.tsx</em>
</p>

---

## Step 4: Rebuild and Experience the Fix

After the agent applies optimizations, have it rebuild and redeploy the app so you can try it yourself.

### 🤖 Prompt 4

Copy and paste this into your AI agent's chat:

```
Rebuild the Debug variant and reinstall the app on my Fire TV device.
```

The agent will:
1. Rebuild the app in Debug mode
2. Reinstall it on your device

**🏁 Checkpoint:** Once the app relaunches, navigate the home screen with the D-pad and scroll through the rows. The lag you saw in Step 1 should be gone — scrolling now feels smooth. Take a moment to compare the before-and-after feel for yourself.

---

## Step 5: Re-measure UI Fluidity

Now confirm the improvement with hard numbers.

### 🤖 Prompt 5

Copy and paste this into your AI agent's chat:

```
Remeasure UI fluidity.
```

The agent will re-run the KPI Visualizer to measure the new fluidity score.

> 💡 If you'd rather do the rebuild and re-measure in one go, you can instead ask:
>
> ```
> Yes. Proceed with rebuilding, reinstalling the app, and remeasuring UI fluidity.
> ```

**🏁 Checkpoint:** The fluidity score improves significantly from the baseline toward the ≥99% target. Here's the report from Kiro after the fix:

<p align="center">
  <img src="https://github.com/user-attachments/assets/dfb383d7-a683-4de2-be03-3932f2eb62a3" width="400" alt="UI fluidity KPI report showing an improved score after the fix">
  <br>
  <em>UI fluidity KPI report (after the fix — passing)</em>
</p>

---

## About the Bug

To have the coding agent explain what it fixed, copy and paste this into the chat:

```
What was the issue fixed to improve UI fluidity?
```

The agent will return a detailed report of the root cause and the optimization it applied.

---

## Summary

In this exercise, you learned to:
1. Use the `diagnose_ui_fluidity` workflow to systematically identify UI fluidity failures
2. Let the AI agent analyze CPU hot functions and apply targeted optimizations
3. Verify improvements by re-running KPI measurements

<details>
<summary><strong>Appendix A: MCP Tools Used in Fluidity Diagnosis</strong></summary>

<p align="center">
  <img src="https://github.com/user-attachments/assets/f1dd4976-fc99-4300-ab1b-fb04fb485405" width="640" alt="Diagram of MCP tools used in fluidity diagnosis">
  <br>
  <em>MCP tools used in the fluidity diagnosis workflow</em>
</p>

</details>

---

**Previous:** [Diagnose Crashes](3_diagnose_crashes.md) | **Next:** [Wrap Up and Next Steps](5_wrap_up_and_next_steps.md)
