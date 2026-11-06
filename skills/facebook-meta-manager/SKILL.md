---
name: facebook-meta-manager
description: Manage 64 client and business Facebook Pages via Meta Graph API v21.0. Create, view, edit, and delete posts, upload photos, inspect followers/analytics, and search pages.
---

# 📱 Facebook Meta Manager Skill

This skill provides autonomous management of Vladimir Bulantsev's 64 client and business Facebook Pages using Meta Graph API v21.0 and perpetual page tokens (`expires_at: 0`).

Credentials vault:
- Master Keys: `/root/Secret_Privat/PASS_KEYS/facebook_api.json`
- Pages & Tokens: `/root/Secret_Privat/PASS_KEYS/facebook_pages.json`
- CLI executable: `fb` or `/root/Secret_Privat/AI/tools/fb_cli.py`

---

## 🛠️ Commands Reference (`fb` CLI)

### 1. List & Search Pages
List all 64 managed pages or search by keyword:
```bash
fb list
fb list --filter "Autoservis"
fb list --filter "Praha"
```

### 2. View Page Details & Analytics
Get page ID, followers count, fans/likes, URL, and category:
```bash
fb info --page "Gin-It: PC Servis, It služby"
fb info --page "952516921289655"
```

### 3. List Recent Posts
Fetch recent posts published on a page, with IDs, dates, preview, and Facebook post links:
```bash
fb posts --page "Gin-It: PC Servis, It služby" --limit 5
```

### 4. Create a Post
Publish a new text post:
```bash
fb post --page "Gin-It: PC Servis, It služby" --message "Ваш рекламный или информационный текст..."
```

Publish a post with an image:
```bash
fb post --page "Autoservis - Řeporyje" --message "Текст поста" --image "/path/to/image.jpg"
```

### 5. Edit an Existing Post
Update text of an existing post:
```bash
fb edit --post-id "108272877286995_1452040610359854" --message "Обновленный текст публикации..."
```
*(Optional `--page <PageName>` if the post ID does not start with `{page_id}_`)*

### 6. Delete a Post
Delete a post:
```bash
fb delete --post-id "108272877286995_1452040610359854"
```

### 7. Token Refresh (Disaster Recovery)
If Vladimir updates Facebook credentials or exchanges tokens:
```bash
fb exchange
```
