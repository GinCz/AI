# Linux Automated Hardening Script (Template)

A production-grade Bash hardening script enforcing SSH isolation, firewall defaults, and kernel protections.

```bash
#!/usr/bin/env bash
# Automated Linux Hardening Baseline Script
set -euo pipefail

echo "[*] Starting Linux Hardening Protocol..."

# 1. Update and install core security utilities
apt-get update && apt-get install -y --no-install-recommends \
    ufw \
    fail2ban \
    auditd \
    apparmor \
    apparmor-utils \
    unattended-upgrades

# 2. Configure UFW Firewall
echo "[*] Configuring UFW Firewall..."
ufw default deny incoming
ufw default allow outgoing
ufw default deny routed
# Allow custom SSH port (e.g. 22222) with rate limiting
ufw limit 22222/tcp comment "SSH Hardened Port"
# Allow HTTP/HTTPS if web server
ufw allow 80/tcp comment "HTTP Web"
ufw allow 443/tcp comment "HTTPS Web"
ufw --force enable

# 3. Secure Shared Memory (/dev/shm)
if ! grep -q "/dev/shm" /etc/fstab; then
    echo "tmpfs /dev/shm tmpfs defaults,noexec,nosuid,nodev 0 0" >> /etc/fstab
    mount -o remount /dev/shm
fi

# 4. Kernel Network Hardening
cat > /etc/sysctl.d/99-security-hardening.conf << 'EOF'
# Disable IP packet forwarding (unless router/gateway)
net.ipv4.ip_forward = 0

# Ignore ICMP Echo broadcast requests (Smurf attack mitigation)
net.ipv4.icmp_echo_ignore_broadcasts = 1

# Ignore bogus ICMP error responses
net.ipv4.icmp_ignore_bogus_error_responses = 1

# Protect against SYN flood attacks (SYN Cookies)
net.ipv4.tcp_syncookies = 1

# Log Martians (unroutable packets)
net.ipv4.conf.all.log_martians = 1
net.ipv4.conf.default.log_martians = 1

# Disable ICMP Redirect acceptance (prevent MitM)
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0

# Disable Source Packet Routing
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0

# Reverse Path Filtering (Spoofing defense)
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1
EOF

sysctl --system

# 5. Enable and start security daemons
systemctl enable --now fail2ban
systemctl enable --now auditd
systemctl enable --now unattended-upgrades

echo "[+] Linux Hardening Protocol Completed Successfully."
```
