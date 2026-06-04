# Build, Run, and Manage the App Using Prompts

We'll use a pre-built reference app rather than building one from scratch, so you can focus on the debugging and tooling workflows in the later exercises.

In this exercise you'll drive the full app lifecycle — build, install, launch, verify, and clean up — by talking to your AI assistant in plain language. Each section shows the **prompt** you give the agent; the assistant runs the right Vega tooling for you.

## In This Exercise

1. Clone the reference app and open the workspace
2. Connect your Vega device
3. Build and run the app
4. Manage the app lifecycle (install, launch, terminate, uninstall, list)
5. Verify the manifest

## Prerequisites

Before starting, make sure you have:

- [ ] Completed [Prerequisites](0_prerequisites.md) and verified the MCP server is connected
- [ ] A Fire TV Stick HD or 4K Select running Vega OS with Developer Mode enabled
- [ ] A USB cable to connect the device to your computer

> 💡 **Prompts are flexible.** The exact wording doesn't matter — the MCP server maps your intent to the right workflow. The prompts below are starting points; phrase them in your own words if you prefer.

---

## Step 1: Clone the Workshop App

In a terminal window, run:

```bash
# Navigate to the workshop directory
cd ~/vegaWorkshop

# Clone the workshop reference app repository
git clone https://github.com/senthil-lux/VegaWorkshopApp.git

# Navigate into the cloned repository
cd VegaWorkshopApp
```

## Step 2: Open the Workspace in Your AI Assistant

Open the `~/vegaWorkshop` workspace in your AI assistant.

For example, to open the folder in Kiro IDE from the terminal, run the command below — or open it from Kiro's **File** menu.

```bash
kiro ~/vegaWorkshop
```

## Step 3: Connect Your Vega Device

Connect your Fire TV device to your computer, then confirm it's detected:

```bash
vega device list
```

You should see your device listed in the output.

> ⚠️ **Device not showing up?** Check the cable connection and confirm the device is powered on with Developer Mode enabled.

## Step 4: Build and Run the App

Open your AI coding assistant (with the MCP server configured in the [prerequisites](0_prerequisites.md)) and run this prompt:

```
Build the release variant of this app using npm and install it on the connected Vega device
```

Your AI assistant uses the MCP workflows to build the app and deploy it to your connected Vega device.

Here's an example of Kiro invoking the MCP tool and the `amazon-devices-vega-build-and-run` skill:

<p align="center">
  <img src="https://github.com/user-attachments/assets/d67a68de-9b6d-4d09-bd48-f376db0a98e8" width="640" alt="Kiro invoking the MCP build-and-run skill">
  <br>
  <em>Kiro invoking the MCP build-and-run skill</em>
</p>

**🏁 Checkpoint:** The reference app launches on your device, and you can navigate it with the D-pad.

<p align="center">
  <img src="../images/XHRa9e779280eb94f8192f4393d7.png" width="640" alt="Reference app home screen on device">
  <br>
  <em>The reference app running on the device</em>
</p>

<p align="center">
  <img src="../images/vega-navigation-working-animated.gif" width="640" alt="Navigating the reference app with the remote">
  <br>
  <em>Navigating the app with the remote</em>
</p>

> 📖 Prefer to build manually? Follow the steps in the [Run apps on a device](https://developer.amazon.com/docs/vega/latest/run-apps.html) guide.

---

## Step 5: Manage the App Lifecycle

Once the app is on the device, you can run every lifecycle action through prompts. Try these one at a time — the agent runs the right Vega tooling for each.

### Build a specific variant

```
Build the Debug variant of this app using npm.
```

> The build defaults to the Release variant and validates the manifest automatically.

### Install the app

```
Install the app on my connected Vega device.
```

### Launch the app

```
Launch the app on my Vega device.
```

### Check whether the app is installed or running

```
Is the app installed and currently running on my device?
```

### List installed apps

```
List the apps installed on my Vega device.
```

### Terminate the app

```
Stop the running app on my device.
```

### Uninstall the app

```
Uninstall the app from my Vega device.
```

**🏁 Checkpoint:** You can install, launch, terminate, and uninstall the app entirely through prompts.

---

## Step 6: Verify the Manifest

Every Vega app has a `manifest.toml` that declares its package id, components, capabilities, and privileges. A malformed manifest is one of the most common reasons a build or install fails.

```
Check my app's manifest.toml for problems and explain what each section declares.
```

The agent reviews `manifest.toml` and reports any issues. Manifest validation also runs automatically during a build — you can make it explicit:

```
Build the app and fail if the manifest has any validation errors.
```

> 📖 For the full manifest schema, see the [App Manifest reference](https://developer.amazon.com/docs/vega/latest/app-manifest.html).

**🏁 Checkpoint:** The manifest validates cleanly, and you understand what its key sections (package id, components, privileges) declare.

---

> 🔀 **Heads up:** Throughout the workshop you'll switch between branches of this repo, one per exercise. Each branch contains a specific scenario — a crash bug or a performance bug — that you'll debug using the MCP server.

---

**Previous:** [Vega Knowledge Search](1_vega_knowledge_search.md) | **Next:** [Diagnose Crashes](3_diagnose_crashes.md)
