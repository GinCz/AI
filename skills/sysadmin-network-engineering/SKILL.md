---
name: sysadmin-network-engineering
description: >-
  Advanced system administration for Linux & Windows Server, computer networking (routing, DNS, reverse proxies), VPN tunneling & protocol obfuscation (Xray, 3X-UI, Reality, WireGuard), 3-2-1 backup strategies (Borg, Rclone), and storage management.
---
# Senior System Administration & Network Engineering

A master operational manual for systems administration across Linux and Windows Server environments, enterprise network routing, modern obfuscated VPN architectures, and disaster recovery.

---

## 1. Dual-Stack System Administration (Linux & Windows)

### Enterprise Linux (Debian, Ubuntu, AlmaLinux):
- **Service Lifecycle Management**: `systemd` units, override drops (`/etc/systemd/system/<unit>.d/override.conf`), sandboxing directives (`ProtectSystem=strict`, `PrivateTmp=yes`, `NoNewPrivileges=true`).
- **Resource Limits**: PAM limits (`/etc/security/limits.conf`), `cgroups v2` resource budgeting.
- **Package Management**: Automated security patching via `unattended-upgrades` with blacklisting of kernel reboot packages on production nodes.

### Windows Server & Workstation Administration:
- **PowerShell 7+ Automation**: Script blocks, advanced parameters, pipeline chaining, structured error handling with `$ErrorActionPreference = 'Stop'`.
- **Windows Services & Scheduled Tasks**: Automated creation, service account delegation (`gMSA` - Group Managed Service Accounts), non-interactive background scheduling.
- **Sysinternals Diagnostics**:
  - `Process Explorer` (identifying process handles, DLL injection, CPU spikes).
  - `Process Monitor` (ProcMon - real-time file system, registry, and network activity tracing).
  - `Autoruns` (comprehensive audit of startup hooks, WMI persistence, scheduled tasks).

---

## 2. Enterprise Network Architecture & Routing

### Routing & Subnetting:
- **Linux Network Stack**: `iproute2` suite (`ip addr`, `ip route`, `ip rule`), policy-based routing (PBR), multiple routing tables (`/etc/iproute2/rt_tables`), network namespaces (`ip netns`).
- **Windows Network Stack**: `Get-NetIPAddress`, `Get-NetRoute`, `New-NetRoute`, `Test-NetConnection`.
- **MTU & MSS Clamping**: Preventing packet fragmentation in VPN tunnels:
  ```bash
  # Clamping TCP MSS to PMTU in iptables
  iptables -t mangle -A FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
  ```

### DNS Infrastructure & Split-Horizon DNS:
- **DNS Resolution**: Unbound, CoreDNS, systemd-resolved, and `dnsmasq`.
- **Encrypted DNS**: DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) preventing ISP spoofing and inspection.
- **Split-Horizon Architecture**: Internal queries resolve to private IPs (`10.0.0.0/8`, `192.168.0.0/16`), while external public queries resolve to WAN IPs.

---

## 3. Reverse Proxies, Load Balancing & SSL/TLS Automation

### Nginx High-Performance Reverse Proxy:
- HTTP/2 & HTTP/3 (QUIC) support, upstream connection pooling (`keepalive 64`), buffer tuning.
- **Automated SSL/TLS via Certbot / ACME**:
  ```bash
  # Issue wildcard certificate via Cloudflare DNS plugin
  certbot certonly --dns-cloudflare --dns-cloudflare-credentials ~/.secrets/cloudflare.ini \
    -d example.com -d "*.example.com" --agree-tos -m admin@example.com --non-interactive
  ```

### Modern Reverse Proxies (Traefik & Caddy):
- **Caddy**: Automatic zero-config TLS via Let's Encrypt / ZeroSSL with reverse proxying and on-demand certificates.
- **Traefik**: Dynamic configuration discovery via Docker labels.

---

## 4. Advanced VPN, Protocol Obfuscation & Tunneling

Operational management of secure tunnels capable of bypassing deep packet inspection (DPI) and active network probing:

### Modern Obfuscation (Xray-Core, 3X-UI & Reality Protocol):
- **VLESS with Reality**:
  - Eliminates the need for a real domain certificate on the server.
  - **SNI Camouflage (Stealth)**: Borrows the TLS certificate and SNI of a legitimate third-party website (e.g. `gateway.icloud.com`, `dl.google.com`, `microsoft.com`).
  - Active probing resistance: When an unauthorized scanner connects without the client private key, the server transparently proxies the connection to the camouflage target.
- **Management via 3X-UI**:
  - Inbound management (VLESS, VMess, Trojan, Shadowsocks).
  - Multi-user bandwidth accounting and automatic credential expiry.

### WireGuard High-Speed Kernel Mesh:
- Modern Cryptography: Curve25519, ChaCha20, Poly1305, BLAKE2s.
- Instant connection handover for roaming mobile clients.
- Configuration template:
  ```ini
  [Interface]
  PrivateKey = <SERVER_PRIVATE_KEY>
  Address = 10.100.0.1/24
  ListenPort = 51820
  PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
  PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

  [Peer]
  PublicKey = <CLIENT_PUBLIC_KEY>
  AllowedIPs = 10.100.0.2/32
  ```

### SSH Advanced Tunneling:
- **Local Port Forward**: `ssh -L 8080:127.0.0.1:80 user@remote-server` (Access remote service locally).
- **Remote / Reverse Tunnel**: `ssh -R 9000:127.0.0.1:3000 user@remote-server` (Expose local port to public internet).
- **Dynamic SOCKS5 Proxy**: `ssh -D 1080 -q -C -N user@remote-server` (Route all local browser traffic through remote host).

---

## 5. Storage Architecture, Backups & Disaster Recovery

### The 3-2-1-1-0 Backup Architecture:
- **3** copies of critical data.
- **2** different storage media types (Local SSD/NVMe + NAS or Cloud).
- **1** copy stored offsite (geographically separated remote datacenter).
- **1** copy offline / immutable / air-gapped (WORM or cold storage with Object Lock).
- **0** errors on backup recovery verification.

### Enterprise Backup Tooling:
- **BorgBackup**:
  - Deduplicated, authenticated, and encrypted client-side backups.
  - Efficient pruning (`borg prune --keep-daily=7 --keep-weekly=4 --keep-monthly=12`).
- **Rclone**:
  - Syncing encrypted directory trees to 40+ cloud backends (Mega, S3, OCI, Google Drive, SFTP, WebDAV).
- **Automated Recovery Testing**: A backup that hasn't been tested for restoration is legally and operationally deemed nonexistent. Automated weekly restoration tests into an isolated test container.
