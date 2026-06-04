# Prerequisites

Complete these steps **before** the workshop. They set up the tooling you'll use in every later exercise.

## What You'll Need

- An AI coding assistant such as Kiro, Cursor, Claude Code, Copilot, Amazon Q, or Cline.
- [Node.js and npm](https://nodejs.org/) installed (required to run the `npx` commands below).
- A terminal and roughly 15–20 minutes (most of it is the SDK download).

> Don't have an AI coding assistant? Try [Kiro](https://kiro.dev/) — it comes with free credits on first use.

## Step 1: Install the MCP Server

The Amazon Devices Builder Tools MCP server connects your AI assistant to the official Vega tooling and documentation.

In a terminal window, run:

```bash
# Create a workspace directory for the workshop
mkdir ~/vegaWorkshop && cd ~/vegaWorkshop

# Install the MCP server and steering document
npx -y @amazon-devices/amazon-devices-buildertools-mcp@latest init-context
```

This prompts you to select your AI coding assistant and configures the MCP server for it.

> 📖 Learn more about these tools in the [MCP Server documentation](https://developer.amazon.com/docs/vega/0.22/mcp-server.html).

### Verify the Installation

Confirm your setup is correct:

```bash
npx -y @amazon-devices/amazon-devices-buildertools-mcp@latest check-status
```

Your agent's context document and MCP configuration should both show as ✅ Configured.

### Verify the MCP Version

Ensure the version is `1.0.2` or higher:

```bash
npx -y @amazon-devices/amazon-devices-buildertools-mcp@latest --version
```

### Enable MCP in Your AI Assistant

> ⚠️ **Important:** If MCP isn't enabled by default in your AI assistant, enable it now.

For example, in Kiro IDE, click the **Enable MCP** button:

<img src="../images/kiro-ide-enable-mcp.png" height="400">

> For detailed setup instructions and verification checkpoints, see the [MCP Server Setup Reference](references/2_set_up_mcp_server.md).

## Step 2: Install the Vega SDK (Public)

> ✅ **Already have the Vega SDK installed?** Skip ahead — but verify first using the steps below.

Open your AI coding assistant in the `~/vegaWorkshop` directory (where you installed the MCP server) and run this prompt to check whether the SDK is already present:

```
Verify if the Vega SDK is installed.
```

If it isn't installed, run this prompt and let the assistant guide you through it:

```
Help me install the Vega SDK
```

The MCP server walks your AI assistant through the SDK installation.

> 📖 For full setup details, see the [Download and Installation Guide](https://developer.amazon.com/docs/vega/0.22/setup-overview.html).

⏱️ Depending on network speed, this can take **5–15 minutes**. We strongly recommend downloading and installing it **before** the workshop.

---

## Appendix: Verify the MCP Server Is Active in Your AI Assistant

The `check-status` command in Step 1 confirms the MCP server is *configured* on disk. This appendix shows how to confirm it's actually *connected and exposing tools* inside each AI assistant. If the assistant can't see the tools, the workshop prompts won't work.

The MCP server appears as `amazon-devices-buildertools-mcp` (or the name shown in your config). A healthy server lists its tools and shows a connected status.

### Kiro (detailed)

<details>
<summary><strong>How to verify in Kiro</strong></summary>

1. Open the **Kiro panel** (the ghost icon in the activity bar) and find the **MCP Servers** section. The Amazon Devices server should appear with a **green/connected** status indicator.
2. Alternatively, open the Command Palette and search for **MCP** to view server commands, or use the **MCP Server** view to reconnect a server without restarting Kiro.
3. In a chat session you can run the `/mcp` slash command to list the MCP servers currently loaded.

> 💡 **Tips for Kiro**
> - Servers reconnect automatically when you edit the config. If a server looks stuck, reconnect it from the MCP Server view instead of restarting Kiro.
> - MCP configs merge with precedence `user < workspace`. If a server isn't showing up, check whether it's defined at the user level (`~/.kiro/settings/mcp.json`) or in the workspace (`.kiro/settings/mcp.json`).
> - Use the `autoApprove` list in the config to skip approval prompts for trusted workshop tools, and confirm `disabled` is not set to `true`.
> - Reference: [Kiro MCP docs](https://kiro.dev/docs/mcp) and [Configuration](https://kiro.dev/docs/mcp/configuration).

</details>

### Claude Code (detailed)

<details>
<summary><strong>How to verify in Claude Code</strong></summary>

1. In an interactive session, run the `/mcp` slash command. It lists each configured server with its connection status and lets you drill into the available tools.
2. From the terminal, run `claude mcp list` to print configured servers and their connection state. Use `claude mcp get <name>` for details on a single server.
3. Run `/context` in a session to confirm the MCP tools are loaded into the context window (they appear under the MCP tools category).

> 💡 **Tips for Claude Code**
> - MCP config is shared between the CLI and the IDE extension, so you only configure it once.
> - Add servers without hand-editing JSON using `claude mcp add` (supports `--scope local|project|user`). Project-scoped servers live in `.mcp.json` and can be shared with the team.
> - If a server shows as failed, run `/mcp` to view the error, verify the command path resolves, and confirm any required environment variables are set.
> - Reference: [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp) and [Debug your configuration](https://code.claude.com/docs/en/debug-your-config).

</details>

### Cursor (summary)

<details>
<summary><strong>How to verify in Cursor</strong></summary>

Open **Cursor Settings → MCP** (or **Tools & Integrations**). Each server shows a status indicator — a **green dot** means connected — along with a tool count and any error details. If tools don't appear, check the JSON is valid, reload the Cursor window after config changes, and note Cursor's soft limit of ~40 tools per server.

Reference: [Cursor MCP docs](https://docs.cursor.com/en/context/mcp).

</details>

### Codex (summary)

<details>
<summary><strong>How to verify in Codex</strong></summary>

Codex uses **TOML** config (not JSON) and runs MCP servers locally over stdio. List configured servers with `codex mcp list` and add one with `codex mcp add`. Servers live in `config.toml` (or `mcp_servers` entries) shared between the Codex CLI and IDE extension.

Reference: [Codex MCP servers docs](https://developers.openai.com/codex/mcp).

</details>

### GitHub Copilot (VS Code) (summary)

<details>
<summary><strong>How to verify in GitHub Copilot</strong></summary>

Open the Command Palette (`Ctrl/Cmd+Shift+P`) and run **MCP: List Servers**, then select your server to view status, **Show Output** (logs), enable/disable, or restart it. You can also open the **Extensions** view, find the server under **MCP SERVERS - INSTALLED**, and check it there. In Copilot Chat, switch to **Agent** mode and click the **Configure Tools** icon to confirm the server's tools are enabled.

Reference: [Manage MCP servers in VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).

</details>

> ⚠️ All commands and UI labels above reflect the official docs at the time of writing. AI assistants update frequently — if a command or menu has moved, check the linked official documentation for the current steps.

---

**Next:** [Vega Knowledge Search](1_vega_knowledge_search.md)
