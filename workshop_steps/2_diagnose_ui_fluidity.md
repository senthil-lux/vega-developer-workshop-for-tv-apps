# Diagnose and Fix UI Fluidity Issues

TV apps require smooth 60fps rendering for a good user experience. In this exercise, you'll use your AI agent to check out a branch with an intentional performance bug, build and run the app on your Fire TV device, then diagnose and fix UI fluidity issues — all through chat prompts.

## Prompts at a Glance

This exercise requires **3 prompts** to your AI agent. Here's the full sequence:

| # | Type | What You Do |
|---|------|-------------|
| 🤖 Prompt 1 | AI Agent | `Checkout the perf-demo branch, clean previous builds (build and node_modules directories) and build the Debug variant via npm. Then install and launch the vega app on my Fire TV device using vega sdk` |
| 🤖 Prompt 2 | AI Agent | `How is my app's UI fluidity performance? Can you check and make improvements using vega workflow?` |
| 🤖 Prompt 3 | AI Agent | `Yes. Proceed with rebuilding, reinstalling the app, and remeasuring UI fluidity` |

## Prerequisites

Before starting this exercise, make sure you have:

- [ ] Completed [Clone and Run Reference App](1_clone_and_run_reference_app.md)
- [ ] Completed [Set Up MCP Server](2_set_up_mcp_server.md) and verified the MCP server is connected
- [ ] A physical Vega device connected 
---

## Step 1: Check Out the Branch

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
5. Deploy and launch the app on your connected Fire TV device (`vega device install-app --dir . -b Debug` followed by `vega device launch-app --dir .`)

**🏁 Checkpoint:** You should be on the `perf-demo` branch with a clean build directory. The app should launch and you can navigate with the D-pad. You may notice some lag while scrolling — that's the bug we're about to diagnose.

---

## Step 2: Diagnose and Fix UI Fluidity

### 🤖 Prompt 2

Copy and paste this into your AI agent's chat:

```
How is my app's UI fluidity performance? 
```

You might see the report like this : 
<img width="600" height="800" alt="image" src="https://github.com/user-attachments/assets/661e8fd3-e146-4474-ac7c-719b32769e83" />


The agent will follow the workflow from the MCP server. It will:

1. Read the workflow document `react_native_for_vega_diagnose_ui_fluidity`
2. Analyze results, identify the time period where the biggest fluidity drop occured

Now copy and paste the below command :
```
Can you check and make improvements using vega workflow?
```

The agent will continue low the workflow from the MCP server. It will:

4. Identify hot functions in the above time period using `get_app_hot_functions`
5. Apply code optimizations

**🏁 Checkpoint:** The agent should report UI Fluidity KPI FAILING as below 

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

 and apply optimizations to `HomeScreen.tsx`. Below is the fix by Kiro, as exmaple. The reporting might vary based on your coding agent.

<img width="970" height="1344" alt="image" src="https://github.com/user-attachments/assets/37fde8aa-661e-46a9-b56b-dd0982c7e81c" />

After the agent applies optimizations, it will ask if you'd like to rebuild and re-measure. If build was done part of revious prompt itself ,  just ask to remeasure UI fluidity

```
Yes. Proceed with rebuilding, reinstalling the app, and remeasuring UI fluidity. 
```

or 

```
Remeasure UI fluidity. 
```

The agent will:
1. Rebuild the app in Debug mode
2. Reinstall on your device
3. Re-run the KPI Visualizer to measure the new fluidity score

**🏁 Checkpoint:** The fluidity score should improve significantly from the baseline toward the ≥99% target. Here's the  report from Kiro post fix:

<img width="948" height="1054" alt="image" src="https://github.com/user-attachments/assets/dfb383d7-a683-4de2-be03-3932f2eb62a3" />

# About the Bug

Copy paste below prompt in chat window to ask the coding agent to report the bug details:
```
What was the issue fixed to improve UI fluidity ?
```

You will get detailed report by the agent. 

---

## Summary

In this exercise, you learned to:
1. Use the `diagnose_ui_fluidity` workflow to systematically identify UI fluidity failures
2. Let the AI agent analyze CPU hot functions and apply targeted optimizations
3. Verify improvements by re-running KPI measurements

---
<summary>Appendix A: MCP Tools Used in Fluidity Diagnosis</summary>

<img width="1248" height="934" alt="image" src="https://github.com/user-attachments/assets/f1dd4976-fc99-4300-ab1b-fb04fb485405" />

---


