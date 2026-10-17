# Xray-Core VLESS-Reality Deployment Quick Reference

An operational reference for deploying and validating high-security, censorship-resistant VLESS-Reality inbound configurations.

---

## 1. Key Generation

```bash
# Generate Xray X25519 public and private key pair
xray x25519

# Generate a strong UUID for client authentication
xray uuid
```

---

## 2. Inbound Configuration Snippet (`config.json`)

```json
{
  "inbounds": [
    {
      "port": 443,
      "protocol": "vless",
      "settings": {
        "clients": [
          {
            "id": "<CLIENT_UUID>",
            "flow": "xtls-rprx-vision"
          }
        ],
        "decryption": "none"
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality",
        "realitySettings": {
          "show": false,
          "dest": "gateway.icloud.com:443",
          "xver": 0,
          "serverNames": [
            "gateway.icloud.com"
          ],
          "privateKey": "<SERVER_PRIVATE_KEY>",
          "shortIds": [
            "<HEX_SHORT_ID>"
          ]
        }
      },
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls", "quic"]
      }
    }
  ]
}
```

---

## 3. Operational Verification

```bash
# Verify configuration syntax
xray run -test -conf /usr/local/etc/xray/config.json

# Restart Xray service
systemctl restart xray

# Check for active listening socket on port 443
ss -tulpn | grep 443

# Validate active probe redirection using curl from an external machine
curl -I -k https://<SERVER_IP>
# Expected result: Returns the HTTP headers of the camouflage target (e.g. gateway.icloud.com)
```
