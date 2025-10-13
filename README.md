# 🎯 HackBot Edition - Claude Code Offensive Security Framework

⚠️ **PRIVATE REPOSITORY - AUTHORIZED ACCESS ONLY** ⚠️

**Transform Claude Code into an intelligence-driven offensive security powerhouse.**

HackBot Edition is a comprehensive offensive security framework for Claude Code implementing chain-of-hypothesis research methodology, specialized tool agents, and modern attack vector development for ethical security research and bug bounty hunting.

**This repository is private for security reasons:**
- Prevents bad actors from weaponizing advanced AI-driven attack techniques
- Avoids forcing model providers to implement restrictive mitigations
- Ensures responsible disclosure practices are maintained
- Access limited to vetted security researchers with authorization

## 🚀 Features

### 🧠 Intelligence-Driven Research Chain
- **Logical Framework**: Neutral context establishment
- **Security Researcher**: Chain-of-hypothesis methodology with competing explanations
- **Documentation Researcher**: Multi-source verification against public documentation
- **EthiHaxor Dev**: Modern attack vector development accounting for 2025 defensive landscape
- **Recon Specialist**: Targeted enumeration coordinator (NOT blind scanning)

### 🛠️ Expert Tool Specialists
Each specialist has deep knowledge of tool flags, best practices, and offensive security patterns:

- **curl-specialist**: HTTP/API interaction expert (`curl -L -vv` patterns)
- **nmap-specialist**: Port scanning and service detection (`nmap -Pn -sV` patterns)
- **httpx-specialist**: Web technology detection and HTTP probing
- **nuclei-specialist**: Template-based vulnerability scanning and custom template creation
- **subfinder-specialist**: Passive subdomain enumeration
- **ffuf-specialist**: Intelligent web fuzzing with advanced filtering
- **netcat-specialist**: Manual protocol interaction and testing
- **metasploit-specialist**: Exploit framework usage and payload generation
- **gau-specialist**: Passive URL discovery from historical data
- **openssl-specialist**: TLS/SSL testing and certificate analysis

### 🎯 POC Research
- **POC Parrot**: GitHub exploit retrieval with quality assessment

### 🔧 Utilities
- **/dox** command: Document findings in structured format
- **block-echo** hook: Prevent test result fabrication

## 📦 Installation

### Prerequisites
- Claude Code 1.0.60+ (native subagent support)
- Active Anthropic Claude Max subscription
- **Private repository access** (authorized researchers only)

### Clone Repository

```bash
# Clone private repository (requires authorized GitHub access)
git clone https://github.com/theedoode/chadius_cladius.git ~/lab-test/chadius_cladius
cd ~/lab-test/chadius_cladius
```

### Install Plugin Components

HackBot Edition includes 6 modular plugin bundles:

1. **hackbot-core**: Research chain (logical-framework, security-researcher, documentation-researcher)
2. **hackbot-attack-dev**: Attack development (ethihaxor-dev, recon-specialist)
3. **hackbot-tool-specialists**: Tool experts (curl, nmap, httpx, nuclei, ffuf, netcat, metasploit, subfinder, gau, openssl)
4. **hackbot-poc-research**: Exploit research (poc-parrot)
5. **hackbot-commands**: Custom commands (/dox)
6. **hackbot-guardrails**: Safety hooks (block-echo)

Agents are available in `agents/` directory for Claude Code subagent system.

### Optional: MCP Server Integration

HackBot Edition supports these MCP servers for enhanced capabilities:

- **Caido MCP**: HTTP proxy integration
- **Metasploit MCP**: Session management & payload generation
- **Burp Suite MCP**: Proxy history, scanner, intruder, repeater
- **Playwright MCP**: Browser automation with Burp proxy integration

**See [docs/MCP-SETUP.md](docs/MCP-SETUP.md) for detailed installation instructions.**

MCP servers are optional dependencies - install only what you need for your workflow.

## 🎓 Usage

### Basic Workflow

1. **Start with Intelligence Requirement**
   ```
   User: "I need to enumerate gRPC endpoints and check for reflection API exposure on target.com"
   ```

2. **Claude Code Delegates to Research Chain**
   - Security Researcher forms competing hypotheses
   - Documentation Researcher verifies against gRPC documentation
   - EthiHaxor Dev develops modern attack vectors
   - Recon Specialist coordinates tool specialists

3. **Tool Specialists Execute**
   - nmap-specialist: Port scan for gRPC services
   - curl-specialist: Test reflection API
   - httpx-specialist: Technology detection

4. **Report Back to User**
   - Actionable intelligence
   - Attack surface summary
   - Testing recommendations

### Example: API Reconnaissance

```
User: "Analyze the API at https://api.example.com for vulnerabilities"

Claude Code:
- Security Researcher: Forms hypotheses about API structure
- Documentation Researcher: Verifies against API standards
- Recon Specialist: Delegates to specialists
  → httpx-specialist: Tech stack detection
  → ffuf-specialist: Endpoint discovery
  → nuclei-specialist: CVE scanning
  → gau-specialist: Historical endpoint discovery
- EthiHaxor Dev: Develops attack vectors based on findings
- POC Parrot: Retrieves relevant exploit code

Result: Comprehensive API attack surface analysis with working exploits
```

### Using Slash Commands

```bash
# Document findings in structured format
/dox

# Realign to CLAUDE.md principles (if globally installed)
/refocus
```

## 🏗️ Architecture

