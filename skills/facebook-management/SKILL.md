---
name: facebook-management
description: >-
  Autonomous management of Vladimir's 64 Facebook Pages via Meta Graph API CLI (`fb_cli.py`). Use to list pages, publish posts with text/images/links, edit or delete posts, fetch recent feed posts, and check permanent tokens and health status.
---

# Facebook Meta Graph API Management Skill

Comprehensive operational guide and cheatsheet for managing Vladimir's 64 Facebook client and personal pages.

---

## 1. Secrets & Credentials Vault Locations

- **App Secrets**: [`D:\AI\GitHub\Secret_Privat\PASS_KEYS\facebook_api.json`](file:///D:/AI/GitHub/Secret_Privat/PASS_KEYS/facebook_api.json)
- **Pages Database & Permanent Tokens**: [`D:\AI\GitHub\Secret_Privat\PASS_KEYS\facebook_pages.json`](file:///D:/AI/GitHub/Secret_Privat/PASS_KEYS/facebook_pages.json)
- **Vault Documentation**: [`D:\AI\GitHub\Secret_Privat\PASS_KEYS\FACEBOOK_API.md`](file:///D:/AI/GitHub/Secret_Privat/PASS_KEYS/FACEBOOK_API.md)
- **Full Catalog of Pages**: [`D:\AI\GitHub\Secret_Privat\Facebook\Facebook_Pages.md`](file:///D:/AI/GitHub/Secret_Privat/Facebook/Facebook_Pages.md)
- **CLI Executable Tool**: [`D:\AI\GitHub\Secret_Privat\AI\tools\fb_cli.py`](file:///D:/AI/GitHub/Secret_Privat/AI/tools/fb_cli.py)

---

## 2. CLI Tool Usage & Syntax

Run with Python (`python` or `D:\AI\python\python.exe`):

### List All Managed Pages (64 Pages)
```powershell
python D:\AI\GitHub\Secret_Privat\AI\tools\fb_cli.py list
```

### Inspect Page Metadata & Health Status
```powershell
python D:\AI\GitHub\Secret_Privat\AI\tools\fb_cli.py info --page <PAGE_ID_OR_NAME>
```

### Fetch Recent Feed Posts
```powershell
python D:\AI\GitHub\Secret_Privat\AI\tools\fb_cli.py posts --page <PAGE_ID_OR_NAME> --limit 5
```

### Publish a Post (Text Only)
```powershell
python D:\AI\GitHub\Secret_Privat\AI\tools\fb_cli.py post --page <PAGE_ID_OR_NAME> --message "Текст поста..."
```

### Publish a Post with Image and Link
```powershell
python D:\AI\GitHub\Secret_Privat\AI\tools\fb_cli.py post --page <PAGE_ID_OR_NAME> --message "Текст поста..." --image "D:\AI\GEMINI\image.jpg" --link "https://example.com"
```

### Edit an Existing Post
```powershell
python D:\AI\GitHub\Secret_Privat\AI\tools\fb_cli.py edit --page <PAGE_ID_OR_NAME> --post-id <POST_ID> --message "Обновленный текст поста"
```

### Delete a Post
```powershell
python D:\AI\GitHub\Secret_Privat\AI\tools\fb_cli.py delete --page <PAGE_ID_OR_NAME> --post-id <POST_ID>
```

---

## 3. Key Managed Pages Reference

- **Чехия Сегодня**: `111361545587245`
- **Gin-It: PC Servis, It služby**: `108272877286995`
- **Gin-Tv**: `1162424973868549`
- **vladimir_bulantsev**: `117308237990790`
- **Autoservis - Řeporyje**: `952516921289655`
- **4ton-96**: `207005949469796`
- **Balance-B2B**: `115211476557886`
- **WowFlow**: `345156525607847`
- **TMK - Pracovní agentura Praha**: `755254967826070`
- **Салон красоты в Праге Sveta & Co**: `1436863916533231`
