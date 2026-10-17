---
name: writing-plans
description: >-
  Use this skill when asked to create complex system automation, deployment scripts, or cross-platform tasks. It forces the creation of a step-by-step plan before coding.
---
# Script Planning Protocol

Before writing any complex Bash or PowerShell script, you MUST create a plan and present it to the user.

1. **Requirements Gathering**: Identify the target OS (Linux, Windows 10/11, Windows Server), required permissions, and dependencies.
2. **Step-by-step logic**: Write a numbered list of what the script will do sequentially.
3. **Error Handling Strategy**: Explicitly state how errors will be handled (e.g., `set -e` in bash, `Try/Catch` or `ErrorAction Stop` in PowerShell).
4. **Rollback Strategy**: If the script modifies system state, describe how to revert changes if it fails halfway.
5. **Wait for Approval**: Do not write the full code until the user approves the plan.
