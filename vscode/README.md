# 💻 VS Code + Continue.dev & AI Coding Assistant Guide

> **Production setup guide for VS Code, Continue.dev, GitHub Copilot, Remote-SSH, and high-performance free LLM APIs on Windows, macOS, and Linux.**
> 
> *Repository:* [GitHub: AI/vscode ↗](https://github.com/GinCz/AI/tree/main/vscode) | *Author:* [Vladimir Bulantsev (GinCz) ↗](https://github.com/GinCz) | *Version:* v2026-09-04

---

## 🎯 Overview & Capabilities

This guide walks you through turning Visual Studio Code into an autonomous AI development environment using free, high-speed API endpoints and local extensions:

* **Autonomous In-Editor AI:** Integrated agent directly inside VS Code (comparable to GitHub Copilot and Cursor, with zero subscription fees).
* **Agent Mode Execution:** The AI autonomously runs shell commands, edits files, and tests scripts with one-click user confirmation.
* **Seamless Remote-SSH:** Work directly on remote Linux servers with full agent capabilities.
* **Tab Autocomplete:** Fast autocomplete powered by Groq LLaMA 3.3 70B.
* **Context Awareness:** Multi-file indexing, codebase embeddings, git diff analysis, and terminal output ingestion.

---

## 📦 Step 1: Install Visual Studio Code

Download and install the official build for your platform:
* [Download Visual Studio Code ↗](https://code.visualstudio.com/)

---

## 🧩 Step 2: Install Essential Extensions

Open the VS Code Extension Marketplace (`Ctrl+Shift+X` on Windows/Linux or `Cmd+Shift+X` on macOS) and install:

| Extension | Extension ID | Description |
| :--- | :--- | :--- |
| **Continue** | `Continue.continue` | Open-source AI code assistant (Chat, Edit, Agent Mode, Autocomplete) |
| **Remote - SSH** | `ms-vscode-remote.remote-ssh` | Connect to remote machines via SSH directly inside VS Code |
| **Remote Explorer** | `ms-vscode.remote-explorer` | Management UI for SSH connections and remote tunnels |
| **GitHub Copilot** *(Optional)* | `GitHub.copilot` | Official GitHub Copilot extension |

---

## 🔑 Step 3: Obtain Free AI API Keys

Obtain API keys from top-tier AI providers offering generous free tiers:

| Provider | Portal Link | Highlights |
| :--- | :--- | :--- |
| **Groq Cloud** | [console.groq.com/keys ↗](https://console.groq.com/keys) | Ultra-fast LPU inference (LLaMA 3.3 70B) |
| **Google AI Studio** | [aistudio.google.com/apikey ↗](https://aistudio.google.com/apikey) | Gemini 2.0 Flash / Pro with 1M–2M context window |
| **Mistral AI** | [console.mistral.ai/api-keys ↗](https://console.mistral.ai/api-keys) | Mistral Large and Codestral |
| **OpenRouter** | [openrouter.ai/keys ↗](https://openrouter.ai/keys) | Access to free open-weight models (`:free`) |
| **OpenAI** | [platform.openai.com/api-keys ↗](https://platform.openai.com/api-keys) | GPT-4o / o3-mini (Pay-as-you-go) |

---

## ⚙️ Step 4: Configure Continue (`config.yaml`)

1. In VS Code, open the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
2. Type `Continue: Open Config` and hit Enter.
3. Alternatively, open the file directly:
   * **Windows:** `%APPDATA%\Code\User\globalStorage\continue.continue\config.yaml`
   * **macOS:** `~/Library/Application Support/Code/User/globalStorage/continue.continue/config.yaml`
   * **Linux:** `~/.config/Code/User/globalStorage/continue.continue/config.yaml`
4. Copy the production template from [`config.yaml ↗`](config.yaml) in this directory and insert your API keys.

### 🤖 Supported Model Roles:
* **Agent Mode (Autonomous execution):**
  - Groq LLaMA 3.3 70B (`llama-3.3-70b-versatile`)
  - NVIDIA Nemotron 120B (via OpenRouter `:free`)
  - Mistral Large Latest
  - OpenAI GPT-4o
* **Chat & Targeted Editing:**
  - Google Gemini 2.5 / 2.0 Flash
  - Anthropic Claude 3.5 Sonnet (via OpenRouter)
* **Tab Autocomplete:**
  - Groq LLaMA 3.3 70B Versatile

---

## 🔐 Step 5: Configure Remote-SSH for Headless Development

### 1. Generate SSH Key Pair (PowerShell / Bash)
```powershell
ssh-keygen -t ed25519 -C "your_email@domain.com"
```

### 2. Copy Public Key to Remote Server
```powershell
Get-Content ~/.ssh/id_ed25519.pub | ssh root@YOUR_SERVER_IP "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

### 3. Setup SSH Config Template
Edit your local SSH configuration file:
* Windows: `notepad $HOME\.ssh\config`
* Linux / macOS: `nano ~/.ssh/config`

Insert hosts following our [`ssh_config.example ↗`](ssh_config.example) template:
```ssh-config
Host de-master
    HostName 152.53.182.222
    User root
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 30
    ServerAliveCountMax 3
```

### 4. Connect
Press `Ctrl+Shift+P` → `Remote-SSH: Connect to Host...` and select `de-master`.

---

## 🚀 Step 6: Operating in Agent Mode

1. Connect to your host via Remote-SSH.
2. Open the project root (`File` → `Open Folder...`).
3. In the Continue sidebar, switch mode from **Chat** to **Agent**.
4. Select a tool-capable model (e.g. Groq LLaMA 3.3 70B or GPT-4o).
5. Enter your prompt. The agent will inspect files, propose edits, and execute terminal commands upon your approval.

---

## ⌨️ Essential Keyboard Shortcuts

| Shortcut | Command | Action |
| :--- | :--- | :--- |
| `Ctrl+Alt+I` / `Cmd+Alt+I` | `Continue: Open Chat` | Focus AI chat sidebar |
| `Ctrl+I` / `Cmd+I` | `Continue: Edit Code` | Inline AI code generation & diff review |
| `Ctrl+Alt+Space` | `Continue: Force Autocomplete` | Trigger AI autocomplete manually |
| `Ctrl+Shift+P` | `Command Palette` | Access all VS Code & Continue actions |

---

## 📄 Reference Files in this Directory

* [`config.yaml ↗`](config.yaml) — Production configuration file for Continue.dev
* [`copilot-instructions.md ↗`](copilot-instructions.md) — Universal repo instruction template for GitHub Copilot
* [`ssh_config.example ↗`](ssh_config.example) — Production SSH host configuration template