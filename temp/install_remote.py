import urllib.request
import json
import sys

def install_on_host(target_host):
    print(f"=== Installing Ultarix-Monitor on {target_host} ===")
    
    with open("/tmp/1_Client_Install.cmd", "r", encoding="utf-8") as f:
        full_content = f.read()

    ps_start = full_content.find("# ==============================================================================\n# ULTARIX s.r.o. - Client Activity Monitor Agent")
    if ps_start == -1:
        ps_start = full_content.find("# ==============================================================================\r\n# ULTARIX s.r.o. - Client Activity Monitor Agent")
    
    installer_code = full_content[ps_start:]
    
    remote_ps = f"""
$ErrorActionPreference = 'SilentlyContinue'
$ProgressPreference = 'SilentlyContinue'
{installer_code}
Write-Output "INSTALLED_SUCCESSFULLY: $env:COMPUTERNAME"
"""
    
    req = urllib.request.Request(
        "http://127.0.0.1:9876/exec",
        data=remote_ps.encode("utf-8"),
        headers={"Token": "GinCz-Remote-2026", "X-Target": target_host}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            out = resp.read().decode("utf-8", errors="replace")
            print(f"Result from {target_host}:\n{out}")
            return True
    except Exception as e:
        print(f"Error on {target_host}: {e}")
        return False

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "u-09"
    install_on_host(target)
