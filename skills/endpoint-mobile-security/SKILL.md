---
name: endpoint-mobile-security
description: >-
  Workstation, laptop, and mobile endpoint security: BitLocker/LUKS encryption, UEFI/Secure Boot, browser hardening, public Wi-Fi defense (VPN kill-switch), Android application security (APK analysis, jadx, permissions), spyware defense, and SIM swap mitigation.
---
# Endpoint, Workstation & Mobile Security

A comprehensive operational security guide for hardening workstations, laptops, and mobile devices (Android / iOS) against physical compromise, malicious software, network surveillance, and targeted spyware.

---

## 1. Laptop & Workstation Physical Security & Boot Integrity

### A. Boot & Firmware Security:
- **UEFI Secure Boot**: Enforce Secure Boot to guarantee that only cryptographically signed bootloaders (Windows Boot Manager, signed GRUB) can execute, preventing bootkits and evil maid attacks.
- **UEFI / BIOS Administrator Password**: Lock BIOS/UEFI access with a strong administrator password to prevent unauthorized changes to boot order or disabling security chips.
- **DMA (Direct Memory Access) Attack Mitigation**: Enable Kernel DMA Protection in BIOS/OS to neutralize malicious Thunderbolt/PCIe peripheral DMA exploits.

### B. Full-Disk Encryption (FDE):
- **Windows (BitLocker with TPM + Startup PIN)**:
  - Default TPM-only mode is vulnerable to physical TPM bus sniffing.
  - Enforce **TPM + Startup PIN** via Group Policy (`Computer Configuration -> Administrative Templates -> Windows Components -> BitLocker Drive Encryption -> Operating System Drives -> Require additional authentication at startup`).
  - Encryption algorithm: **XTS-AES 256-bit**.
- **Linux (LUKS2 with Argon2id)**:
  - Use `cryptsetup luksFormat --type luks2 --pbkdf argon2id /dev/nvme0n1p3`.
  - Secure swap partition with random encryption key or include swap inside the encrypted LVM volume.

---

## 2. Windows 11 & Linux Workstation Hardening

### Windows 11 Enterprise Hardening:
- **Enable Core Isolation & Memory Integrity (HVCI)**: Uses hardware virtualization to isolate critical OS processes from kernel malware.
- **PowerShell Attack Surface Reduction (ASR)**:
  Enable Defender ASR rules via PowerShell:
  ```powershell
  # Block executable content from email client and webmail
  Add-MpPreference -AttackSurfaceReductionRules_Ids BE9BA2D9-53EA-4CDC-84E5-9B1EEEE46550 -AttackSurfaceReductionRules_Actions Enabled

  # Block credential stealing from the Windows local security authority subsystem (lsass.exe)
  Add-MpPreference -AttackSurfaceReductionRules_Ids 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2 -AttackSurfaceReductionRules_Actions Enabled

  # Block process creations originating from PSExec and WMI commands
  Add-MpPreference -AttackSurfaceReductionRules_Ids d1e49aac-8f56-4280-b9ba-993a6d77406c -AttackSurfaceReductionRules_Actions Enabled
  ```
- **Disable USB Mass Storage Execution (Group Policy / Registry)**:
  Prevent malware introduction via unauthorized USB drives.

### Linux Desktop Hardening:
- Restrict `ptrace` scope: `echo 1 > /proc/sys/kernel/yama/ptrace_scope` (prevents processes from inspecting memory of other user processes).
- Use firejail / Flatpak sandboxing for untrusted graphical applications.

---

## 3. Public Wi-Fi, Travel Security & Network Privacy

When connecting to untrusted networks (hotels, airports, cafes):
1. **Always-On VPN with Kill-Switch**:
   - The operating system firewall must strictly drop all outbound non-VPN traffic.
   - If the VPN connection drops, no network packets may leak in cleartext.
   - **WireGuard Kill-Switch Implementation (Windows / Linux)**:
     Set `AllowedIPs = 0.0.0.0/0, ::/0` with `Table = auto` and firewall rules blocking native gateway traffic except the VPN endpoint IP.
2. **Preventing WebRTC IP Leaks**:
   - WebRTC can reveal local and public IP addresses even behind a VPN/proxy.
   - Disable WebRTC in browser configuration (`about:config` in Firefox -> `media.peerconnection.enabled = false`).
3. **Encrypted DNS**:
   - Enforce DNS-over-HTTPS (DoH) via Quad9 (`9.9.9.9` - blocks malicious domains) or Cloudflare (`1.1.1.2` - blocks malware).
4. **MAC Address Randomization**:
   - Enable per-network randomized MAC addresses on Windows and Android to prevent physical tracking across Wi-Fi hotspots.

---

## 4. Android Mobile Security Architecture

As an Android developer and administrator, maintain rigorous device and application hygiene:

### A. APK Reverse Engineering & Security Audit:
- **Decompilation & Analysis**:
  - `jadx-gui <target.apk>`: Decompile DEX bytecode into readable Java source code to inspect embedded API keys, hardcoded endpoints, and cryptographic implementations.
  - `apktool d <target.apk>`: Extract raw `AndroidManifest.xml`, resources, and smali code.
- **Signature Scheme Verification**:
  Ensure APKs are signed with modern v2/v3/v4 signing schemes via `apksigner verify --verbose <target.apk>`.
- **Runtime Permission Auditing**:
  - Scrutinize dangerous permissions: `READ_PHONE_STATE`, `READ_CALL_LOG`, `PROCESS_OUTGOING_CALLS`, `SYSTEM_ALERT_WINDOW` (overlay attacks), `BIND_ACCESSIBILITY_SERVICE` (banking trojans and keyloggers).

### B. Defense Against Spyware & RATs (Remote Access Trojans):
- **Accessibility Service Auditing**:
  - Regularly verify `Settings -> Accessibility`. Legitimate apps rarely require accessibility services unless providing assistive technologies. Banking trojans abuse accessibility to intercept 2FA codes and perform unauthorized transactions.
- **USB Debugging (ADB) Hygiene**:
  - **Disable USB Debugging** immediately after development sessions. Leaving ADB active allows anyone with physical access to bypass screen lock and extract data.
  - Revoke all authorized debugging computers periodically (`Settings -> Developer options -> Revoke USB debugging authorizations`).
- **Targeted Spyware Indicators (Pegasus / Predator)**:
  - Sudden battery drain, device overheating while idle, unexpected mobile data spikes in background, unexplained crashes of `netd` or system services.
  - Use the Mobile Verification Toolkit (MVT) to analyze Android system dumps and backup files for known IoCs.

### C. SIM Swap Defense & Authentication Hardening:
- **SIM Card PIN**:
  - Always enable a strong PIN on the physical SIM or eSIM (`Settings -> Security -> SIM card lock`).
  - Prevents an attacker from placing your stolen SIM card into another phone to receive SMS 2FA codes.
- **Eliminate SMS 2FA**:
  - Migrate all critical accounts (banking, GitHub, Google, server hosting) from SMS verification to hardware security keys (**FIDO2 / YubiKey**) or authenticator apps (TOTP).
- **Android Keystore & BiometricPrompt**:
  - In custom Android apps, always store cryptographic secrets inside the hardware-backed **Android Keystore** (`KeyGenParameterSpec.Builder(..., KeyProperties.PURPOSE_ENCRYPT | KeyProperties.PURPOSE_DECRYPT).setUserAuthenticationRequired(true)`).
