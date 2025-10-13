# MCP Server Setup Guide

**PRIVATE REPOSITORY - Installation instructions for authorized users only**

HackBot Edition supports these MCP (Model Context Protocol) servers for enhanced offensive security capabilities. This guide shows how to install the MCP server **packages** - you'll configure them in your own `~/.claude.json` with your paths and credentials.

---

## Prerequisites

- **Node.js** v20+ (for npm-based servers)
- **Python 3.8+** (for Python-based servers)
- **Git** (for cloning repositories)
- **Claude Code** (with active Claude Max subscription)

---

## 1. Caido MCP Server

**Purpose**: HTTP proxy integration, request history, and vulnerability testing workflows

### Installation

```bash
# Clone repository
git clone https://github.com/Ebka-Caido-AI/caido-mcp-server.git ~/lab-test/tools/Ebka-Caido-AI

# Build the server
cd ~/lab-test/tools/Ebka-Caido-AI/claude-mcp-server
npm install
npm run build
```

### Configuration Example

Add to your `~/.claude.json` under `mcpServers`:

```json
"caido": {
  "type": "stdio",
  "command": "node",
  "args": [
    "/absolute/path/to/Ebka-Caido-AI/claude-mcp-server/build/index.js"
  ],
  "env": {}
}
```

**Replace** `/absolute/path/to/` with your actual installation path.

---

## 2. Metasploit MCP Server

**Purpose**: Meterpreter session management, payload generation, post-exploitation modules, exploit execution

### Installation

```bash
# Clone repository
git clone https://github.com/GH05TCREW/MetasploitMCP.git ~/lab-test/tools/MetasploitMCP

# Create Python virtual environment
cd ~/lab-test/tools/MetasploitMCP
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Start Metasploit RPC

Metasploit MCP requires msfrpcd running:

```bash
# Start Metasploit RPC daemon (in separate terminal)
msfrpcd -P YourPasswordHere -S -a 127.0.0.1 -p 55553
```

### Configuration Example

Add to your `~/.claude.json` under `mcpServers`:

```json
"metasploit": {
  "type": "stdio",
  "command": "/absolute/path/to/MetasploitMCP/venv/bin/python",
  "args": [
    "/absolute/path/to/MetasploitMCP/MetasploitMCP.py",
    "--transport",
    "stdio"
  ],
  "env": {
    "MSF_PASSWORD": "YourPasswordHere",
    "MSF_SERVER": "127.0.0.1",
    "MSF_PORT": "55553",
    "MSF_SSL": "false"
  }
}
```

**Replace**:
- `/absolute/path/to/` with your actual installation path
- `YourPasswordHere` with your msfrpcd password

---

## 3. Burp Suite MCP Server (via mcp-proxy)

**Purpose**: Burp Suite proxy history, scanner, intruder, repeater integration

### Prerequisites

1. **Burp Suite Community/Pro** installed
2. **Burp MCP Extension** installed from BApp Store:
   - Open Burp → Extensions → BApp Store → Search "MCP Server" → Install

### Installation (mcp-proxy Bridge)

The PortSwigger Burp MCP extension uses STDIO (designed for Claude Desktop). Claude Code requires an SSE→STDIO bridge:

```bash
# Create directory and virtual environment
mkdir -p ~/lab-test/tools/mcp-proxy
cd ~/lab-test/tools/mcp-proxy
python3 -m venv venv
source venv/bin/activate

# Install mcp-proxy
pip install mcp-proxy
```

### Start Burp Suite

Ensure Burp Suite is running with the MCP extension enabled. The extension exposes an SSE endpoint at `http://127.0.0.1:9876/sse`.

### Configuration Example

Add to your `~/.claude.json` under `mcpServers`:

```json
"burp": {
  "type": "stdio",
  "command": "/absolute/path/to/mcp-proxy/venv/bin/mcp-proxy",
  "args": [
    "http://127.0.0.1:9876/sse"
  ],
  "env": {}
}
```

**Replace** `/absolute/path/to/` with your actual installation path.

**Note**: Burp Suite must be running for this MCP server to connect.

---

## 4. Playwright MCP Server

