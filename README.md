# Vega Developer Workshop for TV Apps

<p align="center">
  <img src="./images/workshop-banner.png" width="100%" alt="Vega Developer Workshop — build, verify, and ship TV apps with AI assistance">
</p>

Welcome! This hands-on workshop walks you through using [Amazon's Vega Developer Tools](https://developer.amazon.com/apps-and-games/vega) and the `@amazon-devices/amazon-devices-buildertools-mcp` MCP server to build, debug, and optimize TV apps with AI assistance.

## What You'll Do

You'll clone a pre-built TV streaming reference app and use AI-powered MCP tools — entirely through chat prompts — to:

- Search the official Vega documentation in plain language
- Build, install, launch, and manage the app on a device
- Diagnose and fix an app crash
- Diagnose and fix a UI fluidity (performance) issue
- Detect and fix unnecessary component re-renders

<img src="./images/screen1-list.png" width="640">

## What You'll Learn

- How to use the `@amazon-devices/amazon-devices-buildertools-mcp` MCP server with AI coding assistants
- App lifecycle workflows (build, install, launch, verify) driven by prompts
- Crash debugging workflows with AI-assisted ACR analysis
- Performance debugging techniques for TV apps (UI fluidity, re-renders)

## Prerequisites

Check out the [Prerequisites](workshop_steps/0_prerequisites.md) page to set up the Vega SDK and the MCP server. You'll need a Fire TV Stick HD or 4K Select running Vega OS with [Developer Mode](https://developer.amazon.com/docs/vega/0.22/developer-mode.html) enabled to run the exercises.

## Workshop Steps

> Several exercises use a separate branch in the [VegaWorkshopApp](https://github.com/senthil-lux/VegaWorkshopApp) repository. The prompt in each step checks out the right branch for you.

| # | Step | Branch | What You'll Do |
|---|------|--------|----------------|
| 0 | **[Prerequisites](workshop_steps/0_prerequisites.md)** | — | Install the Vega SDK and configure the MCP server |
| 1 | **[Vega Knowledge Search](workshop_steps/1_vega_knowledge_search.md)** | — | Ask the MCP server questions against the official Vega docs |
| 2 | **[Build, Run, and Manage the App](workshop_steps/2_build_run_manage_app_using_prompts.md)** | `main` | Clone, build, install, launch, and manage the app via prompts |
| 3 | **[Diagnose Crashes](workshop_steps/3_diagnose_crashes.md)** | `crash-demo` | Trigger a crash and fix it with AI-assisted ACR analysis |
| 4 | **[Diagnose UI Fluidity](workshop_steps/4_diagnose_ui_fluidity.md)** | `perf-demo` | Measure, diagnose, and fix a UI fluidity issue |
| 5 | **[Shaka Player Upgrade](workshop_steps/5_shaka_player_upgrade.md)** | `shaka_player` | Upgrade Shaka Player from 4.6.18 to 4.8.5-r1.7 via MCP |
| 6 | **[Wrap Up and Feedback](workshop_steps/6_wrap_up_and_feedback.md)** | — | Survey, recap, and where to go next |

## Getting Started

Begin with the [Prerequisites](workshop_steps/0_prerequisites.md) to install the required tools, then follow the steps in order. Each page links to the next.

## Troubleshooting

Running into issues? Check the [troubleshooting guide](https://developer.amazon.com/docs/vega/0.22/troubleshoot-overview.html) on the [Vega Developer Docs](https://developer.amazon.com/apps-and-games/vega).
