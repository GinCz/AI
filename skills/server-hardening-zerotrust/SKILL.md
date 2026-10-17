---
name: server-hardening-zerotrust
description: >-
  Enterprise infrastructure hardening for Linux & Windows, SSH ed25519/2FA, UFW/Nftables firewalls, Fail2ban, CrowdSec, Web Application Firewalls (WAF), Zero Trust architecture (mTLS, bastion hosts), and PCI DSS v4.0 compliance standards.
---
# Server Hardening, Security Baselines & Zero Trust Architecture

A comprehensive operational security framework for hardening servers, endpoints, cloud nodes, and network perimeters against advanced persistent threats (APTs) and automated exploitation.

---

## 1. Linux Server Hardening Baseline (CIS Benchmarks)

### A. SSH Daemon Hardening (`/etc/ssh/sshd_config`):
```ini
# Port and Protocol
Port 22222                          # Move from default port 22
Protocol 2
AddressFamily inet                  # IPv4 only if IPv6 is unused

# Authentication
PermitRootLogin no                  # Never allow direct root login
PasswordAuthentication no           # Pure key-based authentication
PubkeyAuthentication yes
AuthenticationMethods publickey     # Enforce publickey (or publickey,keyboard-interactive for 2FA)
MaxAuthTries 3                      # Disconnect quickly on failed attempts
LoginGraceTime 20                   # Short window to authenticate
PermitEmptyPasswords no
HostbasedAuthentication no
IgnoreRhosts yes

# Cryptographic Primitives (Modern Only)
KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group16-sha512
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com
MACs hmac-sha2-512-etm@openssh.com

# Session Restrictions
X11Forwarding no
AllowTcpForwarding no               # Disable unless explicitly required for tunneling
ClientAliveInterval 300
ClientAliveCountMax 2
```

### B. Firewall & Intrusion Prevention:
- **Nftables / UFW**:
  - Default policy: **DROP** all incoming, **DROP** all forwarded, **ACCEPT** all outgoing.
  - Rate limiting new incoming connections to prevent brute force and port scans.
- **Fail2ban vs. CrowdSec**:
  - **CrowdSec**: Modern collaborative IPS parsing journald/logs, utilizing a global consensus threat intelligence network, and blocking attackers at the firewall/bouncing level.
  - **Fail2ban**: Local jail rules targeting SSH, Nginx auth, and WordPress brute force.

### C. Kernel Self-Protection & Auditing:
- Enforce AppArmor / SELinux in `enforcing` mode.
- System call auditing via `auditd`: Track modifications to `/etc/passwd`, `/etc/shadow`, `/etc/sudoers`, and execution of SUID binaries.
- Restrict kernel pointers and dmesg: `kernel.dmesg_restrict = 1`, `kernel.kptr_restrict = 2`.

---

## 2. Web Application & Reverse Proxy Hardening

### Secure HTTP Response Headers (Nginx / Cloudflare):
```nginx
# Prevent MIME-sniffing
add_header X-Content-Type-Options "nosniff" always;

# Prevent clickjacking
add_header X-Frame-Options "SAMEORIGIN" always;

# Restrict browser capabilities
add_header Permissions-Policy "geolocation=(), camera=(), microphone=(), payment=()" always;

# Strict Content Security Policy (CSP)
add_header Content-Security-Policy "default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self';" always;

# Strict-Transport-Security (HSTS - 2 years + preload)
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

# Referrer Policy
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
```

### Web Application Firewall (WAF) & Rate Limiting:
- Deploy **Cloudflare WAF** or **ModSecurity with OWASP Core Rule Set (CRS)** to block SQL injection (SQLi), Cross-Site Scripting (XSS), Local File Inclusion (LFI), and Remote Code Execution (RCE).
- Nginx connection & request limiting:
  ```nginx
  limit_req_zone $binary_remote_addr zone=req_limit_per_ip:10m rate=10r/s;
  limit_conn_zone $binary_remote_addr zone=conn_limit_per_ip:10m;

  location /api/ {
      limit_req zone=req_limit_per_ip burst=20 nodelay;
      limit_conn conn_limit_per_ip 10;
  }
  ```

---

## 3. Windows Server & Workstation Hardening

### Attack Surface Reduction (ASR) & Credential Protection:
- **Enable Windows Defender Credential Guard**: Isolates LSA secrets (LSASS) in a virtualization-based security (VBS) container, neutralizing Mimikatz Pass-the-Hash attacks.
- **Disable Legacy Protocols via Group Policy or Registry**:
  - Disable **SMBv1** entirely.
  - Disable **LLMNR** (*Link-Local Multicast Name Resolution*) and **NetBIOS over TCP/IP** to prevent Responder/poisoning attacks.
  - Enforce SMB Signing and SMB Encryption.
- **PowerShell Hardening**:
  - Enforce **Constrained Language Mode** for standard users via AppLocker / WDAC.
  - Enable Script Block Logging (Event ID 4104) and Module Logging.
- **BitLocker with TPM + PIN**: Full disk encryption protecting data at rest on laptops and desktops against physical theft or offline recovery attacks.

---

## 4. Zero Trust Architecture (ZTA)

### Core Tenets of Zero Trust (NIST SP 800-207):
1. **Never Trust, Always Verify**: Location within the local network perimeter grants zero trust.
2. **Least Privilege Access**: Access is granted strictly on a per-session, need-to-know basis.
3. **Assume Breach**: Segment networks and operate under the premise that an adversary is already inside.

### Implementation Checklist:
- **Bastion / Jump Hosts**: Production servers must never expose SSH/RDP directly to the public internet. Access exclusively via an authenticated Bastion host or an encrypted WireGuard/Tailscale mesh with multi-factor authentication (MFA).
- **Mutual TLS (mTLS)**: Inter-service communication across microservices or internal APIs requires cryptographic client and server certificates.
- **Ephemeral Secrets & Vault**: Store zero secrets in code, Dockerfiles, or unencrypted text. Inject via HashiCorp Vault, AWS Secrets Manager, or encrypted SOPS repositories.

---

## 5. PCI DSS v4.0 Compliance Standards

For systems processing, transmitting, or storing cardholder or sensitive financial data:
- **Requirement 1 & 2**: Strict firewall network segmentation isolating the Cardholder Data Environment (CDE) from out-of-scope systems.
- **Requirement 3 & 4**: Strong cryptography (AES-256) for data at rest and TLS 1.3 for data in transit; complete prohibition of storing card verification codes (CVV/CVC) after authorization.
- **Requirement 10**: Log all user access to system components; synchronize clocks via secure NTP; retain audit trail history for at least 12 months (with 3 months immediately available).
- **Requirement 11.5**: Deploy **File Integrity Monitoring (FIM)** (e.g. AIDE, OSSEC, Wazuh) to monitor system binaries and critical configuration files against unauthorized modifications.
