---
name: code-review
description: >-
  Use this skill to audit and review Bash and PowerShell scripts for security, performance, and best practices.
---
# Script Code Review Checklist

When reviewing code, evaluate it against the following criteria:

## For PowerShell (Windows)
- **Security**: Avoid `Invoke-Expression`. Validate input parameters. Ensure secure handling of credentials (use `PSCredential` instead of plain text).
- **Style**: Use full cmdlet names instead of aliases in scripts (e.g., `Get-ChildItem` instead of `ls` or `dir`). Use `PascalCase` for variables.
- **Robustness**: Are errors caught using `try/catch`? Is `[CmdletBinding()]` used for advanced functions?

## For Bash (Linux)
- **Security**: Avoid `eval`. Always quote variables to prevent word splitting and globbing issues (e.g., `"$VAR"`).
- **Robustness**: Are `set -e`, `set -u`, and `set -o pipefail` used? 
- **Portability**: Is the shebang correct (`#!/bin/bash` or `#!/usr/bin/env bash`)? Are there bashisms if the user requested POSIX compliance?

Provide a structured report with [High], [Medium], and [Low] priority fixes.
