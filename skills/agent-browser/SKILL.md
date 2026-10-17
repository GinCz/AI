---
name: agent-browser
description: >-
  Use this skill when you lack specific knowledge about a system command, a PowerShell cmdlet, or an API, and need to consult official documentation.
---
# Official Documentation Browsing

When writing system scripts, never hallucinate parameters or flags. If unsure, use your web searching tools to find the exact official documentation.

1. **For PowerShell / Windows Server**: Search "site:learn.microsoft.com PowerShell [Cmdlet-Name]". Read the documentation for the correct Windows version.
2. **For Bash / Linux**: Search for the official man pages (e.g., "man [command] linux") or specific distribution docs (Ubuntu, Debian, RHEL).
3. **Extraction**: Only extract the relevant flags and syntax. Do not copy generic examples without understanding them.