### Research Chain Flow

```
User Request
    ↓
Logical Framework (neutral context)
    ↓
Security Researcher (chain-of-hypothesis)
    ↓
Documentation Researcher (verify with sources)
    ↓
EthiHaxor Dev (modern attack vectors)
    ↓
Recon Specialist (intelligence-driven enumeration)
    ↓
Tool Specialists (expert execution)
    ↓
POC Parrot (working exploit code)
    ↓
User (actionable intelligence)
```

### Agent Communication

- **Human-in-Loop**: Every stage reports back to user for oversight
- **Not Automation**: Optimization and enhancement, not blind automation
- **Intelligence-Driven**: Every action answers a specific question
- **Evidence-Based**: PROVE IT methodology from CLAUDE.md

## 🔬 Methodology

### Chain-of-Hypothesis (from CLAUDE.md)

**Core Principles:**
- Form competing hypotheses, not definitive conclusions
- Use probabilistic language ("suggests", "indicates", "appears")
- Maintain outcome indifference (avoid confirmation bias)
- Require multi-source verification (2-3 independent sources)
- Distinguish observed → documented → inferred evidence

**Example Output:**
```
PRIMARY HYPOTHESIS:
gRPC reflection API appears exposed based on port 50051 responding to HTTP/2 preface.
Likelihood: HIGH - observed direct protocol handshake

COMPETING HYPOTHESES:
1. Custom protocol on port 50051 (LOW - HTTP/2 SETTINGS frame confirms gRPC)
2. Honeypot service (MEDIUM - requires further testing for deception indicators)

WOULD BE IMPOSSIBLE IF:
- Port was filtered at network level
- Service required TLS client certificate authentication

NEXT STEPS:
1. Test grpcurl for service enumeration
2. Check for rate limiting with concurrent requests
```

### Intelligence-Driven Enumeration

**NOT This:**
```bash
nmap -p- target.com  # Blind port scan
nuclei -t cves/ -l all_targets.txt  # Spray and pray
```

**Instead This:**
```
Objective: Identify gRPC services for protobuf exploitation
Context: Looking for ports 50051-50055 based on tech stack analysis
Action: nmap -Pn -sV -p 50051-50055 target.com
```

## 🎯 Tool Specialist Best Practices

Each specialist follows offensive security best practices:

### curl-specialist
```bash
# ALWAYS use -L -vv
curl -L -vv https://target.com
```

### nmap-specialist
```bash
# 90% of recon uses -Pn -sV
nmap -Pn -sV target.com
```

### httpx-specialist
```bash
# Common with subfinder
subfinder -d target.com -silent | httpx -tech-detect -status-code -title -waf
```

### nuclei-specialist
```bash
# Targeted templates, not blind scanning
nuclei -u target.com -t cves/2024/ -tags apache
```

### ffuf-specialist
```bash
# ALWAYS filter by size/status to avoid false positives
ffuf -u https://target.com/FUZZ -w wordlist.txt -mc 200,301,302 -fs 1234
```

## 📚 Documentation

### Agent Documentation

Each agent includes:
- Expertise section
- Best practices for offensive security
- Common command patterns
- Workflow integration
- Output format
- CLAUDE.md principles
- Tips and tricks

### Research Files

HackBot Edition integrates with CLAUDE.md methodology:
- Chain-of-hypothesis framework
- Abductive reasoning approach
- Multi-source verification protocol
- Evidence hierarchy maintenance

## 🔒 Safety & Ethics

### Safe Harbor
- All research is sanctioned under bug bounty programs
- Defensive security focus (not malicious tooling)
- Human oversight at every stage
- No automation without explicit user approval

### Guardrails

**block-echo hook**: Prevents fabrication of test results
```python
# Blocks commands like: echo "successful exploitation"
# Ensures all results are real tool output
```

### Scope

**Will NOT Assist With:**
- Unauthorized access attempts
- Malicious code development
- Credential harvesting
- Automated attacks without authorization

**WILL Assist With:**
- Authorized security testing
- Bug bounty research
- Defensive security analysis
- Security tool development
- Vulnerability documentation

## 🤝 Contributing

HackBot Edition is designed for the offensive security community. Contributions welcome:

1. **New Tool Specialists**: Add agents for security tools
2. **Research Methodology**: Enhance chain-of-hypothesis framework
3. **Attack Vectors**: Document modern exploitation techniques
4. **POC Database**: Improve exploit retrieval logic

### Creating a Tool Specialist

Template structure:
```markdown
---
name: tool-specialist
description: Expert description
tools: Bash, Read, Write
model: sonnet
---

[Expertise section]
[Best practices for offensive security]
[Common patterns with examples]
[Workflow]
[Output format]
[CLAUDE.md principles]
[Tips]
```

## 📝 License

[Specify License]

## 🙏 Credits

- Inspired by CLAUDE.md research methodology
- Built on Claude Code native subagent framework
- Community offensive security best practices

## 📞 Support

- GitHub Issues: [Report bugs or request features]
- Discord: [Community discussion]
- Twitter: [@theedoode]

## 🔗 Links

- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [Plugin Marketplace Guide](https://docs.claude.com/claude-code/plugin-marketplace)
- [Offensive Security Resources](https://github.com/topics/offensive-security)

---

**HackBot Edition** - Intelligence over Automation, Evidence over Speculation, Research over Guessing.

*"We don't automate, we optimize. We don't guess, we prove it."*