**Purpose**: Browser automation with Burp proxy integration, screenshot capture, DOM inspection, form filling

### Installation

```bash
# Install Playwright CLI globally
sudo npm install -g playwright

# Install browser binaries
playwright install chromium firefox webkit
```

### Configuration Example

Add to your `~/.claude.json` under `mcpServers`:

```json
"playwright": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "@playwright/mcp@latest",
    "--proxy-server=http://127.0.0.1:8080",
    "--block-service-workers"
  ],
  "env": {}
}
```

**Configuration Notes**:
- `--proxy-server=http://127.0.0.1:8080`: Routes ALL browser traffic through Burp Suite
- `--block-service-workers`: Prevents service workers from hijacking requests (ensures complete Burp capture)
- Change proxy port if your Burp Suite uses a different port

---

## Verification

After configuring all MCP servers in `~/.claude.json`, verify they're loaded:

```bash
claude mcp list
```

Expected output:

```
Checking MCP server health...

caido: node /path/to/Ebka-Caido-AI/... - ✓ Connected
metasploit: /path/to/MetasploitMCP/venv/bin/python ... - ✓ Connected (requires msfrpcd running)
burp: /path/to/mcp-proxy/venv/bin/mcp-proxy ... - ✓ Connected (requires Burp Suite running)
playwright: npx @playwright/mcp@latest ... - ✓ Connected
```

---

## Troubleshooting

### MCP Server Not Connecting

1. **Check absolute paths**: Ensure all paths in `~/.claude.json` are absolute, not relative
2. **Check permissions**: Ensure executables have execute permissions (`chmod +x`)
3. **Check dependencies**: Ensure Node.js/Python versions meet requirements
4. **Check background services**: Burp Suite and msfrpcd must be running for their respective MCPs

### Burp MCP Fails to Connect

- Verify Burp Suite is running
- Verify Burp MCP extension is installed and enabled
- Test SSE endpoint: `curl http://127.0.0.1:9876/sse`
- Check Burp Suite logs for MCP extension errors

### Metasploit MCP Fails to Connect

- Verify msfrpcd is running: `ps aux | grep msfrpcd`
- Verify password matches in `~/.claude.json` and msfrpcd startup
- Test RPC connection: `msfrpc -U msf -P YourPasswordHere -a 127.0.0.1 -p 55553`

### Playwright MCP Fails

- Verify Playwright CLI installed: `playwright --version`
- Verify browsers installed: `playwright install chromium`
- Check proxy port matches Burp Suite listener

---

## Architecture Notes

### Traffic Flow (Playwright + Burp)

```
Claude Code (Playwright MCP)
    ↓
Playwright Browser (Chromium/Firefox/WebKit)
    ↓ --proxy-server=127.0.0.1:8080
Burp Suite Proxy (127.0.0.1:8080)
    ↓
Target Web Application
```

**Zero Traffic Fragmentation**: `--block-service-workers` ensures ALL requests flow through Burp, no CDP bypass.

### When to Use Burp's Built-in Browser

For service worker-specific vulnerability testing (cache poisoning, push hijacking), use Burp's built-in Chromium browser instead of Playwright MCP.

---

## Security Considerations

**PRIVATE REPOSITORY**: These MCP servers enable powerful offensive security capabilities:

- **Authorized Testing Only**: Use only on systems you own or have explicit permission to test
- **Credential Management**: Never commit `~/.claude.json` or expose MCP credentials
- **Responsible Disclosure**: Report all findings through proper bug bounty/disclosure channels
- **Safe Harbor**: All HackBot Edition usage assumes ethical, authorized security research

---

## Additional Resources

- [Claude Code MCP Documentation](https://docs.claude.com/en/docs/claude-code/mcp)
- [Caido MCP Repository](https://github.com/Ebka-Caido-AI/caido-mcp-server)
- [Metasploit MCP Repository](https://github.com/GH05TCREW/MetasploitMCP)
- [Playwright MCP Repository](https://github.com/microsoft/playwright-mcp)
- [Burp Suite Extensions](https://portswigger.net/bappstore)

---

**HackBot Edition** - Intelligence over Automation, Evidence over Speculation, Research over Guessing
