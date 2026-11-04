# Windows Update Power Flyout Suppression & Pending State Purge

## Technical Background: Why Standard Methods Fail
In Windows 10 (1903+) and Windows 11, the power menus in the **Start Menu** and **Win + X (Quick Link menu)** are no longer governed by legacy Group Policy settings such as `NoAUWithShutDownOption` (which only affects the classic `Alt + F4` desktop dialog).

Instead, the modern Windows Shell (`explorer.exe`, `twinui.pcshell.dll`, `StartMenuExperienceHost.exe`) queries the **Update Session Orchestrator (USO)** to build the dynamic "Shutdown Flyout".

When an update is staged or downloaded:
1. Orchestrator sets `ShutdownFlyoutOptions` (bitmask 1-15) and `EnhancedShutdownEnabled = 1` in `HKLM:\SOFTWARE\Microsoft\WindowsUpdate\Orchestrator`.
2. As long as `ShutdownFlyoutOptions` is non-zero, the shell forcefully injects **"Update and shut down"** and **"Update and restart"** into the Win+X and Start power flyouts, even if all update files are deleted and the computer has already rebooted.
3. Windows Update Medic Service (`WaaSMedicSvc`) and Update Orchestrator (`UsoSvc`) periodically re-enable `wuauserv` unless services are disabled at the registry service level (`Start = 4`).
4. The Component Based Servicing (CBS) key `HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending` is owned by `NT SERVICE\TrustedInstaller`. Deleting it via standard elevated PowerShell fails silently with *Access Denied* unless `SeTakeOwnershipPrivilege` and `SeRestorePrivilege` are enabled in the calling process token.

---

## Canonical Remediation Workflow

### 1. Orchestrator Flyout Override (Immediate Menu Fix)
Force `ShutdownFlyoutOptions` and `EnhancedShutdownEnabled` to `0` across HKLM and HKCU:
```powershell
$orchestratorKeys = @(
    "HKLM:\SOFTWARE\Microsoft\WindowsUpdate\Orchestrator",
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Orchestrator",
    "HKCU:\Software\Microsoft\WindowsUpdate\Orchestrator"
)

foreach ($keyPath in $orchestratorKeys) {
    if (-not (Test-Path $keyPath)) { New-Item -Path $keyPath -Force | Out-Null }
    Set-ItemProperty -Path $keyPath -Name "ShutdownFlyoutOptions" -Value 0 -Type DWord -Force
    Set-ItemProperty -Path $keyPath -Name "EnhancedShutdownEnabled" -Value 0 -Type DWord -Force
    Set-ItemProperty -Path $keyPath -Name "FlightedEnhancedShutdownEnabled" -Value 0 -Type DWord -Force
}
```

### 2. Low-Level Service Disabling (Registry Service Level)
Prevent Windows from self-healing and restarting the update engine:
```powershell
$services = @("UsoSvc", "WaaSMedicSvc", "wuauserv")
foreach ($svc in $services) {
    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\$svc" -Name "Start" -Value 4 -Type DWord -Force
}
```

### 3. Session Manager File Queue Removal
Clear pending file renames which signal Explorer that updates are pending:
```powershell
$smPath = "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager"
Remove-ItemProperty -Path $smPath -Name "PendingFileRenameOperations" -Force -ErrorAction SilentlyContinue
Remove-ItemProperty -Path $smPath -Name "PendingFileRenameOperations2" -Force -ErrorAction SilentlyContinue
```

### 4. TrustedInstaller CBS Key Purge (Token Privilege Elevation)
Enable token privileges via C# Win32 P/Invoke (`OpenProcessToken` / `AdjustTokenPrivileges`):
- `SeTakeOwnershipPrivilege`
- `SeBackupPrivilege`
- `SeRestorePrivilege`

Take ownership with the Builtin Administrators SID (`S-1-5-32-544`), grant Full Control, and delete:
- `HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending`
- `HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootInProgress`
- `HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\PackagesPending`

### 5. Shell Process Refresh
Restart `explorer.exe` and `StartMenuExperienceHost.exe` to immediately rebuild power menus without requiring a reboot.
