---
name: devops-cloud-engineering
description: >-
  Expert workflows for modern DevOps, CI/CD pipelines (GitHub Actions, runners), Infrastructure as Code (Terraform, Ansible), containerization (Docker, Compose, rootless), cloud platforms (Oracle OCI, NetCup, AWS), monitoring (Prometheus, Grafana, Loki), and Linux performance kernel tuning.
---
# DevOps, Cloud Infrastructure & Automation Engineering

A comprehensive operational guide for architecting, deploying, automating, and maintaining cloud and on-premise infrastructure.

---

## 1. Continuous Integration & Deployment (CI/CD)

### GitHub Actions Production Patterns:
- **Pipeline Architecture**: Linting -> Unit Tests -> SAST/Security Scan -> Multi-arch Build -> Container Push -> Deploy via SSH / Webhook.
- **Self-Hosted Runners vs. GitHub Runners**:
  - Secure runner isolation: Use ephemeral runners or dedicated unprivileged service users.
  - Runner environment variables and secrets must be injected via GitHub Secrets / HashiCorp Vault.
- **Workflow Optimization**:
  - Aggressive caching: `actions/cache` for package dependencies (npm, pip, go mod, cargo).
  - Multi-stage concurrency controls (`concurrency: group: ${{ github.ref }}, cancel-in-progress: true`).
  - Strict step timeouts (`timeout-minutes: 15`) to prevent hanging jobs and token/credit burns.

---

## 2. Infrastructure as Code (IaC) & Configuration Management

### Terraform / OpenTofu Best Practices:
- **Remote State**: S3-compatible backend (e.g. OCI Object Storage, AWS S3) with state locking (DynamoDB or native object locking).
- **Module Architecture**: Reusable modules for VPC/VCN, security lists, compute instances, DNS records.
- **Drift Detection**: Automated scheduled runs to detect unauthorized out-of-band infrastructure modifications.

### Ansible Playbooks & Idempotency:
- Structure: Roles (`tasks`, `handlers`, `templates`, `vars`, `defaults`).
- **Idempotency Rule**: Playbooks must produce the exact same system state whether run once or 50 times (`changed_when` directives for custom shell commands).
- **Security**: Ansible Vault (`ansible-vault encrypt_string`) for secret storage in git repositories.

---

## 3. Containerization (Docker, Compose & OCI)

### Production Dockerfile Standards:
1. **Minimal Base Images**: Alpine, Debian-slim, or Google Distroless.
2. **Multi-Stage Builds**: Separate build-time dependencies (compilers, SDKs) from the runtime environment.
3. **Non-Root Execution**: Always declare `USER nonroot` or create dedicated UID/GID inside the container.
4. **Cache Optimization**: Copy package manifests (`package.json`, `go.mod`, `requirements.txt`) before application source code.
5. **Security Scanning**: Scan images with `Trivy` or `Grype` during CI builds.

### Docker Compose Production Patterns:
- Use explicit healthchecks (`test: ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"]`).
- Resource limits per container:
  ```yaml
  deploy:
    resources:
      limits:
        cpus: '1.5'
        memory: 1024M
      reservations:
        memory: 256M
  ```
- Logging drivers with rotation:
  ```yaml
  logging:
    driver: "json-file"
    options:
      max-size: "50m"
      max-file: "5"
  ```
- Automated restarts: `restart: unless-stopped`.

---

## 4. Cloud Infrastructure Management (Oracle OCI, NetCup, AWS)

### Oracle Cloud Infrastructure (OCI):
- **Free Tier Architecture**: Up to 4 ARM Ampere A1 cores and 24 GB RAM (flexible allocation across 1 to 4 VMs).
- **Network Topology**: Virtual Cloud Network (VCN), Internet Gateway, Service Gateway, Security Lists & Network Security Groups (NSGs).
- **OCI CLI Automation**: Scripted provisioning, snapshot management, and lifecycle policies via `oci-cli`.

### NetCup & Hetzner Infrastructure:
- Custom OS deployment via cloud-init and vKVM.
- FastPanel / Docker multi-tenant hosting with automated SSL and isolated PHP-FPM / Node.js pools.

---

## 5. Observability, Telemetry & Alerting

### Modern Observability Stack:
- **Metrics**: Prometheus pulling metrics via `node_exporter`, `cadvisor` (container stats), and application `/metrics`.
- **Dashboards**: Grafana with pre-configured operational dashboards (CPU, RAM, Disk I/O, Network Throughput).
- **Log Aggregation**: Vector / Promtail collecting `systemd journald` and container logs -> shipping to Grafana Loki.
- **Alerting**: Alertmanager triggering instant notifications to Telegram bots / webhooks upon high error rates, low disk space (< 15%), or unreachable nodes.

---

## 6. Linux Kernel & Performance Tuning (`sysctl.conf`)

Optimize Linux servers for high-throughput networking, database workloads, and low latency:

```ini
# /etc/sysctl.d/99-performance-tuning.conf

# File descriptors and memory
fs.file-max = 2097152
vm.swappiness = 10
vm.vfs_cache_pressure = 50

# TCP BBR Congestion Control
net.core.default_qdisc = fq
net.ipv4.tcp_congestion_control = bbr

# TCP Buffer and Window Scaling
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216

# Connection backlog & SYN Queue
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 100000
net.ipv4.tcp_max_syn_backlog = 16384
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_fin_timeout = 15

# Fast Ephemeral Port Allocation
net.ipv4.ip_local_port_range = 10240 65535
```
Apply immediately without reboot: `sysctl --system`.
