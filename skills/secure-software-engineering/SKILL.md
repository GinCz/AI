---
name: secure-software-engineering
description: >-
  DevOps-grade secure software engineering, modern multi-language practices (Windows PowerShell, C#/.NET 8/9, Android Kotlin/Compose, Linux Server Bash/Python 3.12+/Go/Rust), bulletproof defensive programming, zero-injection standards, cryptographic integrity, performance optimization, and clean architecture.
---
# Secure Software Engineering & Bulletproof DevOps Development

An operational handbook for writing ultra-secure, unhackable, high-performance, and maintainable software across Windows, Android, and Linux environments.

---

## 1. Core Architectural Tenets & Secure Coding Principles

1. **Simplicity Over Cleverness (KISS)**: Complex code hides vulnerabilities. Write straightforward, deterministic logic with single-responsibility components.
2. **Fail-Closed by Default**: If an operation fails, error handling must deny access, revoke tokens, roll back transactions, and terminate execution cleanly.
3. **Defense in Depth**: Never rely on a single layer of validation. Validate inputs at the API perimeter, controller boundary, domain logic, and data layer.
4. **Zero-Trust Memory & Secrets**: Overwrite sensitive cryptographic keys and passwords in memory immediately after use (`Array.Clear`, `sodium_memzero`, `memset_s`). Never write secrets to disk or logs.
5. **Strict Input Sanitization & Parameterization**: Never concatenate external strings into shell commands, SQL queries, LDAP lookups, or file paths. Use parameter binding and typed AST validators.

---

## 2. Bulletproof Bash for Linux Production Servers

### The Unbreakable Bash Header:
Every production Bash script must start with strict safety flags, restricted field separators, and comprehensive error trapping:

```bash
#!/usr/bin/env bash
# ==============================================================================
# Script Name: hardened_service_deploy.sh
# Standard: POSIX Hardened Bash (Strict-Mode, Zero-Eval, Safe-Trap)
# ==============================================================================
set -euo pipefail
IFS=$'\n\t'
umask 077

# Trap unexpected errors with line number and command context
trap 'error_exit $? $LINENO' ERR
trap cleanup EXIT INT TERM

cleanup() {
    local exit_code=$?
    # Clean temporary files securely
    if [[ -n "${TEMP_DIR:-}" && -d "${TEMP_DIR:-}" ]]; then
        rm -rf "${TEMP_DIR}"
    fi
    exit "${exit_code}"
}

error_exit() {
    local code="$1"
    local line="$2"
    printf '{"status":"FATAL","line":%d,"exit_code":%d,"timestamp":"%s"}\n' \
        "${line}" "${code}" "$(date -u +'%Y-%m-%dT%H:%M:%SZ')" >&2
    exit "${code}"
}

# Enforce non-root execution unless explicitly required
if [[ "${EUID}" -eq 0 ]]; then
    printf 'Error: Running as root is forbidden for security.\n' >&2
    exit 1
fi
```

### Atomic File Operations & Process Locking:
```bash
# Process singleton locking via flock (prevents race conditions)
LOCK_FILE="/tmp/service_process.lock"
exec 200>"${LOCK_FILE}"
if ! flock -n 200; then
    printf 'Error: Another instance is already running.\n' >&2
    exit 1
fi

# Atomic file update pattern (prevents corrupted state on crash)
TEMP_DIR="$(mktemp -d -t secure_op_XXXXXX)"
target_config="/etc/app/config.json"
temp_output="${TEMP_DIR}/config.tmp"

# Generate new state safely into temp file
cat <<EOF > "${temp_output}"
{"version":"2.0.0","status":"active","updated":"$(date -u +%s)"}
EOF

# Atomically replace target file using rename syscall (mv)
mv -f "${temp_output}" "${target_config}"
chmod 0600 "${target_config}"
```

---

## 3. Hardened Windows PowerShell & C# / .NET 8/9

### Production PowerShell Strict Standard:
```powershell
<#
.SYNOPSIS
    Hardened enterprise task automation template.
.NOTES
    Standards: PowerShell 7+, StrictMode Latest, No-Eval, Typed AST validation.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [ValidatePattern('^[a-zA-Z0-9\._\-]{3,64}$')]
    [string]$TargetIdentifier,

    [Parameter(Mandatory = $false)]
    [ValidateRange(1, 65535)]
    [int]$Port = 443
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

try {
    # Secure credential handling via Windows DPAPI / PSCredential
    $SecureKeyPath = "$PSScriptRoot\secrets\token.enc"
    if (Test-Path -LiteralPath $SecureKeyPath) {
        $Encrypted = Get-Content -LiteralPath $SecureKeyPath -Raw
        $SecretBytes = [System.Security.Cryptography.ProtectedData]::Unprotect(
            [System.Convert]::FromBase64String($Encrypted),
            $null,
            [System.Security.Cryptography.DataProtectionScope]::CurrentUser
        )
        $SecureToken = [System.Text.Encoding]::UTF8.GetString($SecretBytes)
        # Clear secret array immediately
        [System.Array]::Clear($SecretBytes, 0, $SecretBytes.Length)
    }

    # Execute deterministic logic with explicit path escaping
    Write-Output "Processing identifier: $TargetIdentifier on port $Port"
}
catch {
    Write-Error "Execution aborted due to security failure: $($_.Exception.Message)"
    exit 1
}
```

### C# / .NET 8/9 High-Performance, Zero-Allocation & Memory Safety:
- **Memory Optimization via Spans & Memory Pools**:
```csharp
using System;
using System.Buffers;
using System.Security.Cryptography;

public sealed class SecureTokenValidator
{
    // Constant-time comparison to prevent timing attacks
    public static bool VerifyTokenConstantTime(ReadOnlySpan<byte> expected, ReadOnlySpan<byte> actual)
    {
        return CryptographicOperations.FixedTimeEquals(expected, actual);
    }

    // Zero-allocation buffer slicing with ArrayPool
    public static void ProcessDataBuffer(ReadOnlySpan<byte> incomingPayload)
    {
        byte[] rentedBuffer = ArrayPool<byte>.Shared.Rent(incomingPayload.Length);
        try
        {
            Span<byte> workSpan = rentedBuffer.AsSpan(0, incomingPayload.Length);
            incomingPayload.CopyTo(workSpan);
            // Perform high-throughput parsing on workSpan without GC pressure
        }
        finally
        {
            // Always clear sensitive data before returning to shared pool
            Array.Clear(rentedBuffer, 0, incomingPayload.Length);
            ArrayPool<byte>.Shared.Return(rentedBuffer);
        }
    }
}
```

---

## 4. Unhackable Android Engineering (Kotlin + Jetpack)

### 1. Hardware-Backed Android Keystore Integration:
```kotlin
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import java.security.KeyStore
import javax.crypto.Cipher
import javax.crypto.KeyGenerator
import javax.crypto.SecretKey
import javax.crypto.spec.GCMParameterSpec

object SecureKeyStoreManager {
    private const val ANDROID_KEYSTORE = "AndroidKeyStore"
    private const val KEY_ALIAS = "EnterpriseAuthKeyMaster"

    init {
        val keyStore = KeyStore.getInstance(ANDROID_KEYSTORE).apply { load(null) }
        if (!keyStore.containsAlias(KEY_ALIAS)) {
            val keyGenerator = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, ANDROID_KEYSTORE)
            val spec = KeyGenParameterSpec.Builder(
                KEY_ALIAS,
                KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
            )
                .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                .setKeySize(256)
                .setUserAuthenticationRequired(false) // Set to true if biometric auth is required
                .setIsStrongBoxBacked(true) // Enforce hardware security module (StrongBox) if available
                .build()
            keyGenerator.init(spec)
            keyGenerator.generateKey()
        }
    }

    fun encryptPayload(plainText: ByteArray): Pair<ByteArray, ByteArray> {
        val keyStore = KeyStore.getInstance(ANDROID_KEYSTORE).apply { load(null) }
        val secretKey = keyStore.getKey(KEY_ALIAS, null) as SecretKey
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        cipher.init(Cipher.ENCRYPT_MODE, secretKey)
        val iv = cipher.iv
        val encryptedData = cipher.doFinal(plainText)
        return Pair(iv, encryptedData)
    }

    fun decryptPayload(iv: ByteArray, encryptedData: ByteArray): ByteArray {
        val keyStore = KeyStore.getInstance(ANDROID_KEYSTORE).apply { load(null) }
        val secretKey = keyStore.getKey(KEY_ALIAS, null) as SecretKey
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        val spec = GCMParameterSpec(128, iv)
        cipher.init(Cipher.DECRYPT_MODE, secretKey, spec)
        return cipher.doFinal(encryptedData)
    }
}
```

### 2. Android Manifest & Network Security Hardening:
- **Component Protection**: Set all activities, services, receivers, and providers to `android:exported="false"` unless explicitly designed for external intent invocation.
- **Certificate Pinning via `res/xml/network_security_config.xml`**:
```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="false">
        <domain includeSubdomains="true">api.gincz.com</domain>
        <pin-set expiration="2027-12-31">
            <!-- SHA-256 hash of Subject Public Key Info (SPKI) -->
            <pin digest="SHA-256">AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=</pin>
            <!-- Backup pin for disaster recovery -->
            <pin digest="SHA-256">BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=</pin>
        </pin-set>
    </domain-config>
</network-security-config>
```

### 3. Anti-Tampering, Root & Frida Detection:
- Check for test-keys build tags (`Build.TAGS != null && Build.TAGS.contains("test-keys")`).
- Detect suspicious binaries (`/system/app/Superuser.apk`, `/system/xbin/su`, `/system/bin/magisk`).
- Scan `/proc/self/maps` for injected hooking libraries (`frida-agent.so`, `substrate.so`).
- Enforce ProGuard / R8 full obfuscation rules (`minifyEnabled true`, `shrinkResources true`).

---

## 5. Modern High-Performance Backend Languages (Go & Rust)

### Go Concurrency Safety & Memory Integrity:
- **Race Detector**: Always run and test with `-race` (`go test -race ./...`).
- **Context Propagation**: Pass `context.Context` to every blocking call for explicit cancellation and timeout deadlines.
- **Timing Safe Comparisons**:
```go
package security

import (
	"crypto/subtle"
)

// CompareSecrets performs constant-time comparison to prevent timing attacks
func CompareSecrets(a, b []byte) bool {
	return subtle.ConstantTimeCompare(a, b) == 1
}
```

### Rust Memory Safety & Fearless Concurrency:
- Leverage the ownership model to eliminate null pointer dereferences, use-after-free, and data races at compile time.
- Enforce `#![forbid(unsafe_code)]` in all application modules.
- Use `Zeroize` trait from the `zeroize` crate to securely scrub cryptographic keys from RAM upon drop.

---

## 6. Cryptographic Standards Checklist

| Primitive | Recommended Standard | Deprecated / Forbidden |
| :--- | :--- | :--- |
| **Symmetric Encryption** | AES-256-GCM, ChaCha20-Poly1305 | DES, 3DES, RC4, AES-CBC, AES-ECB |
| **Asymmetric Keys** | Ed25519 (signatures), X25519 (ECDH), RSA-4096 | RSA < 3072, DSA |
| **Hash Functions** | SHA-256, SHA-384, SHA-512, BLAKE3 | MD5, SHA-1 |
| **Password Hashing** | Argon2id (`m=64MB, t=3, p=4`), bcrypt (`cost >= 12`) | Plain SHA, PBKDF2 with low iterations |
| **RNG** | Cryptographically Secure PRNG (`/dev/urandom`, `CryptoRandom`) | `Math.random()`, `rand()` |
