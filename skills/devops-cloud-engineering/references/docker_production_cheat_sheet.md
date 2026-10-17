# Production Docker & Compose Reference Cheat Sheet

Quick operational commands for managing containers, resource audits, and volume backups.

---

## 1. Container Diagnostics & Resource Auditing

```bash
# Live resource metrics (CPU, Memory, Net I/O, Block I/O) sorted by memory usage
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}" | sort -k 3 -h

# Inspect container healthcheck status and last log output
docker inspect --format='{{json .State.Health}}' <container_name> | jq .

# Check top processes running inside a container
docker top <container_name> aux

# Inspect container restart count and exit code
docker inspect --format='ExitCode: {{.State.ExitCode}} | Restarts: {{.RestartCount}} | Error: {{.State.Error}}' <container_name>
```

---

## 2. Safe Docker Cleanup & Pruning

```bash
# Remove stopped containers older than 24h
docker container prune --filter "until=24h" -f

# Remove dangling images (untagged)
docker image prune -f

# Safe system prune (excluding named volumes to protect persistent data)
docker system prune -a --volumes=false -f
```

---

## 3. Atomic Volume Backup & Restore

```bash
# Backup a named volume to a compressed tarball
docker run --rm -v <volume_name>:/volume -v $(pwd):/backup alpine \
  tar -czf /backup/<volume_name>_backup_$(date +%Y%m%d).tar.gz -C /volume .

# Restore a volume from tarball
docker run --rm -v <volume_name>:/volume -v $(pwd):/backup alpine \
  tar -xzf /backup/<backup_file>.tar.gz -C /volume
```
