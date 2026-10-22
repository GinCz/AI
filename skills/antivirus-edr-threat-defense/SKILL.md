---
name: antivirus-edr-threat-defense
description: >-
  Enterprise antivirus management, Endpoint Detection & Response (EDR), Windows Defender hardening (ASR rules, WDAC, AppLocker, Sysmon), Linux host security (Wazuh, ClamAV, Lynis, Falco, eBPF Tetragon, AppArmor/SELinux), anti-ransomware protection, memory injection mitigation, and live incident triage.
---
# Antivirus, EDR & Host Intrusion Defense Engineering

A specialized operations guide for architecting, enforcing, and operating enterprise-grade antivirus systems, Endpoint Detection and Response (EDR) agents, host-level intrusion prevention, anti-ransomware tripwires, and live incident forensics across Windows and Linux platforms.

---

## 1. Antivirus & EDR Architecture Mechanics

### Detection Engines Taxonomy:
1. **Signature & Hash Matching**: Instant static lookup (SHA-256 / Authenticode). High speed, zero overhead, but vulnerable to trivial byte polymorphism.
2. **Heuristic Analysis**: Static code decompilation scanning for suspicious API import tables (e.g. `VirtualAllocEx`, `WriteProcessMemory`, `CreateRemoteThread`).
3. **Behavioral & Dynamic Sandboxing**: Monitoring runtime actions in real time (e.g. mass file renames, shadow copy deletions, unauthorized registry persistence).
4. **Machine Learning / Cloud Telemetry**: Analyzing telemetry against global threat intelligence models to detect zero-day malware patterns.
5. **Antimalware Scan Interface (AMSI)**: In-memory runtime buffer scanning for scripts (PowerShell, VBScript, JScript, Office VBA, .NET assembly loads) before execution.

---

## 2. Enterprise Windows Defender & Host Hardening

### PowerShell Script for Full Attack Surface Reduction (ASR) Deployment:
Microsoft Defender ASR rules block malware vectors (malicious Office macros, script-based downloaders, child process spawning, LSASS credential theft):

```powershell
<#
.SYNOPSIS
    Enforce maximum enterprise Attack Surface Reduction (ASR) rules on Windows.
#>
# Enable Windows Defender Real-Time and Cloud Protection
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -MAPSReporting Advanced
Set-MpPreference -SubmitSamplesConsent SendSafeSamples
Set-MpPreference -HighThreatDefaultAction Clean
Set-MpPreference -SevereThreatDefaultAction Clean

# ASR Rule GUIDs Matrix
$ASRRules = @{
    "Block executable content from email client and webmail"          = "be9b3d45-6107-4742-bb57-1521107c476f"
    "Block Office applications from creating child processes"          = "d4f940ab-401b-4efc-aadc-ad5f3c50688a"
    "Block Office applications from creating executable content"       = "3b5764aa-aed0-4df4-bb3e-815702e4d142"
    "Block Office applications from injecting code into processes"     = "756346d7-3953-435a-9c9c-0f92860502b0"
    "Block JavaScript or VBScript from launching downloaded executable"= "d3e037e1-3eb8-44c8-a917-57927947596d"
    "Block execution of potentially obfuscated scripts"                = "5beb7efe-fd9a-4556-801d-275e5ffc04cc"
    "Block Win32 API calls from Office macros"                         = "92e97fa1-2edf-4476-bdd6-9dd0b4dddc7b"
    "Block credential stealing from Windows Local Security Authority"  = "9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2"
    "Block process creations originating from PSExec and WMI commands" = "d1e49aac-8f56-4280-b9ba-993a6d77406c"
    "Block untrusted and unsigned processes that run from USB"         = "b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4"
    "Block persistence through WMI event subscription"                 = "e6db77e5-3e12-4247-81d7-0e0e5fe2b0d4"
    "Use advanced protection against ransomware"                       = "c1db55ab-c21a-4637-bb3f-a12568109d35"
}

foreach ($RuleName in $ASRRules.Keys) {
    $RuleGuid = $ASRRules[$RuleName]
    Add-MpPreference -AttackSurfaceReductionRules_Ids $RuleGuid -AttackSurfaceReductionRules_Actions Enabled
    Write-Output "ASR Rule Enforced: $RuleName ($RuleGuid)"
}

# Enforce Controlled Folder Access (Anti-Ransomware Shield)
Set-MpPreference -EnableControlledFolderAccess Enabled
```

