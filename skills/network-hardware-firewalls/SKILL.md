---
name: network-hardware-firewalls
description: >-
  Enterprise network engineering, routing and switching for Cisco (IOS-XE, ASA, Firepower), Ubiquiti UniFi (UDM, switches, VLAN isolation, traffic rules), TP-Link Omada SDN, physical/virtual firewalls (FortiGate, pfSense/OPNsense, MikroTik RouterOS v7), Linux nftables/iptables, and Windows Advanced Firewall.
---
# Enterprise Network Hardware, Routing & Firewall Engineering

A comprehensive operational guide for designing, deploying, hardening, and troubleshooting enterprise and branch network infrastructure across physical appliances, SDN ecosystems, next-generation firewalls, and host-level packet filters.

---

## 1. Cisco Enterprise Routing, Switching & Edge Security

### Core IOS-XE Switching & VLAN Segmentation:
```ios
! Configure VLANs with standard naming and security isolation
vlan 10
 name CORPORATE_DATA
vlan 20
 name MANAGEMENT_INFRA
vlan 30
 name IOT_ISOLATED
vlan 99
 name NATIVE_UNUSED
exit

! Trunk Port Configuration (802.1Q) to Upstream Firewall / Core Switch
interface GigabitEthernet0/0/1
 description TRUNK-TO-FIREWALL
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30
 switchport nonegotiate
 no shutdown
exit

! Hardened Access Port with Port Security
interface GigabitEthernet0/0/2
 description WORKSTATION-SECURE
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security mac-address sticky
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit
```

### Layer 2 Infrastructure Protection (DHCP Snooping & DAI):
```ios
! Prevent rogue DHCP servers and ARP spoofing
ip dhcp snooping
ip dhcp snooping vlan 10,20,30
no ip dhcp snooping information option

! Set uplink trunk as trusted DHCP port
interface GigabitEthernet0/0/1
 ip dhcp snooping trust
 ip arp inspection trust
exit

! Enable Dynamic ARP Inspection (DAI)
ip arp inspection vlan 10,20,30
ip arp inspection validate src-mac dst-mac ip
```

### Cisco IOS-XE Routing & Access Control Lists (ACLs):
```ios
! Standard Named Extended Access Control List
ip access-list extended BLOCK_IOT_TO_LAN
 remark Allow established return traffic
 permit tcp 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 established
 remark Allow DNS to local resolver only
 permit udp 192.168.30.0 0.0.0.255 host 192.168.10.5 eq 53
 remark Block all other cross-VLAN traffic
 deny ip 192.168.30.0 0.0.0.255 192.168.0.0 0.0.255.255
 remark Allow IoT outbound to WAN
 permit ip 192.168.30.0 0.0.0.255 any
exit

! IPsec Site-to-Site Tunnel Interface (VTI) on IOS-XE
crypto ikev2 proposal IKEV2-AES-GCM
 encryption aes-gcm-256
 prf sha384
 group 19 20
exit

crypto ikev2 policy IKEV2-POLICY
 proposal IKEV2-AES-GCM
exit

crypto ikev2 profile IKEV2-PROFILE
 match identity remote address <REMOTE_PEER_IP> 255.255.255.255
 identity local address <LOCAL_PUBLIC_IP>
 authentication remote pre-share key <PRE_SHARED_KEY>
 authentication local pre-share key <PRE_SHARED_KEY>
 lifetime 86400
exit

crypto ipsec transform-set TS-AES-GCM esp-gcm 256
 mode tunnel
exit

crypto ipsec profile IPSEC-PROFILE
 set transform-set TS-AES-GCM
 set ikev2-profile IKEV2-PROFILE
exit

interface Tunnel100
 description SECURE-VTI-TUNNEL-BRANCH
 ip address 10.255.255.1 255.255.255.252
 tunnel source GigabitEthernet0/0/0
 tunnel mode ipsec ipv4
 tunnel destination <REMOTE_PEER_IP>
 tunnel protection ipsec profile IPSEC-PROFILE
 ip mtu 1400
 ip tcp adjust-mss 1360
exit
```

---

## 2. Ubiquiti UniFi Ecosystem & Enterprise Gateway Architecture

### Network Architecture & Architecture Matrix:
- **Topology Hierarchy**: UniFi Dream Machine (UDM Pro / SE) -> USW Enterprise/Pro Switch (10G SFP+ DAC / Optical trunk) -> U6/U7 Enterprise Access Points.
- **VLAN Isolation Model**:
  - `Default (VLAN 1)`: UniFi management plane only (Gateways, Switches, APs). Client access strictly prohibited.
  - `VLAN 10 (Corporate)`: Trusted corporate laptops and workstations. Full outbound WAN, managed inter-VLAN access.
  - `VLAN 20 (Servers/DMZ)`: Internal services, reverse proxies, NAS. Isolated with selective port forwarding.
  - `VLAN 30 (IoT)`: Smart devices, cameras, appliances. Total isolation from RFC1918 subnets, WAN access only.
  - `VLAN 40 (Guest)`: Isolated via Client Device Isolation (L2 isolation), captive portal or voucher system, bandwidth throttling.

