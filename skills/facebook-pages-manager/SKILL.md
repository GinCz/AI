---
name: facebook-pages-manager
description: >-
  Manage Facebook Pages, publish posts (text, images, links), edit existing posts, delete posts, read feed and comments, inspect analytics and page info across Vladimir's 64 client business pages via Facebook Meta Graph API.
---
# Facebook Meta Graph API — 64 Managed Client Pages

Master operational manual and autonomous interface for publishing, editing, monitoring, and managing content across Vladimir's 64 client Facebook Pages.

---

## 1. Security & Token Architecture

- **App ID**: `1781406979801707` (App: `AI`)
- **Key Vault**: `Secret_Privat/PASS_KEYS/facebook_api.json` & `facebook_pages.json`
- **Token Lifespan**: **Permanent (`expires_at: 0`)** — never expire unless password is changed.
- **Granted Permissions**:
  - `pages_manage_posts` (Create, edit, delete posts)
  - `pages_read_engagement` (Read metrics, engagement, comments)
  - `pages_manage_metadata` (Manage page configurations & webhooks)
  - `pages_read_user_content` (Read user interactions)
  - `pages_manage_ads` & `ads_management` (Ads management)
  - `pages_show_list` & `business_management` (Business portfolio access)

---

## 2. Fast CLI Tool (`fb-cli`)

On `ORACLE_49`, the CLI utility is globally available at `/usr/local/bin/fb-cli` (and `AI/tools/fb_cli.py` in `Secret_Privat`).

### Quick Reference:

1. **Find Page ID / Check Access**:
   ```bash
   fb-cli list --search "reporyje"
   fb-cli list --search "aklis"
   ```

2. **Inspect Page Status & Verification**:
   ```bash
   fb-cli info --page "Autoservis - Řeporyje"
   ```

3. **Publish New Text Post**:
   ```bash
   fb-cli post --page "Gin-It: PC Servis, It služby" --message "Váš text příspěvku..."
   ```

4. **Publish Post with Photo**:
   ```bash
   fb-cli post --page "Autoservis - Řeporyje" --message "Nové vybavení dílny" --image "/path/to/photo.jpg"
   ```

5. **Read Recent Posts (Inspect Post IDs & Feedback)**:
   ```bash
   fb-cli posts --page "Autoservis - Řeporyje" --limit 5
   ```

6. **Edit Existing Post (Update Text)**:
   ```bash
   fb-cli edit --post-id "952516921289655_122095328990884829" --message "Aktualizovaný text příspěvku..."
   ```

7. **Delete Post**:
   ```bash
   fb-cli delete --post-id "952516921289655_122095328990884829"
   ```

---

## 3. Direct Python Graph API Usage

If custom API calls or advanced batch operations are required:

```python
import json, urllib.request, urllib.parse

# 1. Load permanent page token from cache
with open("/root/AI_49/repos/Secret_Privat/PASS_KEYS/facebook_pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

page_id = "952516921289655" # Example page
token = pages[page_id]["access_token"]

# 2. Edit existing post
post_id = "952516921289655_122095328990884829"
url = f"https://graph.facebook.com/v21.0/{post_id}"
data = urllib.parse.urlencode({"message": "New text", "access_token": token}).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={"User-Agent": "Antigravity/1.0"})
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode("utf-8"))
    print(res) # {"success": True}
```
