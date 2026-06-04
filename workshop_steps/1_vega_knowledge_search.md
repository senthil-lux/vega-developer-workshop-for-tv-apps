# Vega Knowledge Search

Before you start building, get familiar with **Vega Knowledge Search** — the documentation search capability provided by the Amazon Devices Builder Tools MCP server.

Instead of hunting through docs manually, you can ask your AI coding assistant questions in plain language. It uses the MCP server to search the official Vega documentation and return grounded, up-to-date answers.

## How to Use It

Open your AI coding assistant (with the MCP server configured in the [prerequisites](0_prerequisites.md)) and ask any of the questions below. Try them out to see how the assistant pulls answers from the Vega documentation.

> 💡 **Tip:** Start broad, then drill down. Ask a high-level question first, then follow up with "show me a code example", "what packages do I need?", or "what are the common pitfalls?" — the assistant searches the live documentation each time.

## Getting Started

```
What is Vega and how is it different from regular React Native?
```

```
What is the structure of a Vega app project? Walk me through the key files and folders.
```

```
Which @amazon-devices packages are available for a Vega app and what does each one do?
```

```
How do I set up the Vega SDK and verify my development environment is ready?
```

## App Configuration & Manifest

```
What is the manifest.toml file and what are its required fields?
```

```
How do I declare permissions and privileges in my Vega app manifest?
```

```
How do I configure my app to play DRM-protected video? What manifest entries are required?
```

```
How do I set the app icon and package identifier for my Vega app?
```

## Navigation & Focus

```
How do I implement stack, tab, and drawer navigation in a Vega app?
```

```
How does D-pad focus management work on Vega? Explain TVFocusGuideView with an example.
```

```
How do I restore focus to the last-focused item when a user returns to a screen?
```

```
Why are touch events not firing when I navigate with the remote, and what should I use instead?
```

## Media Playback

```
How do I implement video playback in a Vega app using the W3C media APIs?
```

```
How do I integrate Shaka Player for adaptive HLS and DASH streaming on Vega?
```

```
What is the correct initialization and cleanup order for a VideoPlayer instance?
```

```
How do I handle live streams that emit BehindLiveWindow errors during playback?
```

```
How do I add closed captions and subtitle track selection to my video player?
```

## UI Components & Layout

```
How do I use the high-performance Carousel component from kepler-ui-components?
```

```
What are the rules for using useNativeDriver with animations on Vega?
```

```
How should I scale Android dp values to Vega logical pixels?
```

## Performance

```
How do I run a performance test on my Vega app and read the results?
```

```
What are the KPI targets for app launch time and UI fluidity on Vega?
```

```
How do I diagnose and fix dropped frames during D-pad scrolling?
```

```
What are the most common performance pitfalls in Vega apps and how do I avoid them?
```

## Lifecycle & Services

```
How do I implement a headless service in my Vega app?
```

```
How do I detect background and foreground transitions to release resources like the media player?
```

```
How do I persist user preferences across app launches on Vega?
```

## Accessibility

```
What are the accessibility guidelines for Vega apps, and how do I add them to my Vega app?
```

```
How do I add screen reader support and accessible labels to my components?
```

## Build, Run & Submit

```
How do I build the release variant of my app and install it on a connected Vega device?
```

```
How do I debug a crash on my Vega device and read the logs?
```

```
How do I submit my app to the Amazon Appstore?
```

```
What is the app review and certification process for Vega apps?
```

---

**Previous:** [Prerequisites](0_prerequisites.md) | **Next:** [Build, Run, and Manage the App](2_build_run_manage_app_using_prompts.md)
