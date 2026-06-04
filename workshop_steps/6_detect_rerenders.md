# Detect and Fix Unnecessary Re-renders

Unnecessary component re-renders are a common, hard-to-spot cause of sluggish TV apps. In this exercise, you'll check out a branch where the home screen re-renders far more than it needs to, use the `why-did-you-render` (wdyr) tool through the MCP server to see exactly what's re-rendering and why, then fix it — all through chat prompts.

On the `rerender-demo` branch, every time you move focus between thumbnails the app updates the background image, which re-renders the **entire** home screen. Because the row and thumbnail callbacks are recreated on every render, each `ContentRow` and `ThumbnailItem` re-renders too. You'll catch this in the wdyr report and fix it.

## Prompts at a Glance

| # | Prompt | What It Does |
|---|--------|--------------|
| 1 | `Checkout the rerender-demo branch, clean previous builds (build and node_modules directories) and build the Debug variant via npm. Then install and launch the vega app on my Fire TV device using vega sdk` | Builds and deploys the re-render demo app |
| 2 | `Detect unnecessary re-renders in my Vega app using the why-did-you-render workflow.` | Instruments the app with wdyr and relaunches it with logging |
| 3 | (navigate the app, then type `DONE`) → `Analyze the re-render logs and tell me what's re-rendering unnecessarily and why.` | Reports the problem components and root causes |
| 4 | `Apply the recommended fixes to reduce the re-renders.` | Applies `useCallback` / `React.memo` optimizations |
| 5 | (navigate again, type `DONE`) → `Re-analyze the logs and compare against the previous run.` | Confirms the re-renders are gone |

## Prerequisites

Before starting this exercise, make sure you have:

- [ ] Completed [Build, Run, and Manage the App](2_build_run_manage_app_using_prompts.md)
- [ ] Completed [Prerequisites](0_prerequisites.md) and verified the MCP server is connected
- [ ] A Fire TV Stick HD or 4K Select running Vega OS with Developer Mode enabled
- [ ] Your IDE (VS Code or Kiro) open in the `VegaWorkshopApp` directory

---

## Step 1: Check Out the Branch and Run

### 🤖 Prompt 1

Copy and paste this into your AI agent's chat:

```
Checkout the rerender-demo branch, clean previous builds (build and node_modules directories) and build the Debug variant via npm. Then install and launch the vega app on my Fire TV device using vega sdk
```

The agent will:
1. Switch to the `rerender-demo` branch
2. Clean any previous build artifacts
3. Install npm dependencies
4. Build the app in Debug mode
5. Deploy and launch the app on your connected Fire TV device

**🏁 Checkpoint:** You're on the `rerender-demo` branch and the app launches so you can navigate with the D-pad. As you move focus across thumbnails, the background image changes — that focus-driven update is what we're about to investigate.

---

## Step 2: Start the Re-render Detection Workflow

### 🤖 Prompt 2

Copy and paste this into your AI agent's chat:

```
Detect unnecessary re-renders in my Vega app using the why-did-you-render workflow.
```

The agent follows the MCP `detect_component_rerender` workflow. It will:
1. Add the `@welldone-software/why-did-you-render` dev dependency
2. Inspect the home screen components and configure wdyr + Babel for them
3. Rebuild and reinstall the app in Debug mode
4. Start Metro with port forwarding and relaunch the app, streaming logs to a file

If the agent asks **which UX flow you want to monitor**, answer:

```
The home screen — focusing and scrolling through the thumbnail rows.
```

**🏁 Checkpoint:** The app is running with wdyr active, and Metro is streaming logs.

---

## Step 3: Exercise the App, Then Analyze

Using your remote, navigate the home screen for a minute or two:
- Move focus left/right along a row of thumbnails
- Move up/down between rows
- Scroll through the content

Every focus change updates the background image — watch how much re-rendering that triggers. When you're done, type `DONE` in the chat so the agent collects the logs.

### 🤖 Prompt 3

Copy and paste this into your AI agent's chat:

```
Analyze the re-render logs and tell me what's re-rendering unnecessarily and why.
```

The agent filters the wdyr log entries and reports the problem components and root causes. You'll typically see findings like:

- `ContentRow` re-renders because `onItemPress` / `onItemFocus` are **different functions with the same name** on every parent render
- `ThumbnailItem` re-renders because its `onPress` / `onFocus` props are recreated each time
- The whole cascade starts from a single state update — the background image change on focus

**🏁 Checkpoint:** You can see, in plain language, which components re-render too often and what triggers the cascade.

---

## Step 4: Apply the Fixes

### 🤖 Prompt 4

Copy and paste this into your AI agent's chat:

```
Apply the recommended fixes to reduce the re-renders.
```

The agent applies standard React optimizations, typically:
- Wrap `handleItemPress` and `handleItemFocus` in `useCallback` so they keep a stable identity
- Memoize `ContentRow` and `ThumbnailItem` with `React.memo`
- Stabilize the `renderItem` callback passed to the list

> 💡 The agent may ask you to commit or stash your current changes first so you can revert easily. Say yes — it's a good habit.

Because the wdyr workflow runs the app over Metro with Fast Refresh, the agent restarts the app to pick up the changes — no full rebuild or reinstall needed.

**🏁 Checkpoint:** The fixes are applied and the app reloads on your device.

---

## Step 5: Re-verify

Navigate the app again the same way (focus across rows, scroll), then type `DONE`.

### 🤖 Prompt 5

Copy and paste this into your AI agent's chat:

```
Re-analyze the logs and compare against the previous run.
```

**🏁 Checkpoint:** The wdyr report shows far fewer (ideally no) unnecessary re-renders for `ContentRow` and `ThumbnailItem` when focus changes. Navigation feels the same to you, but the app does much less work per focus change.

---

## About the Fix

To have the agent explain what it changed and why it works, ask:

```
What caused the unnecessary re-renders, and how did the fixes resolve them?
```

You'll get a breakdown of the stable-identity pattern (`useCallback` + `React.memo`) and why recreating callbacks on every render defeats memoization.

---

## Cleanup

When you're done, have the agent restore the production configuration:

```
Clean up the why-did-you-render instrumentation and stop Metro.
```

The agent removes the wdyr import and annotations, restores `babel.config.js`, and stops Metro and port forwarding. The `why-did-you-render` package stays as a dev dependency for future debugging.

> ⚠️ Never ship `why-did-you-render` in a production build — it significantly impacts performance. It belongs in `devDependencies` and must be disabled for release.

---

## Summary

In this exercise, you learned to:
1. Instrument a Vega app with `why-did-you-render` through the MCP workflow
2. Capture and analyze re-render logs while interacting with the app
3. Apply `useCallback` and `React.memo` to eliminate unnecessary re-renders
4. Verify the improvement without a full rebuild

---

**Previous:** [Diagnose UI Fluidity](4_diagnose_ui_fluidity.md) | **Next:** [Wrap Up and Next Steps](5_wrap_up_and_next_steps.md)
