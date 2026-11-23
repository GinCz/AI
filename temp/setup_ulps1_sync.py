import urllib.request

with open("/tmp/Sync_To_Cloud.ps1", "r", encoding="utf-8") as f:
    sync_code = f.read()

cmd = f"""
$dir = "C:\\UTIL\\UltarixMonitor"
if (-not (Test-Path $dir)) {{ New-Item -ItemType Directory -Path $dir -Force | Out-Null }}
$syncFile = "$dir\\Sync_To_Cloud.ps1"
@\"
{sync_code}
\"@ | Set-Content -Path $syncFile -Encoding utf8 -Force

schtasks /delete /tn "Ultarix-Cloud-Sync" /f 2>$null | Out-Null
$taskCmd = 'powershell.exe -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "' + $syncFile + '"'
schtasks /create /tn "Ultarix-Cloud-Sync" /tr $taskCmd /sc ONSTART /rl HIGHEST /f | Out-Null
schtasks /run /tn "Ultarix-Cloud-Sync" | Out-Null

Write-Output "ULPS1_SYNC_INSTALLED_AND_STARTED"
"""

req = urllib.request.Request(
    "http://127.0.0.1:9876/exec",
    data=cmd.strip().encode("utf-8"),
    headers={"Token": "GinCz-Remote-2026", "X-Target": "ulps1"}
)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        print(resp.read().decode())
except Exception as e:
    print(f"Err: {e}")
