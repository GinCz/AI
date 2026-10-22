---
name: devops-cloud-engineering
description: >-
  Expert workflows for modern DevOps, CI/CD pipelines (GitHub Actions, runners), Infrastructure as Code (Terraform, Ansible), containerization (Docker, Compose, rootless), cloud platforms (Oracle OCI, NetCup, AWS), monitoring (Prometheus, Grafana, Loki), and Linux performance kernel tuning.
---
# DevOps, Cloud Infrastructure & Automation Engineering

A comprehensive operational guide for architecting, deploying, automating, and maintaining cloud and on-premise infrastructure.

---

## 1. Continuous Integration & Deployment (CI/CD)

### GitHub Actions Hardened Production Pipeline:
```yaml
name: Production Hardened CI/CD
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

# Principle of least privilege for GITHUB_TOKEN
permissions:
  contents: read
  packages: write
  id-token: write # Required for OIDC cloud authentication
  security-events: write

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  audit-and-build:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - name: Checkout Code
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # Pin to exact commit SHA v4.2.2

      - name: Security Scan (SAST & Vulnerabilities)
        uses: aquasecurity/trivy-action@18f2510ee396bbf400402947b394f2dd8c87dbb0
        with:
          scan-type: 'fs'
          ignore-unfixed: true
          severity: 'CRITICAL,HIGH'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Set up QEMU & Docker Buildx
        uses: docker/setup-qemu-action@49b3bc8e6bdd4480e8226f5bf2164930cc65ee1e
      - uses: docker/setup-buildx-action@c47758b77c9736f4b2ef4073d4d51994fabfe349

      - name: Build Multi-Arch Container Image
        uses: docker/build-push-action@4f58ea79222b3b9dc2c8bbdd6debcef730109a75
        with:
          context: .
          platforms: linux/amd64,linux/arm64
          push: false
          tags: app:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

### Self-Hosted Runners Security & Isolation:
- Use ephemeral runners (e.g. GitHub Actions Runner Controller on Kubernetes) destroyed immediately after a single job execution.
- Strictly isolate runner networks using dedicated VLANs/Security Groups. Runners must never possess direct write access to production database subnets.
- Use OpenID Connect (OIDC) token exchange with AWS IAM / OCI / GCP to acquire short-lived STS tokens instead of storing long-lived credentials in GitHub Secrets.

---

## 2. Infrastructure as Code (IaC) & Configuration Management

### Terraform / OpenTofu Best Practices:
- **Remote State**: S3-compatible backend (e.g. OCI Object Storage, AWS S3) with state locking (DynamoDB or native object locking).
- **Module Architecture**: Reusable modules for VPC/VCN, security lists, compute instances, DNS records.
- **Drift Detection**: Automated scheduled runs to detect unauthorized out-of-band infrastructure modifications.
- **Pre-commit Checks**: Run `tflint`, `tfsec`, and `terraform fmt -check` in CI to prevent insecure infrastructure commits.

### Ansible Playbooks & Idempotency:
- Structure: Roles (`tasks`, `handlers`, `templates`, `vars`, `defaults`).
- **Idempotency Rule**: Playbooks must produce the exact same system state whether run once or 50 times (`changed_when` directives for custom shell commands).
- **Security**: Ansible Vault (`ansible-vault encrypt_string`) for secret storage in git repositories.

---

## 3. Containerization (Docker, Rootless & Kubernetes Hardening)

### Production Distroless Dockerfile Standard:
```dockerfile
# Multi-stage build pattern
FROM golang:1.23-bookworm AS builder
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o /bin/app ./cmd/server

# Final minimal runtime container (Google Distroless non-root)
FROM gcr.io/distroless/static-debian12:nonroot
WORKDIR /app
COPY --from=builder /bin/app /app/server
USER nonroot:nonroot
EXPOSE 8080
ENTRYPOINT ["/app/server"]
```

### Hardened Production Docker Compose (`compose.yaml`):
```yaml
services:
  app:
    image: ghcr.io/gincz/app:v2.1.0
    restart: unless-stopped
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    user: "10001:10001"
    tmpfs:
      - /tmp:rw,noexec,nosuid,size=64m
    environment:
      - NODE_ENV=production
    ports:
      - "127.0.0.1:8080:8080" # Bind to loopback only, never 0.0.0.0
    healthcheck:
      test: ["CMD", "/app/server", "-healthcheck"]
      interval: 10s
      timeout: 3s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 1024M
        reservations:
          memory: 256M
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
        max-file: "5"
```

### Kubernetes Pod Security Standards (Restricted Profile):
- Disallow privileged containers (`privileged: false`).
- Enforce read-only root filesystems (`readOnlyRootFilesystem: true`).
- Restrict Linux capabilities to none (`drop: ["ALL"]`).
- Deny root execution (`runAsNonRoot: true`, `runAsUser: 10001`).
- Enforce strict `NetworkPolicy` denying all ingress by default, whitelisting only designated microservice ports.

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