### Windows Event Telemetry & Sysmon Deployment:
- Deploy Sysmon with SwiftOnSecurity configuration (`sysmon.exe -i sysmonconfig-export.xml`).
- Crucial Event IDs to monitor in SIEM:
  - **Event ID 1**: Process Creation (Command line, hashes, parent process).
  - **Event ID 7**: Image Loaded (DLL hijacking detection).
  - **Event ID 8**: CreateRemoteThread (Process injection indicator).
  - **Event ID 10**: ProcessAccess (LSASS access attempts).
  - **Event ID 11**: FileCreate (Ransomware staging, drop of executables).
  - **Event ID 12/13/14**: RegistryEvent (Persistence modifications).

---

## 3. Linux Host Intrusion Prevention & EDR (Wazuh & Falco)

### Wazuh Agent Deployment & Configuration:
Install and configure Wazuh agent to monitor log integrity, rootkits, and active response:
```bash
# Register agent with manager securely
WAZUH_MANAGER="manager.internal.gincz.com"
/var/ossec/bin/agent-auth -m "${WAZUH_MANAGER}" -P "AgentEnrollmentSecret123"

# Start and enable Wazuh agent
systemctl enable --now wazuh-agent
```

### Falco Runtime Syscall Monitoring (`/etc/falco/rules.d/custom_rules.yaml`):
```yaml
- rule: Shell Spawned by Ingress Container
  desc: Detect when a shell is launched inside a web-facing or production container
  condition: container.id != host and proc.name in (bash, sh, zsh, ksh) and evt.type = execve and not proc.pname in (entrypoint, docker-init)
  output: "CRITICAL: Suspicious shell spawned in container (user=%user.name container_id=%container.id container_name=%container.name cmdline=%proc.cmdline)"
  priority: CRITICAL
  tags: [mitre_execution, container]

- rule: Sensitive File Read (/etc/shadow)
  desc: Detect unauthorized access to password database
  condition: open_read and fd.name = "/etc/shadow" and not user.name in (root)
  output: "ALERT: Unauthorized attempt to read /etc/shadow (user=%user.name process=%proc.name cmdline=%proc.cmdline)"
  priority: WARNING
```

### ClamAV Real-Time On-Access Daemon (`/etc/clamav/clamd.conf`):
```ini
# Enforce On-Access scanning on high-risk directories
OnAccessMountPath /tmp
OnAccessMountPath /var/www/uploads
OnAccessIncludePath /home
OnAccessPrevention yes
OnAccessExtraScanning yes
OnAccessExcludeUname clamav
```

---

## 4. Anti-Ransomware Defenses & Tripwires

1. **Volume Shadow Copy Protection**:
   - Deny `vssadmin.exe delete shadows` and `wmic shadowcopy delete` via AppLocker and ASR rules.
2. **Canary Honeypot Files**:
   - Place hidden decoy files (e.g. `C:\Users\Public\Documents\!decoy_financial_statement.xlsx` or `/var/www/!canary.docx`) with strict auditing enabled.
   - Any write, rename, or delete event immediately triggers a high-priority alert and network isolation script.
3. **Immutable 3-2-1-1-0 Backup Standard**:
   - 3 copies of data, 2 different media types, 1 offsite, 1 offline (air-gapped or immutable S3 Object Lock), 0 errors after automated restore verification.

---

## 5. Live Incident Response & Triage Workflows

### Windows Live Triage Script:
```powershell
# Gather volatile evidence into triage artifact directory
$TriageDir = "C:\Triage_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path $TriageDir -Force | Out-Null

# 1. Active Network Connections with Process IDs
Get-NetTCPConnection | Select-Object LocalAddress,LocalPort,RemoteAddress,RemotePort,State,OwningProcess | 
    Export-Csv -Path "$TriageDir\Active_TCP_Connections.csv" -NoTypeInformation

# 2. Running Processes with Command Lines and Parent PIDs
Get-CimInstance Win32_Process | Select-Object ProcessId,ParentProcessId,Name,CommandLine,ExecutablePath |
    Export-Csv -Path "$TriageDir\Running_Processes.csv" -NoTypeInformation

# 3. Scheduled Tasks & Persistence Keys
Get-ScheduledTask | Where-Object { $_.State -ne 'Disabled' } | Select-Object TaskName,TaskPath |
    Export-Csv -Path "$TriageDir\ScheduledTasks.csv" -NoTypeInformation

Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" | Out-File "$TriageDir\Registry_HKLM_Run.txt"
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" | Out-File "$TriageDir\Registry_HKCU_Run.txt"
```

### Linux Live Triage Commands:
```bash
# Memory and running socket inspection
ss -tunap > /tmp/triage_sockets.txt
ps auxfww > /tmp/triage_processes.txt

# Audit open files of suspicious processes
lsof -i -P -n > /tmp/triage_network_files.txt

# Inspect recent persistence modifications
find /etc/cron* /etc/systemd/system /var/spool/cron -mtime -2 -ls > /tmp/recent_persistence.txt
