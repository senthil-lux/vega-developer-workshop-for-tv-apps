# Shaka Player Upgrade

The `shaka_player` branch of the workshop app plays adaptive video (HLS/DASH) using [Shaka Player](https://developer.amazon.com/docs/vega/0.22/media-player-shaka-player.html). It currently ships with **Shaka Player 4.6.18**. In this exercise, you'll run that app, then use the MCP server to find the available Vega-patched Shaka versions and upgrade to **4.8.5-r1.7**.

Because the Vega Shaka package has to be built from a downloaded release, the upgrade is one end-to-end prompt — your agent fetches the release, builds it, swaps it into the app, and rebuilds.

## Prompts at a Glance

| # | Prompt | What It Does |
|---|--------|--------------|
| 1 | `Checkout the shaka_player branch, clean previous builds (build and node_modules directories) and build the Release variant via npm. Then install and launch the vega app on my Fire TV device using vega sdk` | Builds and runs the Shaka demo app (Shaka 4.6.18) |
| 2 | `What Shaka Player versions are available for Vega ?` | Lists the Vega-patched Shaka versions and detects the current one |
| 3 | `Upgrade Shaka Player in this app to 4.8.5-r1.7 — download the Vega release, build it, swap the dist into the app, then clean build and run on my Fire TV device.` | Downloads, builds, swaps in the new Shaka, rebuilds, and runs |

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
Checkout the shaka_player branch, clean previous builds (build and node_modules directories) and build the Release variant via npm. Then install and launch the vega app on my Fire TV device using vega sdk
```

The agent will:
1. Switch to the `shaka_player` branch
2. Clean previous build artifacts and reinstall dependencies
3. Build the app in Release mode
4. Deploy and launch it on your connected Fire TV device

**🏁 Checkpoint:** The app launches and plays adaptive video. This build uses **Shaka Player 4.6.18**.

---

## Step 2: Check Which Shaka Versions Are Available

### 🤖 Prompt 2

Copy and paste this into your AI agent's chat:

```
What Shaka Player versions are available for Vega?
```

The agent uses the MCP server to read the official Vega media-player documentation and report the available Vega-patched Shaka releases, along with the version this app currently uses (4.6.18). The available release families are roughly:

| Version | Notable Patch | Notes |
|---------|---------------|-------|
| **4.16.13** | r1.2 | Newest family; replaces 4.6.18 |
| **4.8.5** | **r1.7** | The version we'll upgrade to in this exercise |
| **4.6.18** | r2.16 | What the app ships with today |
| **4.3.6** | r2.5 | Headless JS playback support |

**🏁 Checkpoint:** The agent confirms the app is on 4.6.18 and that newer Vega-patched versions (including 4.8.5-r1.7) are available.

---

## Step 3: Upgrade and Run

### 🤖 Prompt 3

Copy and paste this into your AI agent's chat:

```
Upgrade Shaka Player in this app to 4.8.5-r1.7 — download the Vega release, build it, swap the dist into the app, then clean build and run on my Fire TV device.
```

The agent will:
1. Download the **4.8.5-r1.7** Vega Shaka release and run its `setup.sh` helper script to build Shaka Player (this generates a `shaka-player` build with a `dist` folder)
2. Copy the generated `dist` into `src/shakaplayer/dist` and update `src/shakaplayer/ShakaPlayer.ts` as needed
3. Run a clean build (`rm -rf build node_modules && npm install && npm run build:release`)
4. Deploy and launch the upgraded app on your Fire TV device

> 💡 **If the agent can't download the release**, download it yourself from the link below and tell the agent where you saved it (e.g., *"I've downloaded it to `~/Downloads/shaka-rel-v4.8.5-r1.7-devices_scope.tar.gz`"*):
>
> ```
> https://amzndevresources.com/vega/media-player/shaka-rel-v4.8.5-r1.7-devices_scope.tar.gz
> ```

**🏁 Checkpoint:** After the upgrade, verify:
- ✅ The app launches without errors
- ✅ `ShakaPlayer.ts` now reports version `4.8.5`
- ✅ Video playback works — navigate to a video and play it
- ✅ Adaptive bitrate switching and playback controls (play, pause, seek) still work

---

## About the Upgrade

To have the agent explain what changed, ask:

```
What did you change to upgrade Shaka Player, and what's new in 4.8.5 compared to 4.6.18?
```

---

**Previous:** [Diagnose UI Fluidity](4_diagnose_ui_fluidity.md) | **Next:** [Wrap Up and Feedback](6_wrap_up_and_feedback.md)
