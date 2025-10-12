#!/usr/bin/env python3
"""
Block Echo Hook - Prevent fabrication of test results

This hook prevents using 'echo' commands to fake security testing results,
ensuring all outputs are genuine tool results. Part of CLAUDE.md "PROVE IT"
methodology.

Hook Type: PreToolUse
Trigger: Before Bash tool execution
Action: Block if 'echo' is used to simulate test results
"""

import re
import sys
import json


def should_block_echo(command: str) -> tuple[bool, str]:
    """
    Determine if an echo command should be blocked.

    Returns:
        (should_block, reason) tuple
    """
    command_lower = command.lower().strip()

    # Allow echo for legitimate purposes
    legitimate_patterns = [
        r'^echo\s+["\']?https?://',  # Piping URLs (echo "http://..." | tool)
        r'^echo\s+-[ne]?\s+["\']\\',  # Sending raw bytes (echo -ne '\x00\x01')
        r'echo\s+.*\|\s*\w+',  # Piping to another command (echo "data" | nc)
        r'echo\s+\$\w+',  # Environment variables (echo $PATH)
        r'^echo\s*$',  # Empty echo for newlines
    ]

    for pattern in legitimate_patterns:
        if re.search(pattern, command_lower):
            return False, ""

    # Block echo commands that look like fabricated results
    suspicious_patterns = [
        (r'echo.*vulnerable', 'Fabricating vulnerability confirmation'),
        (r'echo.*exploit.*success', 'Fabricating exploit success'),
        (r'echo.*pwned', 'Fabricating compromise confirmation'),
        (r'echo.*authenticated', 'Fabricating authentication success'),
        (r'echo.*access.*granted', 'Fabricating access confirmation'),
        (r'echo.*shell', 'Fabricating shell access'),
        (r'echo.*<\?php', 'Fabricating PHP webshell creation'),
        (r'echo.*<script>', 'Fabricating XSS payload'),
        (r'echo.*sql.*injection', 'Fabricating SQL injection success'),
        (r'echo.*root@', 'Fabricating root access'),
        (r'echo.*flag\{', 'Fabricating CTF flag capture'),
        (r'echo.*[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}.*open', 'Fabricating port scan results'),
        (r'echo.*200 OK', 'Fabricating HTTP response'),
        (r'echo.*connection established', 'Fabricating connection success'),
    ]

    for pattern, reason in suspicious_patterns:
        if re.search(pattern, command_lower):
            return True, reason

    # Block any echo that writes to a file (could be fabricating logs)
    if re.search(r'echo.*>>?\s*\w+\.(txt|log|json|xml|html)', command_lower):
        return True, "Fabricating log/result files"

    return False, ""


def main():
    """
    Main hook execution.

    Expected input (stdin): JSON with hook context
    Expected output (stdout): JSON with action (allow/block)
    """
    try:
        # Read hook context from stdin
        context = json.loads(sys.stdin.read())

        tool_name = context.get("tool_name", "")
        tool_input = context.get("tool_input", {})

        # Only check Bash tool
        if tool_name != "Bash":
            print(json.dumps({"action": "allow"}))
            return

        command = tool_input.get("command", "")

        # Check if echo should be blocked
        should_block, reason = should_block_echo(command)

        if should_block:
            response = {
                "action": "block",
                "message": f"""
🚫 BLOCKED: Echo command blocked by CLAUDE.md integrity guardrail

Reason: {reason}

The 'echo' command was blocked because it appears to be fabricating test results.

CLAUDE.md Principle: PROVE IT
- All security findings must be based on real tool output
- No fabrication of exploitation results
- No simulation of successful attacks

If you need to:
- Send data to a tool: Use legitimate tool commands
- Test payloads: Use actual security tools (curl, nc, etc.)
- Generate files: Use Write tool instead of echo redirection

Command attempted:
{command}

Please run real security tools and use their actual output instead.
""".strip()
            }
            print(json.dumps(response))
        else:
            print(json.dumps({"action": "allow"}))

    except Exception as e:
        # On error, allow (fail open to avoid breaking workflow)
        print(json.dumps({
            "action": "allow",
            "error": f"Hook error: {str(e)}"
        }))


if __name__ == "__main__":
    main()
