---
description: Document security findings in structured format for reporting
---

<system_instruction>
Create a structured documentation of current security findings following this format:

## DOCUMENTATION REQUEST

Please provide the following information to document your findings:

1. **Target Information**
   - What is the target (domain, IP, application)?
   - What scope applies (authorized bug bounty, pentest engagement)?

2. **Vulnerability/Finding Summary**
   - What vulnerability or security issue was discovered?
   - What category does it fall under (OWASP, CWE)?

3. **Evidence**
   - What commands were executed?
   - What were the exact outputs?
   - What screenshots or artifacts exist?

4. **Impact Assessment**
   - What is the security impact (use CVSS or similar framework)?
   - What can an attacker achieve?
   - What data/systems are at risk?

5. **Reproduction Steps**
   - Exact steps to reproduce the finding
   - Prerequisites required
   - Expected vs actual behavior

6. **Remediation Recommendations**
   - What should be fixed?
   - How should it be fixed?
   - Priority level?

---

Once you provide this information, I will generate a structured report in the following formats:
- **Markdown Report**: For documentation and GitHub issues
- **JSON Export**: For tool integration
- **Bug Bounty Template**: Ready for submission (HackerOne, Bugcrowd, etc.)

**IMPORTANT REMINDER:**
- Only document PROVEN vulnerabilities with real evidence
- Use CLAUDE.md principles: PROVE IT methodology
- No speculation or inferred impact
- Evidence-based findings only
- Include all relevant command outputs and artifacts
</system_instruction>
