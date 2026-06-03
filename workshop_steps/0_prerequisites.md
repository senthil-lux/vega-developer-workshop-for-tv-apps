# Prerequisites

## Step 1: Install MCP Server

Install the Amazon Devices Builder Tools MCP server by running the following command in a terminal window:

```bash
# Create a workspace directory for the workshop
mkdir ~/vegaWorkshop && cd ~/vegaWorkshop

# Install MCP and steering document
npx -y @amazon-devices/amazon-devices-buildertools-mcp@latest init-context
```
You can read more about this tools here https://developer.amazon.com/docs/vega/0.22/mcp-server.html .


This will prompt you to select your AI coding assistant and configure the MCP server for it.

Verify your setup is correct, run the following command in the terminal window:

```bash
npx -y @amazon-devices/amazon-devices-buildertools-mcp@latest check-status
```

You should see your agent's context document and MCP configuration as ✅ Configured.

**Verify MCP Version**:

Run the following command in the terminal window and ensure version is `0.1.25` or higher.

```bash
npx -y @amazon-devices/amazon-devices-buildertools-mcp@latest --version
```

> To use our MCP (Model Context Protocol) server or AI prompts you will need at-least one AI Coding assistant such as Cursor, Claude Code, Copilot, Kiro, Amazon Q, Cline, etc.
> Don't have an AI coding assistant? Try [Kiro](https://kiro.dev/) — it comes with free credits upon first use.

> ⚠️ **Important:** Enable MCP in your AI Agent if its not enabled by default

_For example, to enable MCP in Kiro IDE click on the 'Enable MCP' button:_

<img src="../images/kiro-ide-enable-mcp.png" height="400">

> For detailed MCP setup instructions and verification checkpoints, see the [MCP Server Setup Reference](references/2_set_up_mcp_server.md).

## Step 2: Install Vega SDK (Public)

Skip this step **if you already have the Vega SDK installed**.  if you have already installed , you can verify using AI aqgent by these steps:

Open your AI coding assistant that you installed the MCP in the `~/vegaWorkshop` directory and run the following prompt:

```
Verify if Vega sdk is installed. 
```

if not install, fowllow below steps:

```
Help me install Vega SDK
```

The MCP server will guide your AI assistant through the SDK installation.

For full public SDK setup details, see the [Download and Installation Guide](https://developer.amazon.com/docs/vega/0.22/setup-overview.html).

Depending on network speeds, this installation can take 5-15 minutes. We strongly recommend you download and install prior to the workshop.

---

**Next:** [Clone and Run Reference App](1_clone_and_run_reference_app.md)