### UniFi Firewall Rules Architecture (Rule Order & Execution):
UniFi processes firewall rules in strict order: **WAN / LAN / Guest** -> **In / Out / Local**.
1. **Rule 2000 (Drop Invalid State)**:
   - Type: `LAN In` | Action: `Drop` | Protocol: `All` | State: `Invalid`
2. **Rule 2001 (Allow Established & Related)**:
   - Type: `LAN In` | Action: `Accept` | Protocol: `All` | State: `Established`, `Related`
3. **Rule 2002 (Allow Inter-VLAN DNS/NTP to Core Server)**:
   - Type: `LAN In` | Action: `Accept` | Protocol: `UDP` | Source: `Any` | Destination: `Port Group: DNS_NTP (53, 123)` on Core Server IP.
4. **Rule 2003 (Block IoT to Private Subnets RFC1918)**:
   - Type: `LAN In` | Action: `Drop` | Source: `Network: IoT` | Destination: `Port/IP Group: RFC1918_ALL (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)`
5. **Rule 2004 (Block Gateway Web/SSH Access from Untrusted VLANs)**:
   - Type: `LAN Local` | Action: `Drop` | Source: `Networks: IoT, Guest` | Destination: `Port Group: MGMT_PORTS (22, 443, 80, 8443)`

### UniFi Edge Features & Advanced Services:
- **Deep Packet Inspection (DPI) & Traffic Rules**: Enforce application blocking (P2P, malicious domains, specific cloud apps) at wire speed.
- **Teleport & WireGuard VPN**: Native zero-configuration remote access using WireGuard protocol with ChaCha20-Poly1305 encryption.
- **mDNS Repeater / Reflector**: Enable selectively on IoT VLAN to allow Chromecast/AirPlay discovery from Corporate VLAN without opening full L2/L3 access.

---

## 3. TP-Link Omada SDN Infrastructure

### Omada Architecture & Deployment:
- **Centralized Controller**: Hardware (OC200, OC300), Software (Docker / Linux VM), or Omada Cloud-Based Controller.
- **Hardware Integration**: Multi-Gigabit VPN Gateways (ER605, ER7206, ER8411) + JetStream L2+/L3 Managed Switches + Omada EAP600/700 APs.

### Multi-WAN Load Balancing & Failover:
1. **Link Backup / Failover**: Primary WAN (High-speed Fiber) + Secondary WAN (Backup 5G/LTE or VDSL). Failover detection interval set to 3 seconds with DNS probe targets (`1.1.1.1`, `8.8.8.8`).
2. **Policy Routing**: Force critical server and administrative traffic through static IP on WAN1; offload streaming and general guest traffic to WAN2.

