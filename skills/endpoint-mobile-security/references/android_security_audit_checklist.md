# Android Security Audit & Hardening Checklist

An operational checklist for evaluating Android application security and personal device hygiene.

---

## 1. APK Security Evaluation Checklist

| Checkpoint | Vulnerability / Anti-Pattern | Recommended Secure Practice |
| :--- | :--- | :--- |
| **Android Keystore** | Storing symmetric keys in `SharedPreferences` or hardcoded in Java code. | Store keys in hardware-backed `AndroidKeyStore` with `setUserAuthenticationRequired(true)`. |
| **Network Security Config** | Cleartext HTTP traffic allowed (`android:usesCleartextTraffic="true"`). | Disable cleartext traffic. Use certificate pinning for critical endpoints. |
| **Exported Components** | Activities, Services, Broadcast Receivers set to `android:exported="true"` without permissions. | Set `android:exported="false"` unless explicitly intended for inter-app communication with custom signature permissions. |
| **Debuggable Flag** | Production APK with `android:debuggable="true"`. | Ensure `android:debuggable="false"` in release builds to prevent runtime memory inspection via debugger. |
| **WebView Security** | `setJavaScriptEnabled(true)` with enabled `addJavascriptInterface` exposed to untrusted web content. | Restrict JavaScript execution, disable file access (`setAllowFileAccess(false)`), use modern secure bridges. |

---

## 2. Quick ADB Security Audit Commands

```bash
# List all apps with system-level or high-risk permissions granted
adb shell pm list permissions -g -d

# Check all installed packages categorized as third-party (sideloaded or non-system)
adb shell pm list packages -3

# Identify apps possessing DEVICE_ADMIN status (used by enterprise MDMs or ransomware)
adb shell dpm list-active-admins

# Verify SELinux status (Must be 'Enforcing')
adb shell getenforce

# Check running background services
adb shell dumpsys activity services | grep -E "ServiceRecord|packageName"
```
