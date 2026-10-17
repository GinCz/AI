---
name: systematic-debugging
description: >-
  Use this skill when encountering errors or unexpected behavior in Bash (Linux) or PowerShell/CMD (Windows) scripts. It enforces a strict, methodical troubleshooting process.
---
# Systematic Debugging Protocol

When asked to debug a script or system issue, follow this strict protocol:

1. **Replicate & Understand**: Never guess the error. Ask the user for the exact error output, or use tools to run the script and capture the error.
2. **Check Environment**: 
   - Windows: Verify PowerShell version, Execution Policy, and Administrator privileges.
   - Linux: Verify bash version, user permissions, `$PATH`, and file execution bits (`chmod +x`).
3. **Isolate the Fault**: Do not rewrite the entire script. Add verbose logging (`set -x` in Bash, `Write-Debug` or `Set-PSDebug` in PowerShell) to isolate the exact line failing.
4. **Hypothesize & Test**: Propose one single hypothesis at a time. Do not make multiple unrelated changes.
5. **Verify**: Once a fix is applied, verify it solves the specific error without introducing new ones.