### Omada ACL Hierarchy & Rule Execution:
- **Gateway ACLs**: Apply at the router level for WAN and inter-network routing decisions.
- **Switch ACLs**: Hardware-enforced on JetStream switch ASICs. Eliminates inter-port communication at Layer 2 wire speed before packets even reach the gateway.
- **EAP ACLs**: Applied directly at wireless APs to isolate Wi-Fi clients from wired infrastructure.
- **Omada Isolation Matrix**:
  - Create IP Group: `RFC1918_Subnets` (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`).
  - Rule `LAN_Isolate_IoT`: Policy: `Deny` | Source: `Subnet_IoT` | Destination: `RFC1918_Subnets`.
  - Direction: Bidirectional isolation with allow established state.

---

## 4. Next-Generation Physical & Virtual Firewalls

### Fortinet FortiGate (FortiOS):
```fortios
# Configure Security Zones and VLAN Interface
config system interface
    edit "VLAN_CORP"
        set vdom "root"
        set ip 192.168.10.1 255.255.255.0
        set allowaccess ping
        set interface "port1"
        set vlanid 10
    next
end

# Hardened Firewall Policy with UTM Inspection
config firewall policy
    edit 10
        set name "CORP_TO_WAN_SECURE"
        set srcintf "VLAN_CORP"
        set dstintf "wan1"
        set action accept
        set srcaddr "all"
        set dstaddr "all"
        set schedule "always"
        set service "ALL"
        set utm-status enable
        set ssl-ssh-profile "deep-inspection"
        set av-profile "default"
        set ips-sensor "high_security"
        set application-list "default"
        set nat enable
    next
end
```

### pfSense & OPNsense (Packet Filter - pf):
- **Aliases**: Centralize IP, port, and URL table aliases for dynamic firewall rules (e.g., `Spamhaus_DROP`, `Emerging_Threats`).
- **pf Rules Processing**: First match wins for rules with `quick` keyword.
- **High Availability (CARP & XMLRPC Sync)**:
  - Configure redundant master/backup nodes sharing Virtual IPs via CARP (Common Address Redundancy Protocol).
  - PFSYNC synchronizes state tables in real time over a dedicated crossover link. Node failover causes zero dropped TCP connections.
- **Intrusion Detection (Suricata / Snort)**:
  - Run in Inline IPS Mode using Netmap driver.
  - Automatically drop malicious signatures (ET Open, Snort Community, Abuse.ch SSLBL).

### MikroTik RouterOS v7:
```routeros
# FastTrack & State Tracking Hardening
/ip firewall filter
add chain=input action=accept connection-state=established,related,untracked comment="Accept established, related"
add chain=input action=drop connection-state=invalid comment="Drop invalid"
add chain=input action=accept protocol=icmp comment="Allow ICMP"
add chain=input action=accept protocol=udp dst-port=13231 comment="Allow WireGuard"
add chain=input action=drop in-interface-list=WAN comment="Drop all other WAN traffic"

add chain=forward action=fasttrack-connection connection-state=established,related hw-offload=yes comment="FastTrack Hardware Offload"
add chain=forward action=accept connection-state=established,related,untracked
add chain=forward action=drop connection-state=invalid

# Raw Pre-routing Table for SYN-Flood and Port Scan Mitigation
/ip firewall raw
add chain=prerouting action=drop tcp-flags=fin,syn,rst,psh,ack,urg,!fin,!syn,!rst,!psh,!ack,!urg comment="Drop NULL packets"
add chain=prerouting action=drop tcp-flags=fin,syn,!rst,!psh,!ack,!urg comment="Drop SYN-FIN packets"
add chain=prerouting action=drop in-interface-list=WAN src-address-list=black_list comment="Drop blacklisted IPs"
```

---

## 5. Modern Host-Level Firewalls (Linux & Windows)

### Linux `nftables` Enterprise Ruleset (`/etc/nftables.conf`):
```nftables
#!/usr/sbin/nft -f
flush ruleset

table inet filter {
    # Dynamic set for rate limiting and brute-force banning
    set ban_list {
        type ipv4_addr
        flags timeout
    }

    chain input {
        type filter hook input priority filter; policy drop;

        # Connection state tracking
        ct state established,related accept
        ct state invalid drop

        # Loopback interface
        iif "lo" accept

        # Rate-limited ICMP
        ip protocol icmp icmp type { echo-request, echo-reply } limit rate 5/second accept
        ip6 nexthdr ipv6-icmp accept

        # Drop and ban SSH brute-force attackers (>5 attempts in 1 minute -> ban 1 hour)
        tcp dport 22 ct state new,untracked meter ssh_meter { ip saddr limit rate over 5/minute } add @ban_list { ip saddr timeout 1h } drop
        ip saddr @ban_list drop

        # Hardened management access
        tcp dport 22 accept
        tcp dport { 80, 443 } accept
    }

    chain forward {
        type filter hook forward priority filter; policy drop;
    }

    chain output {
        type filter hook output priority filter; policy accept;
    }
}
```

### Windows Advanced Firewall Hardening via PowerShell:
```powershell
# Enforce Outbound and Inbound Drop by Default on all profiles
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
Set-NetFirewallProfile -Profile Domain,Public,Private -DefaultInboundAction Block
Set-NetFirewallProfile -Profile Public -DefaultOutboundAction Block

# Enable logging of dropped packets
Set-NetFirewallProfile -Profile Domain,Public,Private -LogFileName "%SystemRoot%\system32\LogFiles\Firewall\pfirewall.log" -LogMaxSizeKilobytes 32768 -LogDroppedConnections True

# Allow Outbound DNS, HTTP, HTTPS for system updates only
New-NetFirewallRule -DisplayName "Outbound-Core-DNS" -Direction Outbound -Action Allow -Protocol UDP -RemotePort 53
New-NetFirewallRule -DisplayName "Outbound-Core-HTTP-HTTPS" -Direction Outbound -Action Allow -Protocol TCP -RemotePort 80,443

# Allow Inbound Hardened Management from Specific Administrative Subnet
New-NetFirewallRule -DisplayName "MGMT-Inbound-WinRM-Hardened" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 5986 -RemoteAddress 192.168.20.0/24
