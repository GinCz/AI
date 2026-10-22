# 🧠 Master AI Skills Framework: Unified Monolithic Compilation (All 35 Skills)

> **Single consolidated reference file containing all 35 domain skills for instant 1-click import into any AI engine (Google Antigravity, Claude, ChatGPT, Cursor, DeepSeek).**  
> *GitHub Repository:* https://github.com/GinCz/AI/tree/main/skills  
> *Raw URL for Direct Fetch:* https://raw.githubusercontent.com/GinCz/AI/main/skills/ALL_SKILLS.md  
> *Author:* Vladimir Bulantsev (@GinCz) | *Version:* v2026-10-22

---

## 🧭 Table of Contents

1. [agent-browser](#agent-browser) — *Web & Documentation*
2. [agy-customizations](#agy-customizations) — *Antigravity Engineering*
3. [allergology-clinical-immunology](#allergology-clinical-immunology) — *Clinical Medicine*
4. [antigravity-guide](#antigravity-guide) — *Antigravity Platform*
5. [antivirus-edr-threat-defense](#antivirus-edr-threat-defense) — *Antivirus & Host EDR Defense*
6. [auto-electronics-diagnostics](#auto-electronics-diagnostics) — *Automotive & EV*
7. [auto-mechanics-powertrain](#auto-mechanics-powertrain) — *Automotive & Powertrain*
8. [bankruptcy-insolvency-restructuring](#bankruptcy-insolvency-restructuring) — *Insolvency & Restructuring*
9. [clinical-cardiology-surgery](#clinical-cardiology-surgery) — *Clinical Medicine*
10. [code-review](#code-review) — *Software Engineering*
11. [compliance-anti-sanctions-aml](#compliance-anti-sanctions-aml) — *Compliance & Sanctions*
12. [cyber-defense-pentest](#cyber-defense-pentest) — *Cybersecurity*
13. [czech-accounting-tax](#czech-accounting-tax) — *Czech Accounting & Tax*
14. [czech-business-law](#czech-business-law) — *Czech Business Law*
15. [czech-litigation-advocacy](#czech-litigation-advocacy) — *Czech Litigation*
16. [devops-cloud-engineering](#devops-cloud-engineering) — *DevOps & Cloud*
17. [endpoint-mobile-security](#endpoint-mobile-security) — *Endpoint & Mobile Security*
18. [eu-business-law-compliance](#eu-business-law-compliance) — *EU Business Law*
19. [eu-litigation-crossborder-law](#eu-litigation-crossborder-law) — *EU Cross-Border Litigation*
20. [eu-vat-accounting](#eu-vat-accounting) — *EU VAT & Cross-Border Tax*
21. [internal-medicine-hematology](#internal-medicine-hematology) — *Clinical Medicine*
22. [intl-contract-drafting-ip](#intl-contract-drafting-ip) — *International Law & IP*
23. [network-hardware-firewalls](#network-hardware-firewalls) — *Enterprise Network & Firewalls*
24. [neurology-neurosurgery-triage](#neurology-neurosurgery-triage) — *Clinical Medicine*
25. [ophthalmology-vision-care](#ophthalmology-vision-care) — *Clinical Medicine*
26. [orthopedics-knee-rehab](#orthopedics-knee-rehab) — *Clinical Medicine*
27. [proctology-colorectal-surgery](#proctology-colorectal-surgery) — *Clinical Medicine*
28. [ru-accounting-tax](#ru-accounting-tax) — *Russian Accounting & Tax*
29. [ru-civil-corporate-law](#ru-civil-corporate-law) — *Russian Business Law*
30. [ru-litigation-advocacy](#ru-litigation-advocacy) — *Russian Litigation*
31. [secure-software-engineering](#secure-software-engineering) — *DevOps & Bulletproof Software Engineering*
32. [server-hardening-zerotrust](#server-hardening-zerotrust) — *Server Hardening*
33. [sysadmin-network-engineering](#sysadmin-network-engineering) — *SysAdmin & Networking*
34. [systematic-debugging](#systematic-debugging) — *Software Engineering*
35. [writing-plans](#writing-plans) — *Software Engineering*

---


<a name="agent-browser"></a>
# 📦 SKILL: agent-browser
*Domain:* **Web & Documentation**

---
name: agent-browser
description: >-
  Use this skill when you lack specific knowledge about a system command, a PowerShell cmdlet, or an API, and need to consult official documentation.
---
# Official Documentation Browsing

When writing system scripts, never hallucinate parameters or flags. If unsure, use your web searching tools to find the exact official documentation.

1. **For PowerShell / Windows Server**: Search "site:learn.microsoft.com PowerShell [Cmdlet-Name]". Read the documentation for the correct Windows version.
2. **For Bash / Linux**: Search for the official man pages (e.g., "man [command] linux") or specific distribution docs (Ubuntu, Debian, RHEL).
3. **Extraction**: Only extract the relevant flags and syntax. Do not copy generic examples without understanding them.

---

<a name="agy-customizations"></a>
# 📦 SKILL: agy-customizations
*Domain:* **Antigravity Engineering**

---
name: agy-customizations
description: >-
  Comprehensive guide and reference for the Antigravity Customization System.
  Use to explain how customizations work, their loading priority, discovery mechanisms,
  and to guide the creation of skills, rules, plugins, hooks, and MCP servers.
---

# Antigravity Customization System Guide

The Antigravity Customization System allows you to tailor the agent's behavior,
teach it new workflows, enforce guidelines, and integrate it with external
tools. By customizing the agent, you can transition it from a general-purpose
assistant to an expert pair programmer specialized in your project's codebase
and processes.

--------------------------------------------------------------------------------

## Customization Types: Quick Reference

Choose the right customization type based on your goal:

Type            | Config File/Folder           | Scope                     | Best For                                                                                | Learn More
:-------------- | :--------------------------- | :------------------------ | :-------------------------------------------------------------------------------------- | :---------
**Rules**       | `GEMINI.md`, `AGENTS.md`     | Contextual / Hierarchical | Enforcing coding styles, API restrictions, and local guidelines.                        | [Rules Guide](./docs/rules.md)
**Skills**      | `skills/<name>/SKILL.md`     | On-Demand (Progressive)   | Teaching the agent multi-step procedures, runbooks, and tool workflows.                 | [Skills Guide](./docs/skills.md)
**Plugins**     | `plugins/<name>/plugin.json` | Bundle                    | Packaging related skills, rules, and MCP configs into a single unit.                    | [Plugins Guide](./docs/plugins.md)
**Hooks**       | `hooks.json`                 | Lifecycle Event           | Running scripts/commands at specific agent lifecycle points (e.g., pre-tool execution). | [Hooks Guide](./docs/hooks.md)
**MCP Servers** | `mcp_config.json`            | Tool Integration          | Connecting the agent to external services and custom tool providers.                    | [MCP Guide](./docs/mcp_servers.md)

--------------------------------------------------------------------------------

## Customization Discovery and Locations

Antigravity automatically discovers your own customizations by traversing
specific directories. Built-in customizations are not found this way: the agent
config names the ones it mounts.

### Discovery Locations

1.  **Workspace Customizations** (Project-Specific):
    *   Path: `.agents/` (or `.agent/`, `_agents/`, `_agent/`) at the root of
        your project.
    *   Use this to share customizations with your team by checking them into
        version control (VCS).
    *   The agent walks from your current working directory up to the repository
        root (e.g., the folder containing `.git`) to find these directories.
2.  **Directory & Project Rules** (Hierarchical):
    *   Paths: `GEMINI.md`, `AGENTS.md`, `.agents/rules/*.md`
    *   As you open or edit files, the agent walks up from the file's directory
        to the repository root, loading all rules it finds.
3.  **Global Configuration** (Machine-Local):
    *   Path: `~/.gemini/config/`
    *   Applies to all projects and workspaces run on your machine.

--------------------------------------------------------------------------------

## Loading Priority and Precedence

When multiple customizations are discovered, they are loaded and applied in a
specific order. If there are naming conflicts (e.g., two skills with the same
name), the higher-priority customization overrides the lower-priority one.

The priority order (from highest to lowest) is:

1.  **Workspace Project**: Hierarchical discovery walking up from the CWD to the
    repository root.
2.  **Declared Configurations**: Customizations explicitly listed in
    `skills.json` or `plugins.json` in your workspace.
3.  **Global Discovery**: `~/.gemini/config/`
4.  **Built-in Customizations**: Default skills bundled with the application,
    mounted by name rather than discovered.
5.  **Global Declared Configurations**: Explicitly listed in global JSON
    configs.

--------------------------------------------------------------------------------

## How Customizations are Applied

### Progressive Disclosure (Skills and Rules)

To prevent overwhelming the model's context window, Antigravity uses
**progressive disclosure**:

*   **Skills** are not loaded into the context window by default. Only their
    names and descriptions are injected. The full content of a skill is only
    loaded if the model (or the user) explicitly decides to activate it.
*   **Rules** with `trigger: model_decision` behave similarly. Only `always_on`
    rules are loaded unconditionally.

### Deduplication

All customizations (especially rules) are deduplicated by their resolved file
paths. A rule file will never be injected more than once in a single
conversation turn, even if it matches multiple trigger conditions.

--------------------------------------------------------------------------------

## Advanced Management: JSON Configs

For customizations stored in non-standard locations, you can use `skills.json`
and `plugins.json` to explicitly register them and inherit from shared
configurations.

*   Learn how to configure these in the
    [JSON Configurations Guide](./docs/json_configs.md).

---

<a name="allergology-clinical-immunology"></a>
# 📦 SKILL: allergology-clinical-immunology
*Domain:* **Clinical Medicine**

---
name: allergology-clinical-immunology
description: >-
  Clinical allergology, immunology, allergic rhinitis, pollen and food sensitization, cross-reactivity (pollen-food syndrome), specific IgE, DAO (histamine intolerance), aTPO thyroid autoimmunity, allergen immunotherapy (AIT/SLIT), and pharmacotherapy.
---
# Clinical Allergology, Immunopathology & Molecular Diagnostics

A master clinical and diagnostic reference for evaluating allergic rhinitis, aeroallergen sensitization, pollen-food allergy syndromes, cross-reactivity cascades, mast cell disorders, histamine intolerance, autoimmune serology, and targeted pharmacotherapy.

---

## 1. Classification & Immunological Mechanisms

### A. Gell & Coombs Hypersensitivity Types:
1. **Type I (Immediate / IgE-Mediated)**:
   - Allergen exposure $\rightarrow$ cross-linking of surface-bound IgE on tissue mast cells and circulating basophils $\rightarrow$ immediate degranulation releasing preformed mediators (histamine, tryptase) followed by de novo synthesis of leukotrienes ($LTC_4, LTD_4$) and prostaglandins ($PGD_2$).
   - Clinical: Allergic rhinoconjunctivitis, bronchial asthma, urticaria/angioedema, anaphylaxis.
2. **Type II (Cytotoxic / Antibody-Mediated)**: IgG/IgM against cell-surface antigens (e.g. autoimmune hemolytic anemia, Goodpasture).
3. **Type III (Immune Complex-Mediated)**: Antigen-antibody complex deposition in microvasculature (e.g. serum sickness, post-streptococcal GN).
4. **Type IV (Delayed / T-Cell-Mediated)**: Sensitized CD4+/CD8+ T-lymphocytes releasing cytokines (e.g. contact dermatitis, drug eruptions).

---

## 2. Laboratory Diagnostics & Allergen Panels

### A. Total IgE vs. Specific IgE (ImmunoCAP):
- **Total Serum IgE**:
  - Non-specific screening marker. Normal $< 100\text{ kU/L}$ (in non-atopic adults).
  - Markedly elevated in severe atopic dermatitis, allergic bronchopulmonary aspergillosis (ABPA), parasitic helminth infections, and hyper-IgE syndrome.
  - Normal total IgE does **not** rule out clinically significant severe monosensitization.
- **Specific IgE (sIgE)**:
  - Quantitative measurement of allergen-specific antibodies using FEIA (ImmunoCAP) technology.
  - **CAP Class Scoring Matrix**:
    - **Class 0**: $< 0.35\text{ kU/L}$ (Negative / Undetectable)
    - **Class 1**: $0.35–0.69\text{ kU/L}$ (Low sensitization)
    - **Class 2**: $0.70–3.49\text{ kU/L}$ (Moderate sensitization)
    - **Class 3**: $3.50–17.49\text{ kU/L}$ (High sensitization)
    - **Class 4**: **$17.50–49.99\text{ kU/L}$** (Very high sensitization)
    - **Class 5**: $50.00–99.99\text{ kU/L}$ (Extremely high sensitization)
    - **Class 6**: $\ge 100.00\text{ kU/L}$ (Maximal sensitization)

### B. Major Aeroallergen Sensitizations:
- **Meadow Grass Pollen (Bojínek luční / *Phleum pratense* `g6`)**:
  - Dominant allergen components: `rPhl p 1` (Group 1 beta-expansin) and `rPhl p 5` (Group 5 ribonuclease-like protein) represent true primary grass sensitization. High titers (Class 4+) predict peak symptoms in May–July across Central Europe.
- **Tree Pollens**:
  - Birch (*Betula verrucosa* `t3`): Major component `Bet v 1` (PR-10 family). Peak pollination March–May.
  - Minor component `Bet v 2` (Profilin): Panallergen responsible for extensive broad cross-reactivity with plant foods.
  - Ash (*Fraxinus excelsior* `t15`), Olive, Alder, Hazel.

### C. Cereal / Grain Allergies & Pollen-Food Syndrome (Cross-Reactivity):
- **Grains (Obiloviny)**: Rye (*Secale cereale* `f5`), Wheat (*Triticum aestivum* `f4`), Barley (*Hordeum vulgare* `f6`), Oat (*Avena sativa* `f7`).
- **Pathways**:
  1. **True Food Allergy (IgE to storage proteins / lipid transfer proteins - LTPs, Tri a 19 / omega-5 gliadin)**: Can trigger severe food-dependent exercise-induced anaphylaxis (FDEIA).
  2. **Pollen-Associated Cross-Reactivity (PFS / Oral Allergy Syndrome - OAS)**: IgE antibodies generated against grass pollen Group 1/3 or birch `Bet v 1` cross-react with homologous proteins in raw cereal grains, nuts, and stone fruits. Heat labile; cooked grains often tolerated unless LTPs are involved.

---

## 3. Histamine Intolerance & Diamine Oxidase (DAO)

- **Pathophysiology**: Histamine is metabolized through two pathways:
  1. Extracellular / Intestinal: **Diamine Oxidase (DAO)** breaks down ingested dietary histamine in the intestinal mucosa.
  2. Intracellular / Systemic: **Histamine N-Methyltransferase (HNMT)**.
- **Serum DAO Activity Thresholds**:
  - **$> 10\text{ U/mL}$**: Normal DAO activity (histamine intolerance unlikely).
  - **$3–10\text{ U/mL}$**: Reduced DAO activity (histamine intolerance probable).
  - **$< 3\text{ U/mL}$**: Severe DAO deficiency.
- **Clinical Symptoms of Histamine Excess**: Postprandial flushing, sudden headache, tachycardia/palpitations, abdominal cramping, diarrhea, nasal congestion after consuming histamine-rich foods (aged cheeses, red wine, cured meats, sauerkraut, chocolate, canned fish).
- **Management**: Low-histamine diet, DAO enzyme replacement (taken 15–20 min before meals), vitamin B6 / copper cofactors.

---

## 4. Thyroid Autoimmunity: Anti-TPO Biomarker

- **Anti-Thyroperoxidase Antibodies (aTPO)**:
  - Directed against the thyroid peroxidase enzyme responsible for iodination of tyrosine residues on thyroglobulin.
  - Primary marker for **Hashimoto's Autoimmune Thyroiditis** and autoimmune polyglandular syndromes.
  - Reference range: typically $< 34\text{ kU/L}$ (method-dependent). Levels $\ge 40–50\text{ kU/L}$ confirm autoimmune thyroiditis even in the setting of normal baseline TSH and FT4 (euthyroid phase).
  - Monitoring protocol: Annual TSH and Free T4 check; initiation of levothyroxine replacement upon progression to subclinical or overt hypothyroidism.

---

## 5. Evidence-Based Pharmacotherapy for Allergic Diseases

### A. Intranasal Corticosteroids (INCS) - First-Line:
- **Mometasone furoate** (*Mommox, Nasonex* 50 mcg/spray):
  - Dosage: 2 sprays per nostril once daily (total 200 mcg/day).
  - Mechanism: Potent topical glucocorticoid receptor agonist; negligible systemic bioavailability ($< 0.1\%$). Inhibits recruitment and activation of eosinophils, basophils, and mast cells.
  - Technique: Spray directed laterally towards the ipsilateral ear, avoiding the nasal septum to prevent mucosal crusting and epistaxis.

### B. Second-Generation Non-Sedating Antihistamines (H1-Blockers):
- **Bilastine** (*Nestibil* 20 mg):
  - Dosage: 20 mg once daily on an empty stomach (1 hour before or 2 hours after food/fruit juice to ensure absorption).
  - Pharmacokinetics: High selectivity for peripheral $H_1$ receptors, no blood-brain barrier penetration (zero sedation), zero hepatic CYP450 metabolism (excreted unchanged in feces/urine; safe with liver impairment and minimal drug interactions).
- **Levocetirizine** (5 mg q24h) / **Desloratadine** (5 mg q24h): Alternative high-affinity selective inverse agonists.

### C. Allergen Immunotherapy (AIT / SLIT - Sublingual Immunotherapy):
- The only disease-modifying treatment capable of altering the natural course of allergic disease (preventing progression from allergic rhinitis to bronchial asthma).
- Mechanism: Repeated controlled allergen exposure induces regulatory T-cells ($T_{reg}$), suppresses Th2 responses, and triggers class-switching to protective **IgG4 blocking antibodies**.
- Regimen: 3 consecutive years of continuous or pre-coseasonal sublingual tablets/drops (e.g. *Grazax* for grass pollen).

---

<a name="antigravity-guide"></a>
# 📦 SKILL: antigravity-guide
*Domain:* **Antigravity Platform**

---
name: antigravity-guide
description: Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy), Antigravity 2.0, Antigravity IDE, Python SDK, slash commands, keybindings, and customizations (skills, rules, MCP, sidecars). Activate this skill when the user asks questions about how to use, configure, or customize Antigravity, AGY, the agy CLI, the Antigravity IDE, or Antigravity 2.0.
---

# Google Antigravity (AGY) Guide & Sitemap

Google Antigravity is an AI-first development platform. Depending on which
surface the user is asking about, you **MUST** read the corresponding
subdocumentation in the `references/` directory of this skill:

## 1. Surfaces Sitemap (Offline Subdocs)

-   **Antigravity CLI (`agy`)**: [references/cli.md](references/cli.md)
    -   Pointers to the authoritative public CLI docs for slash commands,
        features, settings, and best practices.
-   **Antigravity IDE**: [references/ide.md](references/ide.md)
    -   Covers the standalone AI-first IDE, sidebar chat panels, and inline code
        lenses.
-   **Antigravity 2.0**: [references/app.md](references/app.md)
    -   Covers the parallel desktop application, left-hand sidebar, chat canvas,
        and the HTML Auxiliary Pane (Subagents, Background Tasks, Artifacts,
        Files Changed, Terminals).
-   **Antigravity SDK**: [references/sdk.md](references/sdk.md)
    -   Covers the public Python SDK
        (https://github.com/google-antigravity/antigravity-sdk-python) for
        programmatic agent leasing, orchestration APIs, and custom tool
        exposing.

--------------------------------------------------------------------------------

## 2. Smart Hybrid Retrieval: When to Fetch Live Docs

The offline subdocs provide excellent quick references. However, if the user
asks for the latest updates, advanced Vertex AI integrations, or complex setups
not covered here, you **MUST** dynamically fetch the live page from the official
sitemap:

<!-- LINT.IfChange(sitemap) -->

-   **Main Documentation Home**: `https://antigravity.google/docs`
-   **Skills**: `https://antigravity.google/docs/skills`
-   **Rules**: `https://antigravity.google/docs/rules-workflows`
-   **Hooks**: `https://antigravity.google/docs/hooks`
-   **Plugins**: `https://antigravity.google/docs/plugins`
-   **Sidecars**: `https://antigravity.google/docs/sidecars`
-   **Model Context Protocol (MCP)**: `https://antigravity.google/docs/mcp`
-   **Browser Automation & Testing**:
    `https://antigravity.google/docs/ide/browser`
-   **Agent Permissions & Security**:
    `https://antigravity.google/docs/permissions`
-   **Terminal Sandbox**: `https://antigravity.google/docs/sandbox`
-   **Changelog & Release Notes**: `https://antigravity.google/changelog`
-   **Troubleshooting & Support**: `https://antigravity.google/support`
    <!-- LINT.ThenChange(//depot/google3/third_party/gemini_coder/agent_ui_toolkit/dev/appVariant/externalAppVariant.ts:custom_links) -->

---

<a name="antivirus-edr-threat-defense"></a>
# 📦 SKILL: antivirus-edr-threat-defense
*Domain:* **Antivirus & Host EDR Defense**

---
name: antivirus-edr-threat-defense
description: >-
  Enterprise antivirus management, Endpoint Detection & Response (EDR), Windows Defender hardening (ASR rules, WDAC, AppLocker, Sysmon), Linux host security (Wazuh, ClamAV, Lynis, Falco, eBPF Tetragon, AppArmor/SELinux), anti-ransomware protection, memory injection mitigation, and live incident triage.
---
# Antivirus, EDR & Host Intrusion Defense Engineering

A specialized operations guide for architecting, enforcing, and operating enterprise-grade antivirus systems, Endpoint Detection and Response (EDR) agents, host-level intrusion prevention, anti-ransomware tripwires, and live incident forensics across Windows and Linux platforms.

---

## 1. Antivirus & EDR Architecture Mechanics

### Detection Engines Taxonomy:
1. **Signature & Hash Matching**: Instant static lookup (SHA-256 / Authenticode). High speed, zero overhead, but vulnerable to trivial byte polymorphism.
2. **Heuristic Analysis**: Static code decompilation scanning for suspicious API import tables (e.g. `VirtualAllocEx`, `WriteProcessMemory`, `CreateRemoteThread`).
3. **Behavioral & Dynamic Sandboxing**: Monitoring runtime actions in real time (e.g. mass file renames, shadow copy deletions, unauthorized registry persistence).
4. **Machine Learning / Cloud Telemetry**: Analyzing telemetry against global threat intelligence models to detect zero-day malware patterns.
5. **Antimalware Scan Interface (AMSI)**: In-memory runtime buffer scanning for scripts (PowerShell, VBScript, JScript, Office VBA, .NET assembly loads) before execution.

---

## 2. Enterprise Windows Defender & Host Hardening

### PowerShell Script for Full Attack Surface Reduction (ASR) Deployment:
Microsoft Defender ASR rules block malware vectors (malicious Office macros, script-based downloaders, child process spawning, LSASS credential theft):

```powershell
<#
.SYNOPSIS
    Enforce maximum enterprise Attack Surface Reduction (ASR) rules on Windows.
#>
# Enable Windows Defender Real-Time and Cloud Protection
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -MAPSReporting Advanced
Set-MpPreference -SubmitSamplesConsent SendSafeSamples
Set-MpPreference -HighThreatDefaultAction Clean
Set-MpPreference -SevereThreatDefaultAction Clean

# ASR Rule GUIDs Matrix
$ASRRules = @{
    "Block executable content from email client and webmail"          = "be9b3d45-6107-4742-bb57-1521107c476f"
    "Block Office applications from creating child processes"          = "d4f940ab-401b-4efc-aadc-ad5f3c50688a"
    "Block Office applications from creating executable content"       = "3b5764aa-aed0-4df4-bb3e-815702e4d142"
    "Block Office applications from injecting code into processes"     = "756346d7-3953-435a-9c9c-0f92860502b0"
    "Block JavaScript or VBScript from launching downloaded executable"= "d3e037e1-3eb8-44c8-a917-57927947596d"
    "Block execution of potentially obfuscated scripts"                = "5beb7efe-fd9a-4556-801d-275e5ffc04cc"
    "Block Win32 API calls from Office macros"                         = "92e97fa1-2edf-4476-bdd6-9dd0b4dddc7b"
    "Block credential stealing from Windows Local Security Authority"  = "9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2"
    "Block process creations originating from PSExec and WMI commands" = "d1e49aac-8f56-4280-b9ba-993a6d77406c"
    "Block untrusted and unsigned processes that run from USB"         = "b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4"
    "Block persistence through WMI event subscription"                 = "e6db77e5-3e12-4247-81d7-0e0e5fe2b0d4"
    "Use advanced protection against ransomware"                       = "c1db55ab-c21a-4637-bb3f-a12568109d35"
}

foreach ($RuleName in $ASRRules.Keys) {
    $RuleGuid = $ASRRules[$RuleName]
    Add-MpPreference -AttackSurfaceReductionRules_Ids $RuleGuid -AttackSurfaceReductionRules_Actions Enabled
    Write-Output "ASR Rule Enforced: $RuleName ($RuleGuid)"
}

# Enforce Controlled Folder Access (Anti-Ransomware Shield)
Set-MpPreference -EnableControlledFolderAccess Enabled
```

### Windows Event Telemetry & Sysmon Deployment:
- Deploy Sysmon with SwiftOnSecurity configuration (`sysmon.exe -i sysmonconfig-export.xml`).
- Crucial Event IDs to monitor in SIEM:
  - **Event ID 1**: Process Creation (Command line, hashes, parent process).
  - **Event ID 7**: Image Loaded (DLL hijacking detection).
  - **Event ID 8**: CreateRemoteThread (Process injection indicator).
  - **Event ID 10**: ProcessAccess (LSASS access attempts).
  - **Event ID 11**: FileCreate (Ransomware staging, drop of executables).
  - **Event ID 12/13/14**: RegistryEvent (Persistence modifications).

---

## 3. Linux Host Intrusion Prevention & EDR (Wazuh & Falco)

### Wazuh Agent Deployment & Configuration:
Install and configure Wazuh agent to monitor log integrity, rootkits, and active response:
```bash
# Register agent with manager securely
WAZUH_MANAGER="manager.internal.gincz.com"
/var/ossec/bin/agent-auth -m "${WAZUH_MANAGER}" -P "AgentEnrollmentSecret123"

# Start and enable Wazuh agent
systemctl enable --now wazuh-agent
```

### Falco Runtime Syscall Monitoring (`/etc/falco/rules.d/custom_rules.yaml`):
```yaml
- rule: Shell Spawned by Ingress Container
  desc: Detect when a shell is launched inside a web-facing or production container
  condition: container.id != host and proc.name in (bash, sh, zsh, ksh) and evt.type = execve and not proc.pname in (entrypoint, docker-init)
  output: "CRITICAL: Suspicious shell spawned in container (user=%user.name container_id=%container.id container_name=%container.name cmdline=%proc.cmdline)"
  priority: CRITICAL
  tags: [mitre_execution, container]

- rule: Sensitive File Read (/etc/shadow)
  desc: Detect unauthorized access to password database
  condition: open_read and fd.name = "/etc/shadow" and not user.name in (root)
  output: "ALERT: Unauthorized attempt to read /etc/shadow (user=%user.name process=%proc.name cmdline=%proc.cmdline)"
  priority: WARNING
```

### ClamAV Real-Time On-Access Daemon (`/etc/clamav/clamd.conf`):
```ini
# Enforce On-Access scanning on high-risk directories
OnAccessMountPath /tmp
OnAccessMountPath /var/www/uploads
OnAccessIncludePath /home
OnAccessPrevention yes
OnAccessExtraScanning yes
OnAccessExcludeUname clamav
```

---

## 4. Anti-Ransomware Defenses & Tripwires

1. **Volume Shadow Copy Protection**:
   - Deny `vssadmin.exe delete shadows` and `wmic shadowcopy delete` via AppLocker and ASR rules.
2. **Canary Honeypot Files**:
   - Place hidden decoy files (e.g. `C:\Users\Public\Documents\!decoy_financial_statement.xlsx` or `/var/www/!canary.docx`) with strict auditing enabled.
   - Any write, rename, or delete event immediately triggers a high-priority alert and network isolation script.
3. **Immutable 3-2-1-1-0 Backup Standard**:
   - 3 copies of data, 2 different media types, 1 offsite, 1 offline (air-gapped or immutable S3 Object Lock), 0 errors after automated restore verification.

---

## 5. Live Incident Response & Triage Workflows

### Windows Live Triage Script:
```powershell
# Gather volatile evidence into triage artifact directory
$TriageDir = "C:\Triage_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path $TriageDir -Force | Out-Null

# 1. Active Network Connections with Process IDs
Get-NetTCPConnection | Select-Object LocalAddress,LocalPort,RemoteAddress,RemotePort,State,OwningProcess | 
    Export-Csv -Path "$TriageDir\Active_TCP_Connections.csv" -NoTypeInformation

# 2. Running Processes with Command Lines and Parent PIDs
Get-CimInstance Win32_Process | Select-Object ProcessId,ParentProcessId,Name,CommandLine,ExecutablePath |
    Export-Csv -Path "$TriageDir\Running_Processes.csv" -NoTypeInformation

# 3. Scheduled Tasks & Persistence Keys
Get-ScheduledTask | Where-Object { $_.State -ne 'Disabled' } | Select-Object TaskName,TaskPath |
    Export-Csv -Path "$TriageDir\ScheduledTasks.csv" -NoTypeInformation

Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" | Out-File "$TriageDir\Registry_HKLM_Run.txt"
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" | Out-File "$TriageDir\Registry_HKCU_Run.txt"
```

### Linux Live Triage Commands:
```bash
# Memory and running socket inspection
ss -tunap > /tmp/triage_sockets.txt
ps auxfww > /tmp/triage_processes.txt

# Audit open files of suspicious processes
lsof -i -P -n > /tmp/triage_network_files.txt

# Inspect recent persistence modifications
find /etc/cron* /etc/systemd/system /var/spool/cron -mtime -2 -ls > /tmp/recent_persistence.txt

---

<a name="auto-electronics-diagnostics"></a>
# 📦 SKILL: auto-electronics-diagnostics
*Domain:* **Automotive & EV**

---
name: auto-electronics-diagnostics
description: >-
  Automotive electrical systems, ECU tuning, network diagnostics (CAN, LIN, FlexRay, DoIP, J1939), oscilloscope sensor analysis, parasitic drain testing, immobilizers, and EV/Hybrid high-voltage safety.
---
# Automotive Electronics, Network Diagnostics & EV/Hybrid Engineering

A master operational engineering manual for automotive electrical troubleshooting, in-vehicle communication bus analysis, ECU diagnostics, sensor oscilloscope signal tracing, and High-Voltage (EV/HEV) safety protocols.

---

## 1. In-Vehicle Communication Networks & Bus Diagnostics

Modern vehicles utilize layered serial networks to interconnect Electronic Control Units (ECUs):

### A. Controller Area Network (CAN Bus - ISO 11898):
- **Physical Layer**:
  - Twisted pair: `CAN-High` (CAN-H) and `CAN-Low` (CAN-L).
  - **Termination Resistors**: Two **120 $\Omega$** resistors placed at the extreme physical ends of the bus (typically inside the Engine ECU and Instrument Cluster/Gateway).
  - **Static Resistance Check** (Ignition OFF, battery disconnected, measure across OBD-II pins 6 & 14):
    $$R_{\text{total}} = \frac{120 \times 120}{120 + 120} = 60\ \Omega$$
    - If reading **$120\ \Omega$** -> One termination resistor or wiring branch is open-circuit.
    - If reading **$0\ \Omega$** -> Direct short circuit between CAN-H and CAN-L.
    - If reading **$> 120\ \Omega$** or open -> Complete bus disconnection.
- **Dynamic Voltage & Oscilloscope Waveforms** (High-Speed CAN 500 kbps):
  - **Recessive State (Logical 1)**: Both lines idle at approximately **2.5 V** (differential voltage $\approx 0\text{ V}$).
  - **Dominant State (Logical 0)**:
    - `CAN-H` rises to approximately **3.5 V** (+1.0 V swing).
    - `CAN-L` drops to approximately **1.5 V** (-1.0 V swing).
    - Differential voltage ($V_{\text{diff}} = V_{\text{CAN-H}} - V_{\text{CAN-L}}$) $\approx \mathbf{2.0\text{ V}}$.
  - Common Waveform Faults:
    - CAN-H or CAN-L shorted to Ground (0V flatline).
    - CAN-H shorted to Battery 12V (flatline at battery voltage, drives transceiver into thermal shutdown).
    - Distorted, rounded waveforms indicating missing termination, severe capacitive loading, or damaged wiring harness.

### B. LIN Bus (Local Interconnect Network - ISO 17987):
- Single-wire, 12V asynchronous protocol operating at low speed (max 20 kbps).
- Master-Slave architecture used for smart peripherals: Alternator voltage regulators (COM/BSS/LIN), wiper motors, window regulators, climate control flap actuators.
- Recessive level = Battery Voltage (~12.0–14.0 V); Dominant level = Ground (~0.0–1.0 V).

### C. FlexRay & MOST Bus:
- **FlexRay**: High-speed (10 Mbps), dual-channel deterministic bus used in advanced chassis control (active steering, dynamic suspension).
- **MOST (Media Oriented Systems Transport)**: Optical fiber ring network for infotainment. Diagnosed using optical loop bypass connectors (*optická propojka*) to isolate broken control units breaking the optical circuit.

### D. Commercial Truck Protocol (SAE J1939):
- Heavy truck network standard operating at 250 kbps or 500 kbps over CAN.
- Uses Diagnostic Link Connector (DLC) 9-pin Deutsch connector.
- Fault codes formatted as **SPN** (Suspect Parameter Number) and **FMI** (Failure Mode Identifier).

---

## 2. Advanced Diagnostic Protocols & Tooling

### A. OBD-II / EOBD Operational Modes:
- **Mode \$01**: Live sensor data stream (PIDs: RPM, vehicle speed, coolant temp, fuel trims).
- **Mode \$02**: Freeze frame data (snapshot of parameters at the exact moment a DTC was stored).
- **Mode \$03**: Confirmed Diagnostic Trouble Codes (DTC).
- **Mode \$06**: On-Board Monitoring Test Results for non-continuously monitored systems:
  - Essential for identifying misfiring cylinders prior to DTC triggering (TID/CID misfire counts).
  - Catalytic converter and oxygen sensor aging thresholds.

### B. Professional Tool Ecosystems:
- **VAG (Volkswagen, Audi, Škoda, Seat)**: VCDS (HEX-V2 / HEX-NET) for adaptations/coding; ODIS-S / ODIS-E for factory flashing and component protection (*ochrana dílů*).
- **BMW**: ISTA-D (Rheingold) for guided troubleshooting; ISTA-P / E-Sys for ECU coding and programming.
- **Mercedes-Benz**: Xentry Diagnosis / DAS, Vediamo, DTS Monaco.
- **Universal Multi-Brand**: Launch X431, Autel MaxiSys, Delphi DS150E, Bosch KTS.

---

## 3. Sensor & Actuator Oscilloscope Analysis

Multimeters measure root-mean-square (RMS) or average voltage; **only an oscilloscope** reveals transient dropouts, glitches, and phase misalignments.

### A. Crankshaft (CKP) & Camshaft (CMP) Phase Correlation:
- **Hall Effect Sensors**: Digital 0–5V or 0–12V square waves.
- **Inductive / Reluctor Sensors**: Analog AC sine wave where frequency and amplitude increase proportionally with engine speed. Missing tooth indicates TDC reference.
- **Timing Chain Stretch Diagnostics**:
  - Connect Channel A to CKP and Channel B to CMP.
  - Measure the precise number of crankshaft teeth or milliseconds between the missing tooth reference and camshaft sync edge. Compare against golden reference waveforms to identify timing chain stretch without engine disassembly.

### B. Fuel Trim & Lambda / Oxygen Sensor Diagnostics:
- **Short-Term Fuel Trim (STFT)** & **Long-Term Fuel Trim (LTFT)**:
  - Normal range: $-5\%$ to $+5\%$.
  - High Positive Fuel Trim ($> +15\%$ to $+25\%$): Lean condition (vacuum leak, unmetered air after MAF, low fuel pressure, clogged fuel injectors).
  - High Negative Fuel Trim ($< -15\%$ to $-25\%$): Rich condition (leaking injector, high fuel pressure, restricted air intake, stuck EVAP purge valve).
- **Broadband Lambda Sensor (Bosch LSU 4.9)**:
  - Operates via internal oxygen pump cell; current ($I_p$) in microamperes ($\mu\text{A}$) determines air-fuel equivalence ratio $\lambda$. Rapid response to throttle blips.

---

## 4. Vehicle Parasitic Drain & Electrical Distribution

### Parasitic Battery Drain Testing (*Měření klidového odběru*):
1. **Preparation**:
   - Close all door latches manually with a screwdriver while doors remain open to access fuse boxes.
   - Lock vehicle via key fob and wait **20 to 45 minutes** for all ECUs to enter deep sleep mode.
2. **Current Measurement**:
   - Normal quiescent sleep current: **$< 30\text{ mA} - 50\text{ mA}$** (0.03–0.05 A).
   - If drain $> 150\text{ mA} - 1.5\text{ A}$ -> Active parasitic draw discharging battery overnight.
3. **Non-Invasive Voltage Drop Technique**:
   - Measure DC millivolts ($mV$) directly across the test points on the back of each blade fuse without pulling the fuse (pulling fuses wakes sleeping modules).
   - Convert $mV$ drop to current using standard fuse chart (e.g. 1.0 mV across a standard 10A mini fuse indicates $\approx 135\text{ mA}$ flowing through that circuit).

---

## 5. ECU Engineering, Immobilizers & Key Programming

- **Microcontroller & EEPROM Work**:
  - Reading/Writing EEPROMs (e.g. 24Cxx, 93Cxx, 95xxx) and flash microcontrollers (Infineon TriCore TC17xx/TC2xx, Motorola/Freescale MPC5xx/MPC55xx).
  - Bench mode & Boot mode connections using pinout harnesses (eliminating need to desolder chips).
- **Immobilizer (Immo) Architectures**:
  - Transponder keys: Megamos Crypto 48, Hitag 2 (PCF7936), Texas Crypto (4D/4E/DST+).
  - Extracting PIN / Secret Key Code (SKC) from Instrument Cluster, BCM, or Engine ECU.
  - Component Protection (*Ochrana dílů*): Cryptographic pairing between donor modules and gateway/chassis VIN to prevent theft of parts.

---

## 6. High-Voltage (EV & Hybrid) Safety & Architecture

Working on electric (BEV) and hybrid (HEV/PHEV) vehicles requires certified High-Voltage qualifications and strict life-safety protocols:

### A. The 5 Safety Rules for High-Voltage Isolation:
1. **Disconnect Completely (*Odpojit*)**: Turn off ignition, remove key fob to safe distance (> 5m), disconnect 12V auxiliary battery negative terminal.
2. **Secure Against Reconnection (*Zabezpečit proti opětovnému zapnutí*)**: Pull the **Manual Service Disconnect (MSD / orange service plug)** and lock out / tag out (LOTO) with a safety padlock.
3. **Verify Absence of Voltage (*Ověřit beznapěťový stav*)**:
   - Use a calibrated, two-pole high-voltage detector rated for **CAT IV 1000V** (never use a standard multimeter).
   - Test tester on known live source -> Test vehicle HV terminals -> Retest tester on known source.
   - Verify that DC voltage between HV+ and HV-, HV+ and Chassis, and HV- and Chassis is **$< 60\text{ V DC}$** (safe threshold).
4. **Earth & Short-Circuit (where prescribed)**.
5. **Cover Adjacent Live Parts**.

### B. High-Voltage Components & Diagnostics:
- **HVIL (High Voltage Interlock Loop)**: Low-voltage series circuit looping through all HV connectors, lids, and service plugs. If any connector is opened, the BMS instantly drops the main contactors.
- **Battery Management System (BMS)**:
  - Monitoring individual cell voltages (millivolt variance between highest and lowest cell; delta $> 30-50\text{ mV}$ indicates degraded cell pack).
  - Isolation resistance monitoring ($R_{\text{iso}} > 500\ \Omega/\text{V}$ required).
- **Inverter & Power Electronics**:
  - Three-phase AC drive generation via IGBT or SiC MOSFET bridges.
  - Bidirectional DC-DC converter stepping 400V/800V pack voltage down to 12V/14V to charge auxiliary battery.

---

<a name="auto-mechanics-powertrain"></a>
# 📦 SKILL: auto-mechanics-powertrain
*Domain:* **Automotive & Powertrain**

---
name: auto-mechanics-powertrain
description: >-
  Automotive mechanical engineering and repair: ICE engines (petrol, diesel Common Rail, classic carbs), heavy commercial trucks (pneumatic brakes, SCR/AdBlue, Euro 3-6), transmissions (manual, automatic, DSG/DCT), chassis, steering, and suspension overhaul.
---
# Automotive Mechanics, Powertrain & Commercial Vehicle Overhaul

A master operational engineering manual for automotive mechanics, engine rebuilding, heavy-duty commercial truck systems, transmissions, and chassis overhaul across modern and classic vehicles.

---

## 1. Internal Combustion Engine (ICE) Mechanics & Rebuilding

### A. Petrol / Gasoline Engines (MPI, Direct Injection TSI/GDI):
- **Fuel Delivery Systems**:
  - Multi-Point Fuel Injection (MPI): Low pressure (3–4 bar), manifold injection.
  - Direct Injection (GDI, TSI/TFSI): High-pressure mechanical fuel pump driven by camshaft lobe (150–350 bar), carbon build-up on intake valves (cleaning via walnut blasting / chemical soaking), piezo vs solenoid high-pressure injectors.
- **Variable Valve Timing (VVT / VANOS / VTEC)**:
  - Oil control valves (solenoids), camshaft phasers. Diagnosis of timing rattle on cold start (worn camshaft sprockets or check valve failure).

### B. Diesel Engines (Common Rail & Pumpe-Düse):
- **Common Rail (CR) Architecture**:
  - High-pressure pump (Bosch CP1/CP3/CP4, Delphi, Denso) reaching 1,600 to 2,500 bar.
  - Fuel return flow test (*přepadová zkouška vstřikovačů*): Measuring return line volume across all cylinders via graduated vials to detect leaking injector valves causing hard hot start or rail pressure drop (DTC P0087).
  - High-pressure pump CP4 failure warning: Swarf/metal particles in fuel filter housing requiring complete fuel system replacement (tank, lines, rails, injectors).
- **Pumpe-Düse (PD / Unit Injector)**:
  - Camshaft-driven individual unit injectors; adjusting pre-load rocker lash (turn bottom out, back off 180°–225°).
  - Worn injector seats in aluminum cylinder head causing fuel mixing into engine oil or hard starting.

### C. Classic Engines & Carburetion:
- **Carburetor Tuning & Overhaul (Weber, Solex, Pierburg, Zenith)**:
  - Float height measurement and needle valve sealing.
  - Idle mixture (*bohatost směsi*) adjustment via idle screw and CO meter; secondary throttle progression; accelerator pump diaphragm check.
  - Multi-carburetor vacuum synchronization using flow meters / manometer sync gauges.
- **Mechanical Ignition Distributors**:
  - Breaker points gap and dwell angle (*úhel sepnutí kontaktů* - typically 50°–54° on 4-cylinder engines).
  - Stroboscopic timing light dynamic setting: Initial base timing with vacuum advance hose disconnected and plugged; verifying centrifugal advance curve across RPM range.

### D. Engine Overhaul Tolerances & Diagnostics:
- **Compression & Cylinder Leak-Down Testing (*Měření komprese a tlakové ztráty válců*)**:
  - Dry vs. wet compression test: If adding 10ml of engine oil into spark/glow plug hole restores low compression -> worn piston rings/cylinder bore; if unchanged -> leaking intake/exhaust valves or blown head gasket.
  - Leak-down test: Supplying regulated compressed air (e.g. 6 bar) at TDC compression:
    - Air hissing from intake manifold -> leaking intake valve.
    - Air hissing from exhaust pipe -> leaking exhaust valve.
    - Air bubbles in expansion tank -> cracked cylinder head or blown head gasket.
    - Air whistling from oil filler cap / dipstick -> worn piston rings or cylinder wall scoring.
- **Precision Metrology**:
  - Cylinder bore ovality and taper (*ovalita a kuželovitost válce*) measured via internal bore gauge (*dutinoměr*).
  - Crankshaft journal clearance verified using **Plastigauge** (typical clearance 0.025 mm – 0.050 mm).
  - Cylinder head surface planarity checked with precision straightedge and feeler gauge (max deflection < 0.05 mm across head length).

---

## 2. Heavy Commercial Vehicles & Trucks (Scania, Volvo, MAN, DAF, Actros)

### A. Pneumatic Air Brake Systems:
- **Air Generation & Preparation**: Compressor, integrated air dryer with desiccant cartridge (*vysoušeč vzduchu*), four-circuit protection valve (*čtyřokruhový jisticí ventil*) isolating independent circuits (front axle, rear axle, trailer, auxiliary).
- **Actuation & Parking**:
  - Foot brake valve (*pedálový brzdový ventil*), relay valves, ABS/EBS modulators.
  - Spring brake actuators (*pružinové brzdové válce - Tristop*): Spring-applied parking brake; mechanical wind-off procedure for emergency towing.
  - Brake disc and drum overhaul: Minimum thickness, heat cracks, pneumatic slack adjusters (*automatické stavěče vůle brzd*).

### B. Heavy Diesel Emissions & Aftertreatment:
- **SCR (Selective Catalytic Reduction) & AdBlue (DEF)**:
  - Urea injection pump, dosing unit, NOx sensors (pre-cat and post-cat).
  - Crystallization clearing in dosing injector; diagnosing SCR efficiency DTCs.
- **DPF & EGR in Commercial Fleets**:
  - Differential pressure sensor diagnostics; thermal management for active regeneration; EGR cooler failure (exhaust gas leaking into coolant or coolant ingestion into intake).
- **Auxiliary Retarders (Hydraulic Retarder & Engine Compression Brake / Jake Brake)**:
  - Fluid heat exchanger, proportional valve actuation, exhaust throttle flap.

---

## 3. Transmissions, Clutches & Drivetrain

### A. Manual Transmissions & Clutches:
- **Dual-Mass Flywheel (*Dvouhmotový setrvačník*) Inspection**:
  - Measuring rotational free play (*vůle pootočení*) in teeth/degrees and tilt rock play (*vůle vyklopení*). Metallic clatter on shutdown indicates worn internal damping springs.
- **Clutch Replacement**:
  - Self-Adjusting Clutch (SAC) installation requiring specialized pre-tensioning tool to avoid premature adjuster ratcheting.
  - Release bearing (*vypínací ložisko* / concentric slave cylinder - CSC) hydraulic bleeding.

### B. Dual-Clutch Transmissions (DSG / DCT / S-Tronic):
- **Dry Clutch (e.g. VAG DQ200 - 7-speed)**:
  - Exact clutch pack shimming with depth gauge; mechatronic hydraulic accumulator pressure checks (accumulator blow-out causing P17BF).
- **Wet Clutch (e.g. VAG DQ250, DQ381, DQ500 / BMW DKG)**:
  - Regular 60,000 km fluid and filter change; mechatronic solenoid cleaning; basic settings calibration via diagnostic tool (adaptation of clutch kiss points and gear selector synchronizers).

### C. Torque-Converter Automatic Transmissions:
- Planetary gear sets, torque converter lock-up clutch (*lock-up spojka*).
- Complete fluid exchange using automated ATF flushing machines (dynamic exchange under running engine) vs. static drain/fill; monitoring transmission oil temperature during level check.

### D. Differentials & Drivetrain Components:
- Setting ring and pinion gear backlash (*zubová vůle*) and tooth contact pattern using marking compound (*inženýrská modř*).
- CV joint (*homokinetický kloub*) boot replacement and grease repacking; propshaft center support bearing alignment.

---

## 4. Chassis, Suspension, Steering & Hydraulics

### A. Suspension Systems:
- **MacPherson & Multi-Link**: Bushing press-in/press-out techniques, ball joint taper extraction, coil spring compressor safety.
- **Air Suspension (*Pneumatické odpružení*)**:
  - Diagnosing leaking air bellows (*vzduchové měchy*) with soapy water / leak spray.
  - Air suspension compressor testing (max pressure output > 14–16 bar); valve block solenoid integrity; ride height sensor calibration via diagnostic software.

### B. Steering & Geometry:
- **Steering Racks**: Hydraulic rack seal rebuilding, electro-hydraulic pumps (EHPS), electric power steering (EPS) torque sensor zero-point calibration.
- **4-Wheel Alignment (*Geometrie kol*)**:
  - Toe-in / Toe-out (*sbíhavost*), Camber (*odklon*), Caster (*záklon rejdového čepu*), Kingpin inclination (*příklon*), Thrust angle (*jízdní osa*).
  - Calibrating Steering Angle Sensor (SAS / G85) after every wheel alignment.

### C. Hydraulic Brake Systems:
- Brake caliper slide pin cleaning and high-temp silicone lubrication (never use copper grease on rubber boots).
- Hydraulic pressure bleeding with automated brake bleeder (1.5–2.0 bar); ABS pump cycling procedure to evacuate air trapped in internal accumulator valves.
- Electronic Parking Brake (EPB): Driving caliper pistons into service mode via diagnostics prior to rear pad replacement; zero-point thickness calibration upon completion.

---

<a name="bankruptcy-insolvency-restructuring"></a>
# 📦 SKILL: bankruptcy-insolvency-restructuring
*Domain:* **Insolvency & Restructuring**

---
name: bankruptcy-insolvency-restructuring
description: >-
  Corporate insolvency, debt restructuring, and bankruptcy litigation: EU Cross-Border Insolvency Regulation 2015/848 (COMI, main/secondary proceedings, Preventive Restructuring Directive 2019/1023), Czech Insolvency Act (IZ č. 182/2006 Sb., konkurs, reorganizace, oddlužení, voidable transactions §§ 235–243), and Russian Bankruptcy Law (127-FZ, contesting suspect transactions Art. 61.2/61.3, and subsidiary liability of controlling persons KDL Chapter III.2).
---
# Bankruptcy, Insolvency & Corporate Restructuring

An exhaustive, high-level tactical and legal treatise for bankruptcy trustees (*insolvenční správci / arbitration receivers*), restructuring advisors, creditors' committee counsel, and defense attorneys protecting directors from personal subsidiary liability.

---

## 1. European Cross-Border Insolvency (Regulation (EU) 2015/848)

Governs jurisdiction, applicable law, and recognition of insolvency proceedings across the European Union:

### A. Centre of Main Interests (COMI) & Jurisdiction (Article 3):
- **Main Insolvency Proceedings**: Can be opened only in the Member State where the debtor's **Centre of Main Interests (COMI)** is situated.
  - *Statutory Presumption*: For companies, COMI is presumed to be the place of the **registered office**.
  - *Rebuttal of Presumption*: The presumption is rebutted if central management, key executive decisions, core assets, and regular commercial interactions are perceivable by third parties to be located in another Member State. Shifting the registered office within 3 months prior to petition does not shift COMI presumption.
  - *Universal Effect*: Main proceedings encompass all debtor's assets located across the entire European Union.
- **Secondary Insolvency Proceedings**: Can be opened in a Member State where the debtor possesses an **Establishment** (*provozovna* - place of operations with human and material means). Scope is strictly limited to assets located in that specific territory.

### B. Preventive Restructuring Frameworks (Directive (EU) 2019/1023):
- Enables viable debtors in financial distress to restructure debt before entering formal court liquidation.
- Key mechanisms: Stay of individual enforcement actions (*moratorium*), adoption of restructuring plans approved by voting classes of creditors, and **cross-class cram-down** (binding dissenting creditor classes if fair and equitable).

---

## 2. Czech Insolvency Law (Insolvenční zákon č. 182/2006 Sb. - IZ)

### A. Statutory Definitions of Insolvency (*Úpadek* - § 3 IZ):
1. **Inability to Pay (*Platební neschopnost*)**:
   - Multiple creditors (at least two independent creditors).
   - Monetary liabilities overdue for more than **30 calendar days**.
   - Inability to meet liabilities (presumed if payments suspended, enforcement fruitless, or default exceeds 3 months).
2. **Over-indebtedness (*Předlužení*)**:
   - Applies to corporations and sole proprietors.
   - The aggregate sum of the debtor's liabilities exceeds the total fair market value of their assets, taking into account future business continuation (*going concern* valuation).

### B. Mandatory Statutory Filing Duty & Executive Liability (§ 98 IZ):
- The statutory executive (*jednatel / člen představenstva*) **must file an insolvency petition without undue delay** after becoming aware (or when they ought to have become aware exercising due managerial care) of the company's insolvency.
- **Personal Tort Liability**: Failure to file creates personal liability with all personal assets for damages caused to creditors (quantum of damage is presumed to be the difference between actual recovery and what creditors would have recovered had the petition been filed on time under § 99 IZ).

### C. Forms of Resolving Insolvency:
1. **Bankruptcy Liquidation (*Konkurs* - §§ 244–315)**:
   - Complete cessation of business, management powers transferred to the Insolvency Trustee (*Insolvenční správce*).
   - Monetization of the bankruptcy estate (*zpeněžení majetkové podstaty*) via public electronic auction and proportional payout to registered creditors.
2. **Reorganization (*Reorganizace* - §§ 316–364)**:
   - Available to large enterprises (turnover > 50M CZK or > 50 employees, or pre-packaged plan approved by majority creditors).
   - Debtor remains in possession (*DIP*), implementing a restructuring plan while preserving employment and ongoing business value.
3. **Debt Discharge (*Oddlužení* - §§ 389–418)**:
   - Available to individuals and sole proprietors without business debt (or with creditor consent).
   - Discharge granted via 3-year or 5-year repayment calendar (paying minimum required percentage of debt) or through liquidation of non-exempt personal assets.

### D. Avoidance of Detrimental Transactions (*Neúčinnost právních jednání* - §§ 235–243 IZ):
The insolvency trustee or creditors may file claw-back lawsuits (*odpůrčí žaloby*) to return assets to the estate:
1. **Transactions Without Adequate Consideration (*Jednání bez přiměřeného protiplnění* - § 240)**:
   - Contracts concluded within **1 year** prior to insolvency (or **3 years** if concluded with affiliated/close persons / *osoby blízké*).
2. **Preferential Transactions (*Zvýhodňující právní jednání* - § 241)**:
   - Early repayment of debt, providing additional collateral for unsecured debt, paying one creditor to the detriment of others within **1 year** (or **3 years** for affiliates).
3. **Intentional Detriment (*Úmyslně zkracující jednání* - § 242)**:
   - Transactions intended to divert assets or defraud creditors within **5 years** prior to insolvency.

---

## 3. Russian Bankruptcy Law (Federal Law No. 127-FZ)

Governed by **Federal Law No. 127-FZ "On Insolvency (Bankruptcy)"**:

### A. Core Criteria & Proceedings:
- Thresholds: Outstanding aggregate claims of at least **2,000,000 RUB** (for legal entities) or **500,000 RUB** (for citizens) overdue for more than **3 months**.
- **Successive Stages for Corporations**:
  1. *Observation (Nablyudenie)*: Interim manager analyzes financial state; creditors register claims in the register (*RTK*); management powers preserved with restrictions.
  2. *Financial Rehabilitation (Finansovoye ozdorovleniye)* or *External Administration (Vneshneye upravleniye)*: Restructuring attempts.
  3. *Bankruptcy Liquidation (Konkursnoye proizvodstvo)*: Management dismissed; Bankruptcy Receiver (*Konkursny upravlyayushchy*) sells all assets at open electronic auction on specialized platforms (Sberbank-AST, Fabrikant, RAD).

### B. Challenging Debtor Transactions (Articles 61.2 and 61.3 of Law 127-FZ):
Transactions concluded prior to bankruptcy can be judicially invalidated:
1. **Suspicious Transactions with Unequal Counter-Performance (Part 1 Art. 61.2)**:
   - Concluded within **1 year** prior to or after acceptance of the bankruptcy petition. Price or terms substantially worse than market benchmarks (e.g. sale of commercial vehicles or real estate at 50% of cadastral/market price).
2. **Transactions Intended to Harm Property Rights of Creditors (Part 2 Art. 61.2)**:
   - Concluded within **3 years** prior to petition. Debtor was insolvent, and the counterparty knew or should have known of the insolvency (presumed for affiliated persons).
3. **Preferential Transactions (Art. 61.3)**:
   - Preferential repayment to one creditor over others concluded within **1 month** (or **6 months** for bad-faith/affiliated counterparties) prior to bankruptcy filing.

### C. Subsidiary Liability of Controlling Persons (KDL - Chapter III.2 of Law 127-FZ):
The ultimate weapon of creditors against company owners, actual beneficiaries, and directors:

1. **Controlling Debtor Person (*KDL*) Definition (Art. 61.10)**:
   - Any physical person or entity that had the power to determine the debtor's actions within the **3 years** preceding the emergence of insolvency signs up to the court petition (CEO, board members, 50%+ shareholders, shadow beneficiaries directing cashflows).
2. **Grounds for Imposing Subsidiary Liability**:
   - **Impossibility of Full Debt Satisfaction (Art. 61.11)**:
     - Imposed if bankruptcy was caused by actions/orders of the KDL.
     - *Statutory Presumptions of Guilt*:
       - Significant transactions causing harm to creditors were executed.
       - Accounting documents or mandatory corporate records are missing, falsified, or concealed.
       - More than 50% of third-priority creditor claims arose from tax offenses (FNS tax audit assessments).
   - **Failure to File Bankruptcy Petition on Time (Art. 61.12)**:
     - The director is personally liable for all obligations that arose **after the expiration of 1 month** from the date the company became insolvent.
3. **Defense Strategies for Managing Directors & Beneficiaries**:
   - *Business Judgment Rule (Justified commercial risk)*: Demonstrating that decisions were made in good faith on an informed basis within customary commercial practices.
   - *Economic Recovery Plan (Economically justified anti-crisis plan)*: Proving that the delay in bankruptcy filing was justified by a realistic, active anti-crisis restructuring strategy (negotiating bank credit extensions, finding new contracts).
   - Separating personal wealth from corporate assets; documenting all arm's-length intercompany transactions with independent appraisals.

---

<a name="clinical-cardiology-surgery"></a>
# 📦 SKILL: clinical-cardiology-surgery
*Domain:* **Clinical Medicine**

---
name: clinical-cardiology-surgery
description: >-
  Clinical cardiology, cardiac surgery, hemodynamics, 12-lead ECG interpretation, arterial hypertension guidelines, coronary artery disease, heart failure management (GDMT), and post-cardiac surgical recovery.
---
# Clinical Cardiology, Interventions & Cardiac Surgery

A comprehensive evidence-based clinical guide for evaluating cardiovascular disease, interpreting diagnostics, understanding interventional and surgical heart procedures, and managing pharmacotherapy in accordance with European Society of Cardiology (ESC) and American Heart Association (AHA) guidelines.

---

## 1. Arterial Hypertension & Hemodynamic Management

### A. Blood Pressure Classification (ESC/ESH Guidelines):
- **Optimal**: $< 120 / < 80\text{ mmHg}$.
- **Normal**: $120–129 / 80–84\text{ mmHg}$.
- **High-Normal**: $130–139 / 85–89\text{ mmHg}$.
- **Grade 1 Hypertension**: $140–159 / 90–99\text{ mmHg}$.
- **Grade 2 Hypertension**: $160–179 / 100–109\text{ mmHg}$.
- **Grade 3 Hypertension**: $\ge 180 / \ge 110\text{ mmHg}$.
- **Isolated Systolic Hypertension**: $\ge 140\text{ mmHg}$ and $< 90\text{ mmHg}$ (common in elderly due to arterial stiffening).

### B. Pharmacotherapy - The First-Line Classes:
1. **ACE Inhibitors (ACEi)** (*ramipril, perindopril*) or **Angiotensin Receptor Blockers (ARBs)** (*telmisartan, losartan, candesartan*):
   - First-line for hypertension with diabetes, chronic kidney disease (albuminuria), or heart failure.
   - Mechanism: Inhibit the renin-angiotensin-aldosterone system (RAAS), preventing vasoconstriction and sodium retention.
   - Monitoring: Serum potassium and creatinine (rise up to 30% acceptable initially; check for hyperkalemia).
2. **Dihydropyridine Calcium Channel Blockers (DHP-CCB)** (*amlodipine, felodipine*):
   - Potent arterial vasodilators reducing peripheral vascular resistance.
   - Side effect profile: Dose-dependent peripheral ankle edema (fluid redistribution, not volume overload).
3. **Thiazide-like Diuretics** (*indapamide, chlorthalidone*):
   - Preferred over hydrochlorothiazide due to longer half-life and better cardiovascular outcome evidence.
   - Monitoring: Serum sodium (hyponatremia), potassium (hypokalemia), uric acid.
4. **Beta-Blockers (BB)** (*bisoprolol, metoprolol succinate, carvedilol, nebivolol*):
   - Reserved as first-line when specific compelling indications exist: post-myocardial infarction, symptomatic angina, heart failure with reduced ejection fraction (HFrEF), or rate control in atrial fibrillation.

### C. Hypertensive Crisis:
- **Hypertensive Urgency**: Severe BP elevation ($\ge 180 / \ge 110\text{ mmHg}$) **without** acute target organ damage. Managed with oral anti-hypertensives over 24–48 hours; rapid precipitous drops must be avoided.
- **Hypertensive Emergency**: Severe BP elevation accompanied by acute life-threatening end-organ damage (acute aortic dissection, acute pulmonary edema, acute coronary syndrome, ischemic stroke/intracerebral hemorrhage, hypertensive encephalopathy, acute renal failure, malignant retinopathy). Requires immediate ICU admission and titrated intravenous infusions (e.g. labetalol, urapidil, nitroprusside).

---

## 2. Ischemic Heart Disease (IHD) & Acute Coronary Syndromes (ACS)

### A. Clinical Spectrum:
- **Stable Angina**: Predictable retrosternal chest tightness or pressure brought on by physical exertion or emotional stress, lasting $< 10–15$ minutes, relieved within minutes by rest or sublingual nitroglycerin.
- **Acute Coronary Syndrome (ACS)**:
  - **STEMI (ST-Elevation Myocardial Infarction)**: Transmural myocardial ischemia caused by complete acute thrombotic occlusion of a coronary artery. Requires immediate emergency reperfusion (**Primary PCI within 120 minutes** of FMC).
  - **NSTEMI (Non-ST-Elevation Myocardial Infarction)**: Subendocardial necrosis without persistent ST-elevation. Elevated high-sensitivity cardiac troponins (hs-cTnI / hs-cTnT) demonstrating a rising/falling kinetic pattern.
  - **Unstable Angina**: Rest angina, new-onset severe angina, or crescendo angina **without** biomarker elevation (normal troponins).

### B. Cardiac Biomarkers:
- **High-Sensitivity Cardiac Troponin (hs-cTnI / hs-cTnT)**:
  - Regulatory structural proteins of the cardiac contractile apparatus.
  - ESC 0h/1h or 0h/2h diagnostic algorithm: Baseline measurement followed by delta change at 1 or 2 hours to rapidly rule out or rule in myocardial necrosis.

---

## 3. 12-Lead Electrocardiogram (ECG) Interpretation

Systematic 7-step analysis:
1. **Rate & Rhythm**:
   - Regular rhythm: $300 / \text{number of large squares between R-R}$.
   - Sinus rhythm criteria: Upright P wave in lead II, inverted in aVR, followed consistently by a QRS complex.
2. **Electrical Axis**:
   - Lead I positive, Lead aVF positive -> Normal axis ($-30^\circ\text{ to }+90^\circ$).
   - Lead I positive, Lead aVF negative, Lead II negative -> Left axis deviation (LAD).
   - Lead I negative, Lead aVF positive -> Right axis deviation (RAD).
3. **P Wave & PR Interval**:
   - PR interval normal: **$120–200\text{ ms}$** (3 to 5 small squares). Prolongation $> 200\text{ ms}$ defines 1st degree AV block.
4. **QRS Complex**:
   - Normal duration: **$< 120\text{ ms}$**.
   - Broad QRS ($\ge 120\text{ ms}$): Left Bundle Branch Block (LBBB: broad notched R waves in I, aVL, V5-V6, deep S in V1-V2) or Right Bundle Branch Block (RBBB: rsR' "rabbit ears" in V1-V2, wide slurred S in I and V6).
5. **ST Segment & T Wave (Ischemia & Infarction Localization)**:
   - **V1–V2**: Anteroseptal (LAD septal perforators).
   - **V3–V4**: Anterior / Apical (LAD diagonal / main stem).
   - **V5–V6, I, aVL**: Lateral wall (Left Circumflex - LCx or LAD diagonal).
   - **II, III, aVF**: Inferior wall (Right Coronary Artery - RCA or dominant LCx).
   - **Reciprocal ST depressions**: Opposite leads show mirror-image ST depressions (e.g. ST depression in I and aVL during inferior STEMI).
6. **QT Interval**:
   - Corrected QT (QTc) calculated via Bazett formula: $\text{QTc} = \frac{\text{QT}}{\sqrt{\text{RR}}}$.
   - Normal: $< 440\text{ ms}$ in men, $< 460\text{ ms}$ in women. Prolongation $> 500\text{ ms}$ significantly increases risk of polymorphic ventricular tachycardia (**Torsades de Pointes**).

---

## 4. Heart Failure & Guideline-Directed Medical Therapy (GDMT)

Heart failure is categorized by Left Ventricular Ejection Fraction (LVEF):
- **HFrEF** (Reduced EF): $\text{LVEF} \le 40\%$.
- **HFmrEF** (Mildly Reduced EF): $\text{LVEF } 41–49\%$.
- **HFpEF** (Preserved EF): $\text{LVEF} \ge 50\%$ with structural/diastolic dysfunction and elevated **NT-proBNP**.

### The "Four Pillars" of HFrEF Mortality Reduction:
1. **ARNI (Angiotensin Receptor-Neprilysin Inhibitor)** (*sacubitril/valsartan*) or ACEi.
2. **Beta-Blocker with proven HF benefit** (*bisoprolol, carvedilol, metoprolol succinate*).
3. **Mineralocorticoid Receptor Antagonist (MRA)** (*spironolactone or eplerenone*).
4. **SGLT2 Inhibitor** (*dapagliflozin or empagliflozin*): Reduces cardiovascular death and HF hospitalization regardless of diabetic status.
*(Loop diuretics like furosemide are added strictly for symptomatic fluid congestion).*

---

## 5. Cardiac Surgery & Interventional Procedures

### A. Percutaneous Coronary Intervention (PCI):
- Access: Transradial artery approach (reduces bleeding complications compared to transfemoral).
- Drug-Eluting Stents (DES): Stents coated with antiproliferative agents (*everolimus, zotarolimus*) to prevent in-stent neointimal hyperplasia (restenosis).
- **Dual Antiplatelet Therapy (DAPT)**: Mandatory combination of Aspirin 100mg + P2Y12 inhibitor (*ticagrelor, prasugrel, or clopidogrel*) for 6 to 12 months post-PCI to prevent acute stent thrombosis.

### B. Coronary Artery Bypass Grafting (CABG):
- **Indications**: Left main coronary artery stenosis $> 50\%$, three-vessel CAD with high anatomic complexity (SYNTAX score $> 22$), or two-vessel CAD with proximal LAD stenosis in diabetic patients.
- **Conduits**:
  - **LIMA (Left Internal Mammary Artery) to LAD**: The gold standard conduit with $> 90\%$ 10-year patency rate.
  - **Saphenous Vein Grafts (SVG)** or **Radial Artery Grafts**: Secondary conduits anastomosed from the aorta to target vessels (RCA, LCx / obtuse marginal).
- **Surgical Modalities**: On-Pump (utilizing Cardiopulmonary Bypass / Heart-Lung Machine with cardioplegic arrest) vs. Off-Pump (OPCAB - beating heart surgery).

### C. Heart Valve Replacement & Repair:
- **Aortic Stenosis**: TAVI (Transcatheter Aortic Valve Implantation via femoral artery) vs. Surgical Aortic Valve Replacement (SAVR).
- **Mechanical vs. Biological Prosthetic Valves**:
  - Mechanical: Highly durable (> 25 years), but requires lifelong anticoagulation with Vitamin K antagonists (Warfarin) with strict target INR (2.5–3.5 depending on position).
  - Biological (Bovine/Porcine pericardium): Low thrombogenicity (aspirin only), but subject to structural valve deterioration over 10–15 years.

---

<a name="code-review"></a>
# 📦 SKILL: code-review
*Domain:* **Software Engineering**

---
name: code-review
description: >-
  Use this skill to audit and review Bash and PowerShell scripts for security, performance, and best practices.
---
# Script Code Review Checklist

When reviewing code, evaluate it against the following criteria:

## For PowerShell (Windows)
- **Security**: Avoid `Invoke-Expression`. Validate input parameters. Ensure secure handling of credentials (use `PSCredential` instead of plain text).
- **Style**: Use full cmdlet names instead of aliases in scripts (e.g., `Get-ChildItem` instead of `ls` or `dir`). Use `PascalCase` for variables.
- **Robustness**: Are errors caught using `try/catch`? Is `[CmdletBinding()]` used for advanced functions?

## For Bash (Linux)
- **Security**: Avoid `eval`. Always quote variables to prevent word splitting and globbing issues (e.g., `"$VAR"`).
- **Robustness**: Are `set -e`, `set -u`, and `set -o pipefail` used? 
- **Portability**: Is the shebang correct (`#!/bin/bash` or `#!/usr/bin/env bash`)? Are there bashisms if the user requested POSIX compliance?

Provide a structured report with [High], [Medium], and [Low] priority fixes.

---

<a name="compliance-anti-sanctions-aml"></a>
# 📦 SKILL: compliance-anti-sanctions-aml
*Domain:* **Compliance & Sanctions**

---
name: compliance-anti-sanctions-aml
description: >-
  International sanctions compliance (EU Council Regulations 833/2014 & 269/2014, US OFAC SDN/SSI lists, UK OFSI, 50-Percent Rule), Dual-Use export controls (Regulation 2021/821, EAR), Anti-Money Laundering and Counter-Terrorist Financing (AMLD5, AMLD6, AMLA, KYC/CDD, UBO registers), and cryptocurrency regulatory compliance (MiCA, CASP licensing, Travel Rule Regulation 2023/1113).
---
# Sanctions Compliance, Anti-Money Laundering (AML/CFT) & Crypto Regulation

An authoritative operational and regulatory reference for Chief Compliance Officers (CCO), Money Laundering Reporting Officers (MLRO), international trade lawyers, and financial institution risk managers.

---

## 1. Global Sanctions Regimes & Enforcement Architecture

Entities engaging in international trade, banking, and technology transfers operate under the jurisdiction of three overlapping sanctions authorities:

```
               [ Global Sanctions & Trade Enforcement ]
                                  |
     +----------------------------+----------------------------+
     |                            |                            |
[ European Union (EU) ]     [ United States (OFAC/BIS) ]   [ United Kingdom (OFSI) ]
 - Reg 833/2014 (Sectoral)    - SDN List (Blocked Persons)   - Sanctions and Anti-Money
 - Reg 269/2014 (Individual)  - Sectoral Sanctions (SSI)       Laundering Act 2018
 - AMLA Enforcement Hub       - Secondary Sanctions          - Consolidated List
```

### A. European Union Sanctions Architecture:
- **Council Regulation (EU) No 269/2014**: Asset freezes and prohibition on making funds or economic resources available directly or indirectly to listed individuals and entities.
- **Council Regulation (EU) No 833/2014**: Comprehensive sectoral restrictions:
  - Banking & financial transactions: Disconnection from SWIFT, prohibition on accepting deposits over 100,000 EUR from Russian nationals, prohibitions on transactions with the Central Bank of Russia.
  - Technology, industrial goods, and software bans: Dual-use goods, semiconductors, advanced electronics, enterprise management software (ERP, CRM, CAD).
  - Anti-Circumvention Rule (Article 12): Strict prohibition against knowingly and intentionally participating in activities the object or effect of which is to circumvent the prohibitions.
  - Mandatory "No-Russia" Clause (Article 12g): Exporters must contractually prohibit re-exportation of sensitive goods to Russia and include strict liquidated damages remedies.

### B. United States Sanctions (OFAC - Department of the Treasury):
- **Specially Designated Nationals (*SDN List*)**: All property and interests in property within US jurisdiction are blocked; US persons are prohibited from engaging in any transactions.
- **Secondary Sanctions**: Foreign financial institutions (FFI) and foreign companies risk being designated on the SDN list or cut off from the US correspondent banking system if they facilitate significant transactions with blocked persons or designated military-industrial sectors (Executive Order 14114).
- **Executive Orders & Sectoral Determinations**: Broad restrictions covering maritime transport, oil price caps ($60/barrel), mining, and technology.

---

## 2. The 50-Percent Rule & Corporate Control Test

A company that is not explicitly named on a sanctions list may nonetheless be legally blocked by operation of law:

### A. The OFAC 50-Percent Rule:
- Any entity owned in the aggregate, **directly or indirectly, 50 percent or more by one or more blocked persons** is considered blocked, regardless of whether the entity itself is designated by name.
- Ownership is **cumulative**: If Blocked Person A owns 25% and Blocked Person B owns 25%, the entity is 50% owned and automatically blocked.

### B. The European Union Ownership & Control Test:
Under EU Council guidelines and CJEU jurisprudence:
1. **Ownership Criterion**: 50% or more of the proprietary rights or majority interest held by a listed person.
2. **Control Criterion (Factual Control)**: Even if ownership is under 50%, an entity is deemed controlled and blocked if a listed person has:
   - The right or power to appoint or remove a majority of the board of directors or executive management.
   - The right to exercise a dominant influence pursuant to a contract or constitutional provision.
   - The power to manage or direct the company's financial or operational affairs (e.g. through nominee shareholders, close family relatives acting as proxies, or shadow directing).

---

## 3. Dual-Use Export Controls & Technology Transfer

Governed in the EU by **Regulation (EU) 2021/821** and in the US by the **Export Administration Regulations (EAR)**:

- **Dual-Use Goods Definition**: Items, software, and technology that can be used for both civil and military purposes, including items that can assist in the design, development, production, or use of nuclear, chemical, or biological weapons.
- **Classification & Control Lists**:
  - Export Control Classification Number (**ECCN**) under the Commerce Control List (CCL) or Annex I of EU Regulation 2021/821 (Category 0 to 9: Nuclear, Materials, Electronics, Computers, Telecommunications, Information Security, Sensors, Navigation, Aerospace).
- **Catch-All Clause**: Mandatory export authorization even for non-listed items if the exporter has been informed by authorities or has reason to know that the items may be intended for military end-use or weapons of mass destruction.
- **Know Your Customer (KYC) in Supply Chains**: Verification of ultimate consignee, end-use statements (EUS), and anti-diversion screening against denied persons lists.

---

## 4. Anti-Money Laundering & Counter-Terrorist Financing (AML/CFT)

Operating under the **Financial Action Task Force (FATF)** recommendations and the **EU AML Package (AMLD5, AMLD6 & AMLA)**:

### A. Customer Due Diligence (CDD) Protocols:
- **Simplified Due Diligence (SDD)**: Low-risk domestic public entities, listed companies.
- **Standard Due Diligence (CDD)**:
  - Identity verification of physical persons (government ID, proof of address).
  - Commercial entities: Verification of legal form, registration extract, articles of association, active management.
  - Identification of the **Ultimate Beneficial Owner (UBO)**: Every physical person who ultimately owns or controls more than **25%** of the shares, voting rights, or ownership interest in the legal entity.
- **Enhanced Due Diligence (EDD)**:
  - Mandatory for: (1) High-risk third countries on FATF black/grey lists, (2) Politically Exposed Persons (**PEP**) and their family members / close associates, (3) Cross-border correspondent banking relationships, (4) Complex or unusually large transactions with no clear economic purpose.
  - Requires: Source of Wealth (SoW) and Source of Funds (SoF) documentary evidence, senior management approval for onboarding, intensified ongoing monitoring.

### B. Obliged Entities & Reporting Obligations:
- Banks, payment institutions, crypto-asset providers, auditors, tax advisors, real estate brokers, and lawyers.
- Mandatory filing of **Suspicious Transaction Reports (STR / SAR)** to the national Financial Intelligence Unit (**FIU** / *FAU in Czechia*, *Rosfinmonitoring in RF*).
- **Prohibition of Tipping-Off**: Obliged entities and their employees are strictly prohibited from disclosing to the customer or third parties that a report has been filed or that a money laundering investigation is underway.

---

## 5. Cryptocurrency Regulation: MiCA & The EU Travel Rule

The European Union has established the world's first comprehensive regulatory framework for crypto-assets:

### A. Markets in Crypto-Assets Regulation (MiCA - Regulation (EU) 2023/1114):
- **Classification of Crypto-Assets**:
  1. *Asset-Referenced Tokens (ART)*: Tokens that purport to maintain a stable value by referencing multiple currencies, commodities, or other crypto-assets. Strict reserve and capital requirements.
  2. *Electronic Money Tokens (EMT)*: Stablecoins pegged to a single official currency (e.g. EUR, USD). Must be issued by authorized credit or electronic money institutions.
  3. *Utility Tokens & Other Crypto-Assets*: Require publication of an approved **Crypto-Asset White Paper**.
- **Crypto-Asset Service Providers (CASP)**:
  - Entities providing custody, exchange of crypto for fiat or other crypto, operation of trading platforms, and execution of orders.
  - Mandatory licensing and authorization by national competent authorities (e.g. ČNB in Czechia, BaFin in Germany, AMF in France) with EU-wide passporting rights.
  - Strict prudential requirements: Capital reserves (50k to 150k EUR), governance standards, segregation of client assets, IT security (DORA compliance).

### B. The EU Crypto Travel Rule (Regulation (EU) 2023/1113):
- Extends the traditional FATF wire transfer rules to transfers of crypto-assets.
- **Mandatory Information Transmission**: When executing a crypto transfer, the sending CASP must collect, verify, and immediately transmit to the receiving CASP:
  - Name of the originator (sender), originator's crypto wallet address, account number, physical address, national identity number or date/place of birth.
  - Name of the beneficiary (recipient) and beneficiary's wallet address.
- **Self-Hosted Wallets (Unhosted Wallets)**: For transfers exceeding **1,000 EUR** to/from unhosted wallets, CASPs are mandated to verify whether the wallet is effectively owned or controlled by the customer.

---

<a name="cyber-defense-pentest"></a>
# 📦 SKILL: cyber-defense-pentest
*Domain:* **Cybersecurity**

---
name: cyber-defense-pentest
description: >-
  Offensive security, penetration testing methodologies, MITRE ATT&CK framework, OWASP Top 10 web vulnerabilities, network reconnaissance (Nmap, Nuclei), privilege escalation analysis (Linux SUID, Windows Potato), active threat hunting, and incident response.
---
# Cyber Defense, Threat Hunting & Penetration Testing

An advanced operational security manual covering adversarial techniques, threat hunting, vulnerability assessments, penetration testing methodologies, and rapid incident response.

---

## 1. Adversarial Methodology & MITRE ATT&CK Framework

Security defense requires mastering how adversaries operate across the **Cyber Kill Chain**:
1. **Reconnaissance**: Passive OSINT & active perimeter port scanning.
2. **Initial Access**: Exploiting public-facing web applications, phishing, exposed credentials.
3. **Execution**: Running unauthorized scripts, web shells, living-off-the-land binaries (LOLBins).
4. **Persistence**: Creating malicious cron jobs, systemd services, registry Run keys, scheduled tasks.
5. **Privilege Escalation**: Exploiting misconfigured SUID binaries, unquoted service paths, kernel vulnerabilities.
6. **Defense Evasion**: Disabling security services, clearing bash history / event logs, timestomping.
7. **Credential Access**: Dumping LSASS, reading `/etc/shadow`, extracting unencrypted tokens/passwords.
8. **Lateral Movement**: SSH pivoting, Pass-the-Hash, RDP hijacking, WinRM remoting.
9. **Exfiltration & Impact**: Compressing, encrypting, and staging data via encrypted channels.

---

## 2. Network Reconnaissance & Vulnerability Assessment

### Nmap Advanced Operational Scanning:
```bash
# Stealth TCP SYN Scan with Service Version Detection and OS Fingerprinting
nmap -sS -sV -O -p- --min-rate 1000 -T4 -oA scan_results <TARGET_IP>

# Vulnerability Scanning via Nmap Scripting Engine (NSE)
nmap --script "vuln and safe" -p 80,443,22,3389,8080 <TARGET_IP>

# Fast Masscan for large CIDR blocks
masscan -p1-65535 <SUBNET/24> --rate=5000 -e eth0
```

### Automated Vulnerability & Web Scanning:
- **Nuclei**: Fast template-based vulnerability scanning targeting known CVEs, misconfigurations, and exposed secrets:
  ```bash
  nuclei -u https://example.com -severity critical,high -silent
  ```
- **WPScan**: Scanning WordPress installations for vulnerable plugins, themes, and user enumeration:
  ```bash
  wpscan --url https://example.com --enumerate vp,vt,u --api-token <WPSCAN_TOKEN>
  ```
- **SSRF Defense (Cloud Metadata Protection)**:
  - Block access from web server containers to cloud instance metadata (`169.254.169.254`).
  - Enforce IMDSv2 (Session token requirement) in AWS/OCI:
    ```bash
    iptables -A OUTPUT -m owner ! --uid-owner root -d 169.254.169.254 -j DROP
    ```

---

## 3. Privilege Escalation Vectors & Audit (PrivEsc)

### Linux Privilege Escalation Vectors:
1. **Misconfigured Sudo Permissions (`sudo -l`)**:
   - Binaries permitted without password that allow shell escape (e.g. `vim`, `find`, `less`, `awk`, `python`, `nmap` via GTFOBins).
2. **SUID / SGID Executables**:
   ```bash
   # Search for dangerous SUID binaries owned by root
   find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;
   ```
3. **Writable Cron Jobs / Systemd Services**:
   - World-writable scripts executed periodically by root.
4. **Weak File Permissions**:
   - Write access to `/etc/passwd` (generating a new root user) or readable `/etc/shadow`.
5. **Kernel Exploits**: Dirty Pipe (CVE-2022-0847), Dirty COW, overlayfs vulnerabilities. Check kernel version via `uname -r`.

### Windows Privilege Escalation Vectors:
1. **Unquoted Service Paths**:
   - Service executable paths containing spaces without quotation marks (e.g. `C:\Program Files\App Dir\service.exe`), allowing dropping malicious binaries earlier in the path.
2. **Token Impersonation & Potato Exploits**:
   - Accounts holding `SeImpersonatePrivilege` or `SeAssignPrimaryTokenPrivilege` (e.g. IIS / `LOCAL SERVICE`) can elevate to `SYSTEM` via SweetPotato / GodPotato.
3. **AlwaysInstallElevated**:
   - Registry keys `AlwaysInstallElevated = 1` allowing standard users to install `.msi` packages running as `SYSTEM`.

---

## 4. Threat Hunting & Indicator of Compromise (IoC) Detection

### Quick Linux Triage Checklist during Active Attack:
```bash
# 1. Check currently logged in users and terminal sessions
w
who -a
last -n 20

# 2. Inspect active network listening sockets and external connections
ss -tulpn
ss -tupn | grep ESTAB

# 3. List running processes by CPU/Memory with full command paths
ps auxf --sort=-%cpu | head -n 30

# 4. Search for recently modified files in system directories within the last 24h
find /etc /bin /sbin /usr/bin /usr/sbin /tmp /dev/shm -mtime -1 -type f -ls

# 5. Check cron schedules across all users
for user in $(cut -f1 -d: /etc/passwd); do crontab -u $user -l 2>/dev/null; done
ls -la /etc/cron* /etc/systemd/system/

# 6. Audit rootkits using automated scanning
rkhunter --check --sk
chkrootkit
```

---

## 5. Security Incident Response Protocol (CSIRT / DFIR)

When an unauthorized intrusion or breach is confirmed:
1. **Containment**:
   - Isolate the host from the network immediately (`iptables -P INPUT DROP; iptables -P OUTPUT DROP` or disconnect vNIC).
   - **Do NOT reboot or power off immediately** if memory analysis is required (RAM holds encryption keys, running malware, and unwritten connections).
2. **Evidence Preservation**:
   - Capture volatile memory (RAM dump via `LiME` on Linux or `DumpIt` / `FTK Imager` on Windows).
   - Create cryptographic disk image hash (SHA-256) of virtual disks.
3. **Eradication**:
   - Identify entry vector (vulnerable web plugin, compromised SSH key, stolen credential).
   - Rebuild compromised hosts from pristine golden images / IaC rather than trying to manually "clean" malware.
4. **Post-Incident Remediation**:
   - Rotate all SSH keys, database passwords, API tokens, and service credentials.

---

<a name="czech-accounting-tax"></a>
# 📦 SKILL: czech-accounting-tax
*Domain:* **Czech Accounting & Tax**

---
name: czech-accounting-tax
description: >-
  Operational workflows and advisory for Czech accounting, taxation (DPFO, DPPO, DPH), social and health insurance (ČSSZ, VZP/OZP), flat-rate regimes (paušální daň and paušální výdaje), payroll (DPP, DPČ, HPP), dividends/profit distribution, and mandatory electronic filings (MOJE daně, DIS+, ISDS datová schránka) for OSVČ and s.r.o.
---
# Czech Accounting, Taxation & Reporting (Český účetní a daňový systém)

A complete operational guide for entrepreneurs, accountants, and consultants operating in the Czech Republic under Czech statutory law.

---

## 1. Statutory Framework & Primary Legislation

All accounting and taxation in the Czech Republic is governed by the following key statutes:
- **Act on Accounting** (*Zákon č. 563/1991 Sb., o účetnictví*): Fundamental principles, double-entry bookkeeping, chart of accounts, financial statements.
- **Czech Accounting Standards** (*České účetní standardy - ČÚS*): Operational rules for individual balance sheet and P&L accounts.
- **Income Taxes Act** (*Zákon č. 586/1992 Sb., o daních z příjmů - ZDP*): Personal Income Tax (DPFO), Corporate Income Tax (DPPO), tax allowances, depreciation.
- **Value Added Tax Act** (*Zákon č. 235/2004 Sb., o dani z přidané hodnoty - ZDPH*): Domestic and cross-border VAT, identified persons, control statements.
- **Tax Code** (*Zákon č. 280/2009 Sb., Daňový řád - DŘ*): Procedural tax rules, audits, penalties, deadlines, electronic filing obligations.
- **Social Security Acts** (*Zákon č. 589/1992 Sb.* & *Zákon č. 155/1995 Sb.*): Social insurance premiums and pension coverage.
- **Health Insurance Act** (*Zákon č. 592/1992 Sb.*): Public health insurance financing and assessment bases.

---

## 2. OSVČ (Sole Proprietor / Fyzická osoba) Tax Regimes

Sole proprietors in the Czech Republic can choose among four accounting/tax methods based on turnover and expense ratio:

### A. Paušální daň (Flat-rate Tax Regime - § 7a ZDP)
Combines income tax, social insurance, and health insurance into a single monthly payment sent directly to the local Financial Office (*Finanční úřad*).
- **No annual tax return** (*Daňové přiznání*) or insurance overviews (*Přehledy ČSSZ/ZP*) required if conditions are met throughout the year.
- **Conditions**: Turnover under 2,000,000 CZK/year, not registered as a standard VAT payer (can be *Identifikovaná osoba*), no employment income subject to advance tax (only DPP up to 10k or withholding tax allowed).
- **Entry deadline**: Must notify the tax authority by **January 10** of the tax year (or upon trade registration).
- **Three Tiers (Pásma)**:
  - **Band 1** (Turnover up to 1M CZK regardless of activity; up to 1.5M CZK if 60%+ flat expense eligible; up to 2M CZK if 80% craft trade eligible).
  - **Band 2** (Turnover up to 1.5M CZK regardless; up to 2M CZK if 60%+ flat expense eligible).
  - **Band 3** (Turnover up to 2M CZK for all other eligible categories).

### B. Výdajový paušál (Lump-sum Flat Expenses - § 7 odst. 7 ZDP)
Revenue is recorded, but actual expense receipts are not tracked. Statutory flat expenses are deducted from gross income:
- **80% flat expenses**: Craft trades (*Řemeslné živnosti*) and agricultural production (capped at max **1,600,000 CZK** expense).
- **60% flat expenses**: General, non-craft licensed and free trades (*Volné, vázané a koncesované živnosti*) (capped at max **1,200,000 CZK** expense).
- **40% flat expenses**: Freelance, independent professions, copyright, software IP without trade license (*Autorské honoráře, svobodná povolání*) (capped at max **800,000 CZK**).
- **30% flat expenses**: Rental income under § 9 ZDP (capped at max **600,000 CZK**).
*Full annual DPFO tax return and ČSSZ/ZP overviews must be filed.*

### C. Daňová evidence (Tax Records - § 7b ZDP)
Used when actual expenses exceed lump-sum percentages or turnover is high:
- Tracks actual cash receipts, cash expenses, bank movements, receivables (*pohledávky*), liabilities (*závazky*), and business assets (*obchodní majetek*).
- Cash-based principle: Revenue and expenses are recognized when money is paid/received.

### D. Podvojné účetnictví (Double-entry Bookkeeping for OSVČ)
Mandatory for OSVČ only if annual turnover exceeds **25,000,000 CZK** in the preceding calendar year, or voluntarily.

---

## 3. Corporate Taxation for s.r.o. (DPPO)

A Czech limited liability company (*společnost s ručením omezeným - s.r.o.*) is legally required to keep double-entry bookkeeping (*Podvojné účetnictví*).

### Corporate Income Tax Rate
- **21%** (increased from 19% starting tax year 2024 under the government consolidation package).

### Tax Base Transformation:
$$\text{Základ daně} = \text{Výsledek hospodaření před zdaněním} + \text{Daňově neuznatelné náklady} - \text{Nedaňové výnosy} - \text{Odpisy/Položky snižující}$$

- **Non-deductible expenses (§ 25 ZDP)**:
  - Representation/hospitality costs (*reprezentace, pohoštění* - Account 513).
  - Gifts and sponsorships (*dary* - Account 543, deductible only under strict charitable limits § 20 odst. 8).
  - Contractual and statutory late penalties (*smluvní pokuty* unless paid, or non-tax administrative fines).
  - Expenses lacking direct causal nexus to income generation (*výdaje bez přímé souvislosti s dosažením příjmů*).
  - Executive/director bonuses without formal approval or beyond contractual authorization.
- **Tax-deductible expenses (§ 24 ZDP)**:
  - Office rental, operational overhead, server costs, software subscriptions.
  - Employee wages and compulsory social/health employer contributions.
  - Tax depreciation of fixed assets (*daňové odpisy*).
  - Fuel and travel allowances (*cestovní náhrady*) under statutory decrees.

### Asset Depreciation (Odpisy majetku)
- **Tangible assets (*Hmotný majetek*)**: Entry price over **80,000 CZK** and useful life > 1 year.
- **6 Depreciation Groups (§ 30 ZDP)**:
  - **Group 1 (3 years)**: Computers, IT hardware, phones, office tech.
  - **Group 2 (5 years)**: Passenger cars, trucks, standard machinery.
  - **Group 3 (10 years)**: Heavy machinery, turbines, metal structures.
  - **Group 4 (20 years)**: Lightweight buildings, wooden construction.
  - **Group 5 (30 years)**: Standard residential and office buildings.
  - **Group 6 (50 years)**: Historical buildings, administrative complexes.
- Methods: Straight-line (*rovnoměrný*) or Accelerated (*zrychlený*). Once chosen for an asset, the method cannot be changed.

---

## 4. Personal Income Tax (DPFO) & Tax Credits

### Progressive Tax Rates:
- **15%**: Applied to the tax base up to **36 times the national average monthly wage** (*průměrná mzda*).
- **23%**: Applied to the portion of taxable income exceeding 36 times the average wage.

### Tax Allowances and Credits (Slevy na dani - § 35ba, § 35c ZDP):
- **Basic Taxpayer Relief (*Základní sleva na poplatníka*)**: **30,840 CZK / year** (claimed in full by all taxpayers with taxable income).
- **Spouse Relief (*Sleva na manžela/manželku*)**: **24,840 CZK / year** (only if spouse income < 68,000 CZK/year AND caring for a child under 3 years old). Double if ZTP/P.
- **Child Tax Credit (*Daňové zvýhodnění na dítě*)**:
  - 1st child: **15,204 CZK / year**
  - 2nd child: **22,320 CZK / year**
  - 3rd and subsequent children: **27,840 CZK / year**
  *If child credit exceeds tax liability, the difference is paid out as a cash tax bonus (*Daňový bonus*) up to statutory limits.*

---

## 5. Compulsory Social and Health Insurance

### OSVČ (Sole Proprietors):
- **ČSSZ (Czech Social Security Administration)**:
  - Principal activity (*Hlavní činnost*): Compulsory minimum monthly advance base. Minimum advances adjust annually based on average wage growth.
  - Secondary activity (*Vedlejší činnost* - e.g. employed, student, pensioner): Mandatory only if net annual profit exceeds the decisive threshold (*rozhodná částka*).
  - Voluntary Sickness Insurance (*Nemocenské pojištění*): Separate voluntary opt-in required to receive maternity or sickness benefits.
- **Public Health Insurance (VZP, OZP, VoZP, ČPZP, ZP MV ČR)**:
  - Standard rate: **13.5%** of the assessment base (which is 50% of net tax profit).
  - Minimum monthly advance is strictly mandatory for *hlavní činnost*, regardless of whether profit or loss is recorded.

### Employment Payroll Contributions (HPP - Hlavní pracovní poměr):
- **Employer pays**:
  - Social security: **24.8%** (21.5% pension, 2.1% sickness, 1.2% state employment policy).
  - Health insurance: **9.0%**.
  - Total employer surcharge: **33.8%** on top of gross wage (*hrubá mzda*).
- **Employee pays (withheld by employer)**:
  - Social security: **7.1%** (including 0.6% employee sickness insurance).
  - Health insurance: **4.5%**.
  - Personal income tax advance (*záloha na daň*): 15% / 23% after applying signed tax declaration (*Prohlášení poplatníka / Růžový formulář*).

---

## 6. Flexible Employment Contracts (DPP & DPČ)

### Dohoda o provedení práce (DPP):
- Capped at **300 hours per calendar year** per single employer.
- Mandatory monthly electronic reporting to ČSSZ for all active DPP agreements (*Výkaz DPP*).
- Threshold for social and health insurance deductions applies; amounts below the threshold are exempt from social/health insurance and taxed via 15% withholding tax (*srážková daň*).

### Dohoda o pracovní činnosti (DPČ):
- Working time cannot exceed half of the standard weekly working hours (maximum 20 hours/week on average).
- Insurance applies if monthly remuneration reaches or exceeds the statutory threshold (*rozhodná částka pro účast na nemocenském pojištění* - currently 4,000 CZK).

---

## 7. Profit Distribution & Dividends in an s.r.o.

### Legal Procedure:
1. Approval of annual financial statements (*Řádná účetní závěrka*) by the General Meeting (*Valná hromada*) within **6 months** of the balance sheet date.
2. **Insolvency Test (§ 40 ZOK)**:
   > The company must not distribute profits, advances on profit, or equity funds if the distribution would cause the company's insolvency or bankruptcy.
3. Balance Sheet Test: Profit distribution cannot exceed the net profit of the current period + retained earnings - accumulated losses - non-distributable reserve funds.
4. **Withholding Tax (*Srážková daň*)**:
   - Standard rate: **15%** withheld at source and remitted to the tax office by the end of the month following the distribution decision.
   - EU Parent-Subsidiary Directive: 0% withholding tax if the parent company owns at least 10% of the subsidiary continuously for at least 12 months.

---

## 8. Electronic Filing & Official Portals

Electronic filing is **mandatory by law** for all Czech legal entities and registered OSVČ. Paper submissions are legally inadmissible:
- **Datová schránka (ISDS - Zákon č. 300/2008 Sb.)**:
  - Official state digital mailbox system. Mandatory for all OSVČ and companies.
  - Submissions sent via ISDS have the legal status of an authorized signature.
- **Portál MOJE daně (DIS+)**:
  - Direct electronic filing of DPFO, DPPO, DPH, Kontrolní hlášení, and Souhrnné hlášení.
  - Real-time access to tax balances, overpayments (*přeplatky*), and underpayments.
- **ePortál ČSSZ**:
  - Filing of *Přehled o příjmech a výdajích*, registration of employees, monthly DPP overviews.
- **Health Insurance Portals**:
  - VZP Point / Vitakarta OZP: Annual *Přehled*, employee registration (*Hromadné oznámení zaměstnavatele*).

---

<a name="czech-business-law"></a>
# 📦 SKILL: czech-business-law
*Domain:* **Czech Business Law**

---
name: czech-business-law
description: >-
  Legal reference and procedures for Czech corporate law (ZOK - s.r.o. governance, jednatel duties, valná hromada, dividend distributions), Civil Code (NOZ - contracts, penalties, statute of limitations), Trade Licensing Act (Živnostenský zákon), Labour Code (Zákoník práce, Schwarzsystém risks), Commercial Register, and Beneficial Ownership (ESM).
---
# Czech Business Law & Corporate Compliance (České obchodní právo)

A comprehensive legal and operational guide for managing commercial entities, concluding contracts, navigating corporate governance, and mitigating regulatory liabilities under the Czech legal system.

---

## 1. Statutory Architecture & Hierarchy of Czech Law

Legal norms in the Czech Republic adhere to a strict statutory hierarchy:
1. **Constitutional Order**: *Ústava České republiky* (Act No. 1/1993 Coll.) and the *Listina základních práv a svobod* (Charter of Fundamental Rights and Basic Freedoms).
2. **European Union Law**: Primary and secondary EU law (EU Regulations apply directly; EU Directives take precedence once transposed or when possessing direct vertical effect).
3. **Statutes (*Zákony*)**: Enacted by Parliament and promulgated in the Collection of Laws (*Sbírka zákonů - Sb.*).
4. **Subordinate Regulations**: Government Decrees (*Nařízení vlády*) and Ministerial Ordinances (*Vyhlášky ministerstev*).
5. **Case Law Precedents**: Jurisprudence of the Supreme Court (*Nejvyšší soud - NS*) and Supreme Administrative Court (*Nejvyšší správní soud - NSS*).

---

## 2. Czech Corporate Law: The s.r.o. (ZOK - Zákon č. 90/2012 Sb.)

The Limited Liability Company (*Společnost s ručením omezeným - s.r.o.*) is governed by the **Act on Business Corporations** (*Zákon o obchodních korporacích - ZOK*).

### A. Formation and Capital Requirements:
- **Founding Document**: Memorandum of Association (*Společenská smlouva*) or Deed of Foundation (*Zakladatelská listina* for a single founder) must be executed in the form of a **Czech Notarial Deed (*Notářský zápis*)**.
- **Registered Capital (*Základní kapitál*)**: Minimum statutory contribution is **1 CZK per share**, though practical commercial banking standards generally favor 10,000 CZK to 200,000 CZK.
- **Shares (*Podíly*)**: Can be divided into multiple classes (basic share, priority share with preferred profit rights, fixed-yield share). Can be embodied in an unregistered certificated share (*Kmenový list*).

### B. The Statutory Executive (*Jednatel*) - Governance & Fiduciary Duties:
The *Jednatel* represents the company in all corporate, commercial, and judicial matters:
- **Duty of Due Managerial Care (*Péče řádného hospodáře* - §§ 51–53 ZOK)**:
  - The executive must act with necessary loyalty, knowledge, diligence, and care.
  - **Business Judgment Rule (*Pravidlo podnikatelského úsudku* - § 51 odst. 1 ZOK)**: An executive acts with due care if they could in good faith reasonably assume, when making a business decision, that they were acting on an informed basis and in the defensible interest of the corporation.
  - **Burden of Proof (*Důkazní břemeno*)**: In litigation regarding alleged damages, the burden of proof rests on the executive to prove that they acted with due managerial care (§ 52 odst. 2 ZOK).
- **Executive Service Contract (*Smlouva o výkonu funkce* - § 59 ZOK)**:
  - Must be in **written form** and expressly approved by the General Meeting (*Valná hromada*).
  - Must enumerate all components of remuneration, bonuses, company cars, pension benefits, and severance. If remuneration is not agreed in writing or approved by the general meeting, the function is legally deemed performed **free of charge (*bezúplatně*)**.
- **Non-Compete Covenant (*Zákaz konkurence* - § 199 ZOK)**:
  - Unless explicitly waived by the shareholders, an executive cannot engage in competing business, serve as an executive/board member in competing entities, or act as an intermediary for third parties in the company's business field.
- **Conflict of Interest Notification (§ 54 ZOK)**:
  - Must formally notify the General Meeting and supervisory board in writing before entering into any contract between the company and the executive or their close relatives.

### C. General Meeting (*Valná hromada*) & Decision-Making:
- Supreme body of the s.r.o., composed of all shareholders (*společníci*).
- **Mandatory Annual Meeting**: Must convene at least once every financial year to review and approve the financial statements within **6 months** of the balance sheet date (§ 181 odst. 2 ZOK).
- **Per Rollam Voting (§ 175 ZOK)**: Written/electronic voting outside a physical meeting, provided the company's Memorandum of Association allows it.
- **Insolvency Test (§ 40 ZOK)**:
  > The executive is strictly prohibited from paying out profits, advances on profit, or equity funds if doing so would cause the company's insolvency under the Insolvency Act. Violating this rule exposes the executive to personal liability with their entire personal assets.

---

## 3. Civil Code & Commercial Contracts (NOZ - Zákon č. 89/2012 Sb.)

The Czech Civil Code (*Občanský zákoník - NOZ*) governs all contractual relationships:

### Core Contractual Types:
1. **Contract for Work (*Smlouva o dílo* - §§ 2586–2635 NOZ)**:
   - Primary contract for software development, IT services, construction, and engineering.
   - Crucial terms: Definition of the work (*dílo*), completion deadline, handover and acceptance protocol (*předávací protokol*), price determination (fixed, estimated with cap, or hourly rate), warranty and defect liability (*vady díla*).
2. **Purchase Agreement (*Kupní smlouva* - §§ 2079–2183 NOZ)**:
   - Governs sale of goods, transfer of title, retention of title clause (*výhrada vlastnictví*), and inspection requirements.
3. **Agency / Mandate Contract (*Příkazní smlouva* - § 2430 NOZ) & Innominate Contracts (§ 1746 odst. 2)**:
   - General framework for ongoing management, advisory, and outsourcing services.
4. **Commercial Lease (*Nájem prostor sloužících podnikání* - §§ 2302–2315 NOZ)**:
   - Specific statutory rules protecting commercial tenants; grounds for termination, notice periods, and claim for damages due to loss of client base.
5. **Non-Disclosure Agreement (NDA) & Intellectual Property Clauses**:
   - Trade secret protection (*Obchodní tajemství* - § 504 NOZ).
   - Assignment of IP rights governed by the Copyright Act (*Autorský zákon č. 121/2000 Sb.*). Under Czech law, moral rights (*osobnostní práva*) cannot be transferred or waived; only exclusive economic exploitation rights (*výhradní majetková práva / licence*) can be granted.

### Breach, Damages & Enforcement:
- **Contractual Penalty (*Smluvní pokuta* - § 2048 NOZ)**:
  - Must be agreed in writing; payable regardless of fault or actual damages.
  - Court moderation right (*moderační právo soudu* - § 2051 NOZ): A court may reduce a disproportionately excessive penalty down to the level of actual damage.
- **Statutory Interest on Late Payments (*Zákonné úroky z prodlení*)**:
  - Governed by Government Decree No. 351/2013 Coll.
  - Calculated as: **Czech National Bank (ČNB) 2-week Repo Rate + 8 percentage points**.
- **Statute of Limitations (*Promlčení* - § 629 NOZ)**:
  - General subjective limitation period is **3 years** from when the party learned of the circumstance.
  - Objective maximum limitation period is **10 years**. Parties may agree on a custom limitation period between 1 and 15 years (§ 630 NOZ).

---

## 4. Trade Licensing Act (Zákon č. 455/1991 Sb., o živnostenském podnikání)

Conducting continuous, independent business for profit in the Czech Republic requires a trade license (*Živnostenské oprávnění*):
- **Free Trades (*Živnost volná*)**: Covers 80 statutory fields of activity (IT services, consulting, wholesale, marketing). No proof of professional qualification required; merely general conditions (18+ years, legal capacity, clean criminal record / *bezúhonnost*).
- **Craft Trades (*Živnost řemeslná*)**: Requires vocational certificate, university degree in field, or certified years of practical experience (e.g. electrical work, masonry, auto repair).
- **Regulated Trades (*Živnost vázaná*)**: Requires specific professional certifications prescribed by law (e.g. accounting advisory, psychological counseling, real estate brokerage).
- **Concession Trades (*Živnost koncesovaná*)**: Requires state concession and background security checks (e.g. passenger taxi transport, road freight, firearms).
- **Responsible Representative (*Odpovědný zástupce*)**: A legal entity or unqualified person must appoint a certified physical person who guarantees compliance with statutory qualifications.

---

## 5. Czech Labour Law & Schwarzsystém Prevention

The **Labour Code (*Zákoník práce č. 262/2006 Sb.*)** establishes mandatory employee protections:

### Employment Contracts (HPP):
- Essential statutory terms: (1) Type of work (*druh práce*), (2) Place of performance (*místo výkonu práce*), (3) Start date (*den nástupu*).
- **Probationary Period (*Zkušební doba*)**: Max 3 months for standard employees, max 6 months for managerial staff. Must be agreed in writing before employment commences.
- **Termination (*Rozvázání pracovního poměru*)**:
  - Mutual agreement (*Dohoda* - § 49).
  - Notice by employer (*Výpověď zaměstnavatelem* - § 52): Only on strict statutory grounds (redundancy, health incapacity, persistent performance breaches). Statutory notice period is a minimum of **2 calendar months**.
  - Statutory Severance (*Odstupné* - § 67): 1x, 2x, or 3x average monthly earnings based on tenure (under 1 year, 1-2 years, over 2 years).
  - Immediate termination (*Okamžité zrušení* - § 55): Permitted only for gross criminal conduct or extreme breach of discipline.

### Schwarzsystém (Disguised Employment - § 5 písm. e) Zákona č. 435/2004 Sb.):
The illegal practice of contracting an individual as an independent contractor (OSVČ) when the actual working relationship exhibits the characteristics of dependent employment:
- **Warning Signs evaluated by State Labour Inspection (*SÚIP*)**:
  - Worker performs duties under the direct management and instruction of the client.
  - Worker uses company equipment, laptops, email domain, and office space exclusively provided by the client.
  - Worker has set working hours, requested "vacation approval", and does not invoice other clients (economic dependence).
  - Worker bears zero entrepreneurial risk and does not hold a separate business establishment.
- **Statutory Sanctions**:
  - Fine up to **10,000,000 CZK** for the ordering entity (minimum fine 50,000 CZK).
  - Fine up to **100,000 CZK** for the contractor.
  - Retroactive assessment of all unpaid social insurance, health insurance, and personal income tax withholdings plus statutory penalties and late interest.

---

## 6. Public Registers, Transparency & Insolvency

- **Commercial Register (*Obchodní rejstřík* - Zákon č. 304/2013 Sb.)**:
  - Administered by regional courts (*Rejstříkový soud*).
  - **Collection of Deeds (*Sbírka listin*)**: Mandatory deposit of annual financial statements, auditor reports, and founding documents. Failure to submit can result in court fines up to 100,000 CZK or ex officio judicial liquidation of the company (§ 105a).
- **Register of Beneficial Owners (*Evidence skutečných majitelů - ESM* - Zákon č. 37/2021 Sb.)**:
  - Mandatory registration of the Ultimate Beneficial Owner (UBO - holding > 25% voting or profit rights).
  - **Severe Statutory Sanction**: An unregistered beneficial owner cannot receive dividend distributions, and the company is prohibited from voting the shares of an unregistered owner (§§ 53–54).
- **Insolvency Act (*Insolvenční zákon č. 182/2006 Sb.*)**:
  - **Insolvency Definitions**:
    - Inability to pay (*Platební neschopnost*): Multiple creditors, liabilities overdue for > 30 days, inability to satisfy obligations.
    - Over-indebtedness (*Předlužení*): Sum of the debtor's liabilities exceeds the fair value of their assets.
  - **Statutory Duty to File**: The executive must file a debtor's insolvency petition without undue delay upon becoming aware (or when they ought to have become aware) of insolvency. Delay creates direct personal tort liability for damages caused to creditors.

---

<a name="czech-litigation-advocacy"></a>
# 📦 SKILL: czech-litigation-advocacy
*Domain:* **Czech Litigation**

---
name: czech-litigation-advocacy
description: >-
  Czech judicial proceedings and trial advocacy: civil procedure (OSŘ č. 99/1963 Sb., pre-action notice § 142a, Electronic Payment Orders EPR), enforcement and judicial bailiffs (Exekuční řád č. 120/2001 Sb.), administrative justice (SŘS č. 150/2002 Sb., OAMP and tax litigation), white-collar criminal defense (Trestní zákoník č. 40/2009 Sb., corporate liability TOPO č. 418/2011 Sb.), and the Czech Bar Association regulations (Zákon o advokacii č. 85/1996 Sb., Advokátní tarif č. 177/1996 Sb.).
---
# Czech Litigation, Court Procedure & Advocacy (České soudní řízení, exekuce a advokacie)

A high-level procedural and tactical guide for litigation attorneys (*advokáti*), in-house counsel, and foreign legal practitioners conducting court litigation, enforcement actions, and administrative appeals in the Czech Republic.

---

## 1. Czech Judicial Architecture & Court Hierarchy

The court system of the Czech Republic (*Soudní soustava ČR*) is structured into a four-tier judicial hierarchy under Act No. 6/2002 Coll., on Courts and Judges:

```
               [ Ústavní soud ČR (Brno) - Constitutional Court ]
                                      ^
                                      |
         +----------------------------+----------------------------+
         |                                                         |
  [ Nejvyšší soud ČR (NS, Brno) ]               [ Nejvyšší správní soud ČR (NSS, Brno) ]
         |                                                         |
  [ Vrchní soudy (Praha, Olomouc) ]                 [ Krajské soudy (Správní úseky) ]
         |                                                         |
  [ Krajské soudy (Městský soud v Praze) ]                 [ Správní orgány ]
         |
  [ Okresní soudy (Obvodní soudy v Praze 1–10) ]
```

---

## 2. Civil Judicial Procedure (Občanský soudní řád - OSŘ č. 99/1963 Sb.)

### A. Pre-Action Formal Notice (*Předžalobní výzva k plnění* - § 142a OSŘ):
- **Statutory Precondition for Legal Costs**: To be awarded compensation for the costs of proceedings (*náhrada nákladů řízení*) against a defendant, the claimant **must send a written formal demand for payment at least 7 calendar days before filing the lawsuit**.
- **Delivery Rules**: Sent to the last known address or registered delivery address (or via mandatory Data Box / *Datová schránka*). Proof of dispatch (not necessarily proof of receipt) suffices if sent to the registered corporate seat or permanent address.

### B. Summary Payment Order Proceedings:
1. **Electronic Payment Order (*Elektronický platební rozkaz - EPR* - § 174a OSŘ)**:
   - For monetary claims up to **1,000,000 CZK**.
   - Submitted electronically via the Ministry of Justice ePodatelna portal using qualified electronic signature.
   - **Reduced Court Fee**: **4%** of the principal claim (minimum 800 CZK), compared to standard 5% (min. 1,000 CZK).
2. **Standard Payment Order (*Platební rozkaz* - § 172 OSŘ)**:
   - Issued by court without hearing the defendant based strictly on documentary evidence.
   - **Strict Delivery Rule**: Must be served into the defendant's own hands (*do vlastních rukou*). Fictitious service (*náhradní doručení / fikce doručení*) is legally precluded. If unserved, the court cancels the order and proceeds to standard trial.
3. **Opposition (*Odpor*)**:
   - The defendant has **15 calendar days** from the date of physical receipt to file an *Odpor*.
   - A timely filed opposition automatically cancels the payment order in full (*zrušení v plném rozsahu*), and the judge schedules a standard oral hearing.

### C. Standard Litigation (*Žalobní řízení*):
- **Burden of Allegation (*Břemeno tvrzení*) & Burden of Proof (*Důkazní břemeno*)**:
  - The plaintiff must state all material facts and propose evidence. Under § 118a OSŘ, the judge is required to give formal instructions (*poučení*) if a party fails to meet the burden.
- **Preliminary Injunctions (*Předběžné opatření* - §§ 74–77 OSŘ)**:
  - Applied when immediate preservation of the status quo is necessary.
  - Mandatory security deposit (*jistota na náhradu škody*): **10,000 CZK** for civil matters; **50,000 CZK** for commercial/entrepreneurial matters. Court decides within 7 days without hearing the counterparty.

### D. System of Legal Remedies (*Opravné prostředky*):
1. **Appellate Review (*Odvolání* - §§ 201–226 OSŘ)**:
   - Filed within **15 days** from the delivery of the written judgment.
   - Appellate courts (Regional Courts / High Courts) review both facts and law within the scope of the appeal. Principle of incomplete appellate review (*neúplná apelace*): new facts and evidence are admissible only under strict statutory exceptions (§ 205a OSŘ).
2. **Extraordinary Appeal (*Dovolání k Nejvyššímu soudu* - §§ 236–243g OSŘ)**:
   - Filed within **2 months** from the delivery of the appellate decision.
   - **Mandatory Representation by an Advocate**: The appellant must be represented by a Czech attorney (*advokát*).
   - Admissibility threshold: Legal question of substantive or procedural law that has not yet been resolved in Supreme Court case law, has been resolved differently by appellate courts, or deviates from established case law.
3. **Constitutional Complaint (*Ústavní stížnost* - Zákon č. 182/1993 Sb.)**:
   - Filed within **2 months** after exhausting all procedural remedies to the Constitutional Court in Brno for violation of fundamental constitutional rights (due process, fair trial under Art. 36 of Charter). Mandatory advocate representation.

---

## 3. Enforcement & Bailiff Law (Exekuční řád č. 120/2001 Sb.)

Enforcement of enforceable titles (*Exekuční titul* - judgments, arbitration awards, notarial deeds with direct enforceability clause / *notářský zápis s doložkou přímé vykonatelnosti*):

### A. Judicial Bailiffs (*Soudní exekutoři*):
- Free choice of bailiff: The creditor can select any court bailiff across the Czech Republic regardless of debtor's residence.
- The bailiff is endowed with state enforcement power to search and seize assets via automated electronic queries to banks, land registry, vehicle register, and social security.

### B. Core Execution Modalities:
1. **Garnishment of Bank Accounts (*Přikázání pohledávky z účtu*)**: Immediate electronic freeze on all bank accounts. Debtor can make a one-time emergency withdrawal of double the subsistence minimum (*dvojnásobek životního minima*).
2. **Protected Account (*Chráněný účet* - § 304c OSŘ)**: Allows the debtor to protect non-seizable parts of wage or social benefits from repeated garnishment.
3. **Wage Deductions (*Srážky ze mzdy*)**: Deductions by employer from net salary. The **Non-seizable Minimum (*Nezabavitelná částka*)** calculated under government decree must remain untouched for the debtor and their dependents.
4. **Execution on Movables (*Mobiliární exekuce*)**: Physical entry into debtor's residence/office, inventory listing (*soupis majetku*), and physical seizure of personal assets.
5. **Auction of Real Estate (*Dražba nemovitosti*)**: Expert cadastral appraisal followed by public electronic auction (*elektronická dražba*).

### C. Debtor Defense Tactics:
- **Motion to Terminate Execution (*Návrh na zastavení exekuce* - § 55 EŘ / § 268 OSŘ)**:
  - Grounds: Extinction of obligation, statute of limitations, nullity of underlying title, or lack of debtor's assets (*bezvýsledná exekuce*).
- **Motion to Suspend Execution (*Návrh na odklad exekuce* - § 54 EŘ)**: Temporary pause of actions when debtor suffers severe health/social misfortune without fault.

---

## 4. Administrative Justice (Soudní řád správní - SŘS č. 150/2002 Sb.)

Litigation challenging decisions, inaction, or unlawful interventions of public administrative authorities:

1. **Administrative Lawsuit (*Správní žaloba* - §§ 65–78 SŘS)**:
   - Filed to the specialized Administrative Chamber of Regional Courts (*Krajský soud / Městský soud v Praze*).
   - Strict deadline: **2 months** from the delivery of the final administrative appeal decision.
   - Primary cases: Contesting decisions of Financial Directorate (*Odvolací finanční ředitelství - OFŘ*) on tax assessments, decisions of Ministry of Interior (*OAMP MV ČR*) denying residence permits, work cards, or citizenship, decisions of the Czech Trade Inspection (*ČOI*).
2. **Cassation Complaint (*Kasační stížnost k NSS* - §§ 102–110 SŘS)**:
   - Filed to the Supreme Administrative Court in Brno within **2 weeks** from delivery of the regional court decision.
   - **Mandatory Representation by an Advocate** (unless the complainant has a recognized university master's degree in law).

---

## 5. Criminal Procedure & White-Collar Defense (Trestní právo)

Governed by the **Criminal Code (*Trestní zákoník č. 40/2009 Sb.*)** and **Code of Criminal Procedure (*Trestní řád č. 141/1961 Sb.*)**:

### A. Economic Crimes:
- **Fraud (*Podvod* - § 209 TZ)**: Causing damage to another by intentionally misleading or taking advantage of an error. Damage thresholds: Greater damage (*Větší škoda* > 100k CZK), Substantial damage (*Značná škoda* > 1M CZK), Large-scale damage (*Škoda velkého rozsahu* > 10M CZK).
- **Tax Evasion (*Zkrácení daně, poplatku a podobné povinné platby* - § 240 TZ)**: Failure to declare or intentionally understating tax liability in large extent.
- **Breach of Fiduciary Duty (*Porušení povinnosti při správě cizího majetku* - §§ 220, 221 TZ)**: Criminal liability of company executives (*jednatelé*) for mismanagement, harmful investments, or selling assets below market value.

### B. Corporate Criminal Liability (*Zákon o trestní odpovědnosti právnických osob - TOPO č. 418/2011 Sb.*):
- Legal entities can be criminally prosecuted for crimes committed by executives, supervisory members, or employees in the company's interest or within its scope of activity.
- Sanctions: Corporate fines up to 1,460,000,000 CZK, forfeiture of property, ban on public contracts, or judicial dissolution of the legal entity (*zrušení právnické osoby*).
- **Compliance Defense (§ 8 odst. 5 TOPO)**:
  - A corporation is **exonerated from criminal liability** if it proves that it took all measures that could reasonably be required to prevent the criminal offense (effective Criminal Compliance Program, internal whistleblowing channels, regular employee compliance training, independent internal audits).

---

## 6. The Czech Bar & Attorney Tariff (Advokacie a Advokátní tarif)

Advocates in the Czech Republic operate under **Act No. 85/1996 Coll., on the Legal Profession (*Zákon o advokacii*)** and are members of the **Czech Bar Association (*Česká advokátní komora - ČAK*)**:

### A. Attorney-Client Privilege (*Povinnost mlčenlivosti* - § 21 Zákona o advokacii):
- The advocate is statutorily bound by absolute secrecy regarding all facts learned during legal representation.
- Client privilege belongs to the client; only the client can relieve the advocate of confidentiality.
- Law office searches (*prohlídka advokátní kanceláře*) require the physical presence and consent of an authorized representative of ČAK; if consent is denied, it can be substituted only by a judge of the Regional Court (§ 85b Trestního řádu).

### B. Attorney Tariff (*Advokátní tarif - Vyhláška MS č. 177/1996 Sb.*):
Governs non-contractual attorney remuneration (*mimosmluvní odměna*) and the statutory reimbursement of legal costs awarded by courts against losing parties:
- **Tariff Value (*Tarifní hodnota* - § 8)**: The principal amount of the claim.
- **Rate per Legal Service Act (*Odměna za jeden úkon právní služby* - § 7)**:
  - Up to 10,000 CZK: 1,500 CZK.
  - Over 10,000 to 200,000 CZK: 1,500 CZK + 40 CZK per each 1,000 CZK above 10,000 CZK.
  - Over 200,000 to 10,000,000 CZK: 9,100 CZK + 40 CZK per each 10,000 CZK above 200,000 CZK.
- **Recognized Legal Service Acts (*Úkony právní služby* - § 11)**:
  - Initial conference with client including acceptance of representation.
  - Drafting of statement of claim (*žaloba*) or detailed defense response (*vyjádření ve věci*).
  - Drafting of appellate brief (*odvolání*) or cassation (*dovolání*).
  - Participation in court hearing (each commenced 2 hours counts as 1 act).
- **Lump-sum Outlay Allowance (*Režijní paušál* - § 13 odst. 4)**: Flat statutory fee of **300 CZK** per legal act to cover administrative and postal expenses, plus VAT (21%) if the advocate is a registered VAT payer.

---

<a name="devops-cloud-engineering"></a>
# 📦 SKILL: devops-cloud-engineering
*Domain:* **DevOps & Cloud**

---
name: devops-cloud-engineering
description: >-
  Expert workflows for modern DevOps, CI/CD pipelines (GitHub Actions, runners), Infrastructure as Code (Terraform, Ansible), containerization (Docker, Compose, rootless), cloud platforms (Oracle OCI, NetCup, AWS), monitoring (Prometheus, Grafana, Loki), and Linux performance kernel tuning.
---
# DevOps, Cloud Infrastructure & Automation Engineering

A comprehensive operational guide for architecting, deploying, automating, and maintaining cloud and on-premise infrastructure.

---

## 1. Continuous Integration & Deployment (CI/CD)

### GitHub Actions Hardened Production Pipeline:
```yaml
name: Production Hardened CI/CD
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

# Principle of least privilege for GITHUB_TOKEN
permissions:
  contents: read
  packages: write
  id-token: write # Required for OIDC cloud authentication
  security-events: write

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  audit-and-build:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - name: Checkout Code
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # Pin to exact commit SHA v4.2.2

      - name: Security Scan (SAST & Vulnerabilities)
        uses: aquasecurity/trivy-action@18f2510ee396bbf400402947b394f2dd8c87dbb0
        with:
          scan-type: 'fs'
          ignore-unfixed: true
          severity: 'CRITICAL,HIGH'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Set up QEMU & Docker Buildx
        uses: docker/setup-qemu-action@49b3bc8e6bdd4480e8226f5bf2164930cc65ee1e
      - uses: docker/setup-buildx-action@c47758b77c9736f4b2ef4073d4d51994fabfe349

      - name: Build Multi-Arch Container Image
        uses: docker/build-push-action@4f58ea79222b3b9dc2c8bbdd6debcef730109a75
        with:
          context: .
          platforms: linux/amd64,linux/arm64
          push: false
          tags: app:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

### Self-Hosted Runners Security & Isolation:
- Use ephemeral runners (e.g. GitHub Actions Runner Controller on Kubernetes) destroyed immediately after a single job execution.
- Strictly isolate runner networks using dedicated VLANs/Security Groups. Runners must never possess direct write access to production database subnets.
- Use OpenID Connect (OIDC) token exchange with AWS IAM / OCI / GCP to acquire short-lived STS tokens instead of storing long-lived credentials in GitHub Secrets.

---

## 2. Infrastructure as Code (IaC) & Configuration Management

### Terraform / OpenTofu Best Practices:
- **Remote State**: S3-compatible backend (e.g. OCI Object Storage, AWS S3) with state locking (DynamoDB or native object locking).
- **Module Architecture**: Reusable modules for VPC/VCN, security lists, compute instances, DNS records.
- **Drift Detection**: Automated scheduled runs to detect unauthorized out-of-band infrastructure modifications.
- **Pre-commit Checks**: Run `tflint`, `tfsec`, and `terraform fmt -check` in CI to prevent insecure infrastructure commits.

### Ansible Playbooks & Idempotency:
- Structure: Roles (`tasks`, `handlers`, `templates`, `vars`, `defaults`).
- **Idempotency Rule**: Playbooks must produce the exact same system state whether run once or 50 times (`changed_when` directives for custom shell commands).
- **Security**: Ansible Vault (`ansible-vault encrypt_string`) for secret storage in git repositories.

---

## 3. Containerization (Docker, Rootless & Kubernetes Hardening)

### Production Distroless Dockerfile Standard:
```dockerfile
# Multi-stage build pattern
FROM golang:1.23-bookworm AS builder
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o /bin/app ./cmd/server

# Final minimal runtime container (Google Distroless non-root)
FROM gcr.io/distroless/static-debian12:nonroot
WORKDIR /app
COPY --from=builder /bin/app /app/server
USER nonroot:nonroot
EXPOSE 8080
ENTRYPOINT ["/app/server"]
```

### Hardened Production Docker Compose (`compose.yaml`):
```yaml
services:
  app:
    image: ghcr.io/gincz/app:v2.1.0
    restart: unless-stopped
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    user: "10001:10001"
    tmpfs:
      - /tmp:rw,noexec,nosuid,size=64m
    environment:
      - NODE_ENV=production
    ports:
      - "127.0.0.1:8080:8080" # Bind to loopback only, never 0.0.0.0
    healthcheck:
      test: ["CMD", "/app/server", "-healthcheck"]
      interval: 10s
      timeout: 3s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 1024M
        reservations:
          memory: 256M
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
        max-file: "5"
```

### Kubernetes Pod Security Standards (Restricted Profile):
- Disallow privileged containers (`privileged: false`).
- Enforce read-only root filesystems (`readOnlyRootFilesystem: true`).
- Restrict Linux capabilities to none (`drop: ["ALL"]`).
- Deny root execution (`runAsNonRoot: true`, `runAsUser: 10001`).
- Enforce strict `NetworkPolicy` denying all ingress by default, whitelisting only designated microservice ports.

---

## 4. Cloud Infrastructure Management (Oracle OCI, NetCup, AWS)

### Oracle Cloud Infrastructure (OCI):
- **Free Tier Architecture**: Up to 4 ARM Ampere A1 cores and 24 GB RAM (flexible allocation across 1 to 4 VMs).
- **Network Topology**: Virtual Cloud Network (VCN), Internet Gateway, Service Gateway, Security Lists & Network Security Groups (NSGs).
- **OCI CLI Automation**: Scripted provisioning, snapshot management, and lifecycle policies via `oci-cli`.

### NetCup & Hetzner Infrastructure:
- Custom OS deployment via cloud-init and vKVM.
- FastPanel / Docker multi-tenant hosting with automated SSL and isolated PHP-FPM / Node.js pools.

---

## 5. Observability, Telemetry & Alerting

### Modern Observability Stack:
- **Metrics**: Prometheus pulling metrics via `node_exporter`, `cadvisor` (container stats), and application `/metrics`.
- **Dashboards**: Grafana with pre-configured operational dashboards (CPU, RAM, Disk I/O, Network Throughput).
- **Log Aggregation**: Vector / Promtail collecting `systemd journald` and container logs -> shipping to Grafana Loki.
- **Alerting**: Alertmanager triggering instant notifications to Telegram bots / webhooks upon high error rates, low disk space (< 15%), or unreachable nodes.

---

## 6. Linux Kernel & Performance Tuning (`sysctl.conf`)

Optimize Linux servers for high-throughput networking, database workloads, and low latency:

```ini
# /etc/sysctl.d/99-performance-tuning.conf

# File descriptors and memory
fs.file-max = 2097152
vm.swappiness = 10
vm.vfs_cache_pressure = 50

# TCP BBR Congestion Control
net.core.default_qdisc = fq
net.ipv4.tcp_congestion_control = bbr

# TCP Buffer and Window Scaling
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216

# Connection backlog & SYN Queue
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 100000
net.ipv4.tcp_max_syn_backlog = 16384
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_fin_timeout = 15

# Fast Ephemeral Port Allocation
net.ipv4.ip_local_port_range = 10240 65535
```
Apply immediately without reboot: `sysctl --system`.

---

<a name="endpoint-mobile-security"></a>
# 📦 SKILL: endpoint-mobile-security
*Domain:* **Endpoint & Mobile Security**

---
name: endpoint-mobile-security
description: >-
  Workstation, laptop, and mobile endpoint security: BitLocker/LUKS encryption, UEFI/Secure Boot, browser hardening, public Wi-Fi defense (VPN kill-switch), Android application security (APK analysis, jadx, permissions), spyware defense, and SIM swap mitigation.
---
# Endpoint, Workstation & Mobile Security

A comprehensive operational security guide for hardening workstations, laptops, and mobile devices (Android / iOS) against physical compromise, malicious software, network surveillance, and targeted spyware.

---

## 1. Laptop & Workstation Physical Security & Boot Integrity

### A. Boot & Firmware Security:
- **UEFI Secure Boot**: Enforce Secure Boot to guarantee that only cryptographically signed bootloaders (Windows Boot Manager, signed GRUB) can execute, preventing bootkits and evil maid attacks.
- **UEFI / BIOS Administrator Password**: Lock BIOS/UEFI access with a strong administrator password to prevent unauthorized changes to boot order or disabling security chips.
- **DMA (Direct Memory Access) Attack Mitigation**: Enable Kernel DMA Protection in BIOS/OS to neutralize malicious Thunderbolt/PCIe peripheral DMA exploits.

### B. Full-Disk Encryption (FDE):
- **Windows (BitLocker with TPM + Startup PIN)**:
  - Default TPM-only mode is vulnerable to physical TPM bus sniffing.
  - Enforce **TPM + Startup PIN** via Group Policy (`Computer Configuration -> Administrative Templates -> Windows Components -> BitLocker Drive Encryption -> Operating System Drives -> Require additional authentication at startup`).
  - Encryption algorithm: **XTS-AES 256-bit**.
- **Linux (LUKS2 with Argon2id)**:
  - Use `cryptsetup luksFormat --type luks2 --pbkdf argon2id /dev/nvme0n1p3`.
  - Secure swap partition with random encryption key or include swap inside the encrypted LVM volume.

---

## 2. Windows 11 & Linux Workstation Hardening

### Windows 11 Enterprise Hardening:
- **Enable Core Isolation & Memory Integrity (HVCI)**: Uses hardware virtualization to isolate critical OS processes from kernel malware.
- **PowerShell Attack Surface Reduction (ASR)**:
  Enable Defender ASR rules via PowerShell:
  ```powershell
  # Block executable content from email client and webmail
  Add-MpPreference -AttackSurfaceReductionRules_Ids BE9BA2D9-53EA-4CDC-84E5-9B1EEEE46550 -AttackSurfaceReductionRules_Actions Enabled

  # Block credential stealing from the Windows local security authority subsystem (lsass.exe)
  Add-MpPreference -AttackSurfaceReductionRules_Ids 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2 -AttackSurfaceReductionRules_Actions Enabled

  # Block process creations originating from PSExec and WMI commands
  Add-MpPreference -AttackSurfaceReductionRules_Ids d1e49aac-8f56-4280-b9ba-993a6d77406c -AttackSurfaceReductionRules_Actions Enabled
  ```
- **Disable USB Mass Storage Execution (Group Policy / Registry)**:
  Prevent malware introduction via unauthorized USB drives.

### Linux Desktop Hardening:
- Restrict `ptrace` scope: `echo 1 > /proc/sys/kernel/yama/ptrace_scope` (prevents processes from inspecting memory of other user processes).
- Use firejail / Flatpak sandboxing for untrusted graphical applications.

---

## 3. Public Wi-Fi, Travel Security & Network Privacy

When connecting to untrusted networks (hotels, airports, cafes):
1. **Always-On VPN with Kill-Switch**:
   - The operating system firewall must strictly drop all outbound non-VPN traffic.
   - If the VPN connection drops, no network packets may leak in cleartext.
   - **WireGuard Kill-Switch Implementation (Windows / Linux)**:
     Set `AllowedIPs = 0.0.0.0/0, ::/0` with `Table = auto` and firewall rules blocking native gateway traffic except the VPN endpoint IP.
2. **Preventing WebRTC IP Leaks**:
   - WebRTC can reveal local and public IP addresses even behind a VPN/proxy.
   - Disable WebRTC in browser configuration (`about:config` in Firefox -> `media.peerconnection.enabled = false`).
3. **Encrypted DNS**:
   - Enforce DNS-over-HTTPS (DoH) via Quad9 (`9.9.9.9` - blocks malicious domains) or Cloudflare (`1.1.1.2` - blocks malware).
4. **MAC Address Randomization**:
   - Enable per-network randomized MAC addresses on Windows and Android to prevent physical tracking across Wi-Fi hotspots.

---

## 4. Android Mobile Security Architecture

As an Android developer and administrator, maintain rigorous device and application hygiene:

### A. APK Reverse Engineering & Security Audit:
- **Decompilation & Analysis**:
  - `jadx-gui <target.apk>`: Decompile DEX bytecode into readable Java source code to inspect embedded API keys, hardcoded endpoints, and cryptographic implementations.
  - `apktool d <target.apk>`: Extract raw `AndroidManifest.xml`, resources, and smali code.
- **Signature Scheme Verification**:
  Ensure APKs are signed with modern v2/v3/v4 signing schemes via `apksigner verify --verbose <target.apk>`.
- **Runtime Permission Auditing**:
  - Scrutinize dangerous permissions: `READ_PHONE_STATE`, `READ_CALL_LOG`, `PROCESS_OUTGOING_CALLS`, `SYSTEM_ALERT_WINDOW` (overlay attacks), `BIND_ACCESSIBILITY_SERVICE` (banking trojans and keyloggers).

### B. Defense Against Spyware & RATs (Remote Access Trojans):
- **Accessibility Service Auditing**:
  - Regularly verify `Settings -> Accessibility`. Legitimate apps rarely require accessibility services unless providing assistive technologies. Banking trojans abuse accessibility to intercept 2FA codes and perform unauthorized transactions.
- **USB Debugging (ADB) Hygiene**:
  - **Disable USB Debugging** immediately after development sessions. Leaving ADB active allows anyone with physical access to bypass screen lock and extract data.
  - Revoke all authorized debugging computers periodically (`Settings -> Developer options -> Revoke USB debugging authorizations`).
- **Targeted Spyware Indicators (Pegasus / Predator)**:
  - Sudden battery drain, device overheating while idle, unexpected mobile data spikes in background, unexplained crashes of `netd` or system services.
  - Use the Mobile Verification Toolkit (MVT) to analyze Android system dumps and backup files for known IoCs.

### C. SIM Swap Defense & Authentication Hardening:
- **SIM Card PIN**:
  - Always enable a strong PIN on the physical SIM or eSIM (`Settings -> Security -> SIM card lock`).
  - Prevents an attacker from placing your stolen SIM card into another phone to receive SMS 2FA codes.
- **Eliminate SMS 2FA**:
  - Migrate all critical accounts (banking, GitHub, Google, server hosting) from SMS verification to hardware security keys (**FIDO2 / YubiKey**) or authenticator apps (TOTP).
- **Android Keystore & BiometricPrompt**:
  - In custom Android apps, always store cryptographic secrets inside the hardware-backed **Android Keystore** (`KeyGenParameterSpec.Builder(..., KeyProperties.PURPOSE_ENCRYPT | KeyProperties.PURPOSE_DECRYPT).setUserAuthenticationRequired(true)`).

---

<a name="eu-business-law-compliance"></a>
# 📦 SKILL: eu-business-law-compliance
*Domain:* **EU Business Law**

---
name: eu-business-law-compliance
description: >-
  Operational reference and compliance frameworks for EU business law, Single Market freedoms, GDPR regulations, EU AI Act, NIS2 cybersecurity directive, DSA/DMA, AML/CFT rules (FAÚ, sanctions, KYC/UBO), and European consumer protection directives.
---
# EU Business Law, Digital Regulations & Compliance (Právo EU a regulatorní rámec)

An operational framework for enterprise compliance, risk management, and commercial operations across the European Union Single Market.

---

## 1. European Union Legal Architecture

### Primary vs. Secondary Legislation:
- **Primary Law**: Treaty on European Union (**TEU**), Treaty on the Functioning of the European Union (**TFEU**), and the Charter of Fundamental Rights.
- **Secondary Law**:
  - **Regulations (*Nařízení*)**: Directly applicable in their entirety across all 27 Member States without requiring national transposition (e.g. GDPR, EU AI Act, DSA, DMA, DORA).
  - **Directives (*Směrnice*)**: Binding as to the result to be achieved, but require transposition into national statutory law by each Member State (e.g. NIS2, Omnibus Directive, VAT Directive).
  - **Decisions (*Rozhodnutí*)**: Binding in their entirety upon those to whom they are addressed.
- **Fundamental Judicial Doctrines**:
  - **Supremacy of EU Law (*Přednost unijního práva*)**: Established in *Costa v. ENEL* (Case 6/64); national laws conflicting with EU law must be set aside by national courts.
  - **Direct Effect (*Přímý účinek*)**: Established in *Van Gend en Loos* (Case 26/62); individuals can enforce clear, precise, and unconditional EU rights directly before national courts.

### The Four Fundamental Freedoms:
1. **Free Movement of Goods**: Prohibition of customs duties, quantitative restrictions, and equivalent measures (Articles 34–36 TFEU).
2. **Freedom to Provide Services (Services Directive 2006/123/EC)**: Cross-border temporary provision of services without requiring a local branch or establishment.
3. **Free Movement of Capital**: Prohibition of restrictions on payments and capital transfers between Member States and with third countries (Article 63 TFEU).
4. **Free Movement of Workers & Posting of Workers (Directive 96/71/EC & 2018/957/EU)**: Requires obtaining an **A1 Certificate** from national social security administrations (e.g. ČSSZ) and observing host country core labor conditions (minimum wage, health and safety).

---

## 2. General Data Protection Regulation (GDPR - Regulation (EU) 2016/679)

### Core Principles of Processing (Article 5):
- **Lawfulness, Fairness & Transparency**: Clear communication of data collection.
- **Purpose Limitation**: Collected only for specified, explicit, and legitimate purposes.
- **Data Minimisation**: Adequate, relevant, and limited to what is strictly necessary.
- **Accuracy**: Keeping data up to date, deleting inaccuracies without delay.
- **Storage Limitation**: Retained only as long as necessary for the processing purpose.
- **Integrity and Confidentiality**: Ensuring appropriate technical and organizational security (encryption, access control).
- **Accountability**: The data controller must be able to demonstrate compliance.

### Legal Bases for Processing (Article 6):
1. **Consent (*Souhlas*)**: Unbundled, freely given, specific, informed, and unambiguous. Must be as easy to withdraw as to give.
2. **Contractual Necessity (*Plnění smlouvy*)**: Necessary for entering into or performing a contract.
3. **Legal Obligation (*Právní povinnost*)**: Complying with statutory law (e.g. tax record retention, accounting acts).
4. **Vital Interests (*Životní zájmy*)**: Protecting life or physical integrity.
5. **Public Interest (*Veřejný zájem*)**: Exercising official authority.
6. **Legitimate Interests (*Oprávněný zájem*)**: Must be supported by a documented **Legitimate Interest Assessment (LIA - Balanční test)** balancing controller interests against individual rights.

### Mandatory Compliance Documentation:
- **Privacy Policy (*Zásady ochrany osobních údajů*)**: Public-facing notice complying with Articles 13 & 14.
- **Data Processing Agreement (DPA - Article 28)**: Mandatory contract with all third-party processors (hosting providers, SaaS, CRMs, payroll agencies).
- **Records of Processing Activities (ROPA - Article 30)**: Internal ledger of data categories, purposes, recipients, and retention periods.
- **Data Protection Impact Assessment (DPIA - Article 35)**: Mandatory before launching high-risk processing (large-scale automated profiling, surveillance, biometric data).

### International Data Transfers (Chapter V):
- **Adequacy Decisions**: Transfers permitted to approved countries (e.g. UK, Switzerland, Japan, Israel).
- **EU-US Data Privacy Framework (DPF)**: Transfers to US certified companies permitted under adequacy decision.
- **Standard Contractual Clauses (SCCs)**: European Commission pre-approved model clauses required when transferring data to non-adequate third countries, accompanied by a **Transfer Impact Assessment (TIA)**.

### Data Breach Management (Articles 33 & 34):
- **72-Hour Clock**: Must formally report any personal data breach to the national supervisory authority (in CZ: *Úřad pro ochranu osobních údajů - ÚOOÚ*) within **72 hours** of becoming aware.
- **Data Subject Notification**: Mandatory without undue delay if the breach poses a high risk to the rights and freedoms of natural persons.
- **Statutory Fines**: Up to **€20,000,000** or **4% of global annual turnover**, whichever is higher.

---

## 3. European Tech, AI & Cybersecurity Legislation

### A. The EU AI Act (Regulation (EU) 2024/1689):
The world's first comprehensive legal framework on Artificial Intelligence:
1. **Prohibited AI Practices (Article 5)**: Unacceptable risk; strictly banned:
   - Subliminal manipulative techniques distorting behavior causing harm.
   - Social scoring systems evaluating trustworthiness.
   - Real-time remote biometric identification in publicly accessible spaces for law enforcement (with narrow exceptions).
   - Biometric categorization deducing race, political opinions, trade union membership, or sexual orientation.
2. **High-Risk AI Systems (Articles 6 & Annex III)**:
   - AI used in critical infrastructure, recruitment/HR management, credit evaluation, educational assessment, biometric identification.
   - **Obligations**: Risk management system, high-quality training datasets, detailed technical documentation, automatic event logging, human oversight mechanisms, accuracy and cybersecurity resilience, CE marking, and registration in the EU database.
3. **General Purpose AI (GPAI) Models**:
   - Technical documentation, summary of training data copyright compliance, cooperation with the European AI Office.
   - Systemic risk GPAI models (cumulative compute > $10^{25}$ FLOPs) subject to model evaluations, adversarial testing (red-teaming), and incident reporting.
4. **Minimal/Limited Risk AI Transparency**:
   - Disclosing that content was generated or manipulated by AI (deepfakes, synthetic audio/video).
   - Informing users when they are interacting with an AI system (chatbots).

### B. NIS2 Directive (Directive (EU) 2022/2555 - Cybersecurity):
- **Entities Covered**: Divided into **Essential Entities** (*Základní subjekty*) and **Important Entities** (*Důležité subjekty*) across critical sectors: IT service providers, cloud computing, data centers, telecoms, energy, healthcare, banking, transport.
- **Core Requirements**:
  - Risk analysis, incident handling, business continuity (backup management, disaster recovery).
  - Supply chain security (auditing suppliers and software dependencies).
  - Cryptography and access control policies.
- **Incident Notification Timeline**:
  - **Early Warning**: Within **24 hours** of becoming aware of a significant incident.
  - **Incident Notification**: Within **72 hours** (initial assessment and severity).
  - **Final Report**: Within **1 month** detailing root cause and mitigation.
- **Direct Management Liability**: Corporate directors and executives can be held personally liable for gross negligence in failing to implement cybersecurity measures, including temporary bans from executive management.

### C. Digital Services Act (DSA) & Digital Markets Act (DMA):
- **DSA (Regulation (EU) 2022/2065)**: Liability exemptions for online intermediaries, illegal content takedown procedures, transparency in recommender algorithms, prohibition of dark patterns in UI.
- **DMA (Regulation (EU) 2022/1925)**: Ex-ante antitrust rules for systemic "gatekeeper" platforms (interoperability, self-preferencing bans, fair data access).

---

## 4. Anti-Money Laundering (AML / CFT) & Sanctions Compliance

Governed by EU AML Directives (5AMLD, 6AMLD), the new EU AML Regulation, and the Czech **AML Act (*Zákon č. 253/2008 Sb.*)**:
- **Obliged Entities (*Povinné osoby*)**: Credit institutions, payment institutions, accountants, tax advisors, auditors, notaries, lawyers in transactional matters, real estate agents, art dealers, and crypto asset service providers (CASPs under MiCA).
- **Customer Due Diligence (CDD / KYC)**:
  - Identification and verification of the client's identity before transaction execution (mandatory for transactions over €1,000 or upon suspicion).
  - **Ultimate Beneficial Owner (UBO / *Skutečný majitel*)**: Verifying physical persons owning or controlling > 25% of capital/voting rights.
  - **Politically Exposed Persons (PEP)**: Enhanced due diligence for individuals holding public political office and their family members.
  - **Source of Funds (*Původ finančních prostředků*)**: Establishing legitimate commercial or personal origins.
- **Sanctions Screening**: Mandatory real-time screening against the **EU Consolidated Financial Sanctions List** and international sanctions regimes (freeze of assets, prohibition of making funds available).
- **Mandatory Reporting of Suspicious Transactions (*Oznámení podezřelého obchodu*)**: Obliged entities must report suspicious transactions to the **Financial Analytical Office (*Finanční analytický úřad - FAÚ*)** without delay.

---

## 5. European Consumer Protection & E-Commerce

Governed by the Consumer Rights Directive (2011/83/EU) and the **Omnibus Directive ((EU) 2019/2161)**:
- **14-Day Right of Withdrawal (*Právo na odstoupení od smlouvy bez udání důvodu*)**:
  - Consumers shopping online have 14 days from receipt of goods to withdraw without penalty.
  - Exceptions: Custom-made products, sealed hygiene products once opened, digital content if consumer explicitly waived withdrawal rights upon immediate download commencement.
- **Price Transparency & Discounts (Article 6a)**:
  - Any announced price reduction (e.g. "Sale -30%") must clearly state the **lowest price applied by the seller during the preceding 30 days** (*historická nejnižší cena za posledních 30 dní*).
- **Verified Customer Reviews**:
  - Commercial sellers must disclose whether and how they ensure that published product reviews originate from consumers who actually purchased or used the product. Publishing unverified or fake reviews is treated as an aggressive unfair commercial practice.
- **Statutory Conformity Guarantee (Directive (EU) 2019/771)**:
  - Mandatory statutory 2-year guarantee for consumer goods.
  - Any defect that becomes apparent within **1 year** (in many states extended to 2 years) of delivery is legally presumed to have existed at the time of delivery unless proven otherwise by the seller.

---

<a name="eu-litigation-crossborder-law"></a>
# 📦 SKILL: eu-litigation-crossborder-law
*Domain:* **EU Cross-Border Litigation**

---
name: eu-litigation-crossborder-law
description: >-
  European cross-border civil litigation, jurisdiction and judgment recognition (Brussels I bis Reg 1215/2012, Rome I and Rome II Regulations), European Payment Orders (EPO), European Account Preservation Orders (EAPO), Court of Justice of the European Union (CJEU, preliminary rulings Art. 267, sanctions annulment Art. 263), European Court of Human Rights (ECtHR Strasbourg, ECHR, Rule 47), and International Commercial Arbitration (1958 New York Convention, ICC, VIAC, LCIA).
---
# European Cross-Border Litigation, CJEU, ECtHR & International Arbitration

A comprehensive procedural and tactical treatise for international litigators, arbitration counsel, cross-border advocates, and dispute resolution partners operating within the European Union and international treaty frameworks.

---

## 1. European Cross-Border Civil & Commercial Litigation

Cross-border disputes between parties residing in different EU Member States are governed by uniform European Union regulations:

### A. Jurisdiction & Judgment Enforcement: Brussels I bis (Regulation (EU) No 1215/2012):
- **General Rule (Article 4)**: Persons domiciled in a Member State shall be sued in the courts of that Member State, regardless of their nationality.
- **Special Alternative Jurisdictions (Article 7)**:
  - *Contracts (Art. 7(1))*: In matters relating to a contract, jurisdiction lies in the courts for the place of performance of the obligation in question:
    - Sale of goods: the place in a Member State where the goods were delivered or should have been delivered.
    - Provision of services: the place in a Member State where the services were provided or should have been provided.
  - *Torts / Delicts (Art. 7(2))*: In matters relating to tort, delict or quasi-delict, jurisdiction lies in the place where the harmful event occurred or may occur (*Erfolgsort* or *Handlungsort*).
- **Choice of Court Agreements / Prorogation (Article 25)**:
  - Parties may agree that the courts of a Member State shall have exclusive jurisdiction. The agreement must be in writing or evidenced in writing, or in accordance with international trade usages.
- **Abolition of Exequatur (Articles 36–39)**:
  - A judgment given in an EU Member State is recognized and enforceable in all other Member States **without any special declaration of enforceability (exequatur abolished)**.
  - The creditor obtains a **Certificate concerning a judgment (Annex I Form)** from the court of origin and submits it directly to the local enforcement authority/bailiff of the enforcing Member State.
  - Grounds for refusal of enforcement (Article 45) are strictly limited: contrary to public policy (*ordre public*), default judgment without timely service, or irreconcilability with an earlier judgment.

### B. Applicable Law: Rome I & Rome II Regulations:
1. **Rome I (Regulation (EC) No 593/2008 - Law Applicable to Contractual Obligations)**:
   - *Freedom of Choice (Article 3)*: A contract shall be governed by the law chosen by the parties.
   - *Absence of Choice (Article 4)*: Contracts for sale of goods are governed by the law of the seller's habitual residence; contracts for services by the provider's habitual residence.
   - *Overriding Mandatory Provisions (Article 9)*: Provisions the respect for which is regarded as crucial by a country for safeguarding its public interests (e.g. antitrust, employment protection, currency restrictions) apply regardless of the chosen governing law.
2. **Rome II (Regulation (EC) No 864/2007 - Law Applicable to Non-Contractual Obligations / Torts)**:
   - General rule (Article 4(1)): Governed by the law of the country in which the damage occurs (*lex loci damni*), irrespective of the country in which the event giving rise to the damage occurred.

---

## 2. Fast-Track European Debt Recovery Instruments

### A. European Payment Order (*EPO* - Regulation (EC) No 1896/2006):
- Fast, paperless procedure for collecting uncontested cross-border monetary claims across all EU Member States (except Denmark).
- **Process**: Creditor files **Form A** describing claim, interest, and documentary evidence without attaching physical exhibits.
- Court issues the order using **Form E**.
- Defendant has **30 calendar days** from service to file a Statement of Opposition using **Form F** without stating any reasons.
- If no opposition is filed, the court issues **Form G (Declaration of Enforceability)**, directly enforceable across the EU.

### B. European Account Preservation Order (*EAPO* - Regulation (EU) No 655/2014):
- Allows a creditor to obtain a cross-border freezing order on bank accounts held by the debtor in other EU Member States prior to or during litigation on the merits.
- **Ex Parte Surprise Effect**: The debtor is not notified of the application prior to the bank account freeze to prevent asset dissipation.
- **Strict Evidence Standards**: Creditor must prove urgent risk of asset diversion (*periculum in mora*) and plausible merit of the main claim (*fumus boni iuris*). Creditor typically must provide security (*jistota / security bond*).

### C. European Small Claims Procedure (*ESCP* - Regulation (EC) No 861/2007):
- For cross-border civil claims not exceeding **5,000 EUR**. Written procedure conducted using standard forms with strictly capped court costs and simplified evidence rules.

---

## 3. The Court of Justice of the European Union (CJEU / Curia, Luxembourg)

The highest judicial authority on European Union law, composed of the **Court of Justice** and the **General Court**:

### A. Preliminary Rulings (*Prejudiciální řízení* - Article 267 TFEU):
- National courts of EU Member States refer questions regarding the interpretation of EU Treaties or the validity and interpretation of secondary EU acts (Directives, Regulations).
- When a question is raised before a national court against whose decisions there is no judicial remedy under national law (e.g., Supreme Courts / Constitutional Courts), that court **is obliged to refer the question to the CJEU** (*CILFIT doctrine* exceptions: question irrelevant, already interpreted by CJEU / *acte éclairé*, or correct application obvious / *acte clair*).
- CJEU preliminary rulings establish binding universal precedents across all 27 Member States.

### B. Action for Annulment (*Žaloba na neplatnost* - Article 263 TFEU):
- Direct lawsuit before the General Court (*Tribunál*) to annul illegal acts of EU institutions (Council, Commission, ECB).
- **Sanctions Delisting Litigation**: Primary avenue for individuals and corporations targeted by EU restrictive measures (sanctions lists under Regulations 269/2014 and 833/2014) to contest listings.
  - Strict deadline: **2 months and 10 days** from publication or notification.
  - Grounds: Manifest error of assessment (*zjevně nesprávné posouzení*), lack of sufficient evidentiary substantiation by the European External Action Service (EEAS), breach of essential procedural requirements, or disproportionate violation of fundamental rights to property.

---

## 4. The European Court of Human Rights (ECtHR / CEDH, Strasbourg)

Enforces the **European Convention on Human Rights (ECHR)** against Contracting States:

### A. Admissibility Criteria (Article 35 ECHR):
1. **Exhaustion of Domestic Remedies**: The applicant must have exhausted all effective national judicial remedies up to the highest competent court (including national Constitutional Courts where applicable).
2. **Strict Time Limit**: The application must be lodged within **4 months** (reduced from 6 months under Protocol 15) from the date of the final domestic decision.
3. **No Anonymous Applications & No Prior Submissions**: Must not be substantially the same as a matter already submitted to another international procedure.
4. **Significant Disadvantage**: The applicant must have suffered a significant disadvantage (*substatní újma*).

### B. Application Requirements & Rule 47:
- Applications must strictly adhere to the official **ECtHR Application Form** under **Rule 47 of the Rules of Court**. Incomplete forms, failure to sign, or failure to enclose all domestic judgments with chronological pagination results in immediate administrative rejection without judicial review.
- Key Substantive Articles litigated:
  - **Article 6 (Right to a Fair Trial)**: Reasonable time, equality of arms, right to an impartial tribunal, presumption of innocence.
  - **Article 8 (Right to Respect for Private and Family Life)**: Privacy, banking secrecy, protection from unlawful surveillance.
  - **Protocol No. 1, Article 1 (Protection of Property)**: Peaceful enjoyment of possessions, arbitrary expropriation, disproportionate customs seizures or tax confiscations.
- **Just Satisfaction (Article 41 ECHR)**: Binding awards of pecuniary damage, non-pecuniary damage (*morální újma*), and legal costs payable by the respondent State.

---

## 5. International Commercial Arbitration (Mezinárodní obchodní arbitráž)

The preeminent global mechanism for resolving cross-border commercial disputes outside sovereign state court systems:

### A. Statutory & Treaty Foundation:
- **1958 New York Convention on the Recognition and Enforcement of Foreign Arbitral Awards**:
  - Ratified by over 170 sovereign states. Ensures arbitral awards rendered in one state are enforceable worldwide as domestic court judgments.
- **UNCITRAL Model Law on International Commercial Arbitration (1985/2006)**: The global statutory standard governing national arbitration statutes.
- **Core Principles**:
  - *Doctrine of Separability*: The arbitration clause (*rozhodčí doložka*) is legally autonomous from the main underlying contract; invalidity of the main contract does not invalidate the arbitration clause.
  - *Principle of Kompetenz-Kompetenz*: The arbitral tribunal has jurisdiction to determine its own jurisdiction.

### B. Leading International Arbitral Institutions:
- **ICC International Court of Arbitration (Paris)**: Leading venue worldwide; Terms of Reference (*mandát rozhodců*), scrutiny of awards by the Court prior to signing.
- **LCIA (London Court of International Arbitration)**: Common law efficiency, fast-track emergency arbitrator appointments.
- **VIAC (Vienna International Arbitral Centre)**: Premier hub for Central and Eastern European (CEE) cross-border disputes.
- **DIS (German Arbitration Institute)** & **SCC (Stockholm Chamber of Commerce)**.

### C. Drafting Arbitration Clauses & Enforcement Defense:
- **Essential Clause Elements**: (1) Clear agreement to arbitrate, (2) Selected institution and applicable rules, (3) Number of arbitrators (one or three), (4) Seat of arbitration (*lex arbitri*), (5) Language of proceedings, (6) Governing substantive law.
- **Grounds for Refusal of Enforcement (Article V of the New York Convention)**:
  - Incapacity of parties or invalidity of arbitration agreement under chosen law.
  - Lack of proper notice of arbitrator appointment or proceedings (denial of right to present case).
  - Award deals with dispute beyond the scope of arbitration submission (*ultra vires*).
  - Composition of tribunal not in accordance with agreement.
  - Award set aside by competent court at the seat of arbitration.
  - Non-arbitrability of dispute under enforcing state's law.
  - Enforcement contrary to the **Public Policy (*ordre public*)** of the country where enforcement is sought.

---

<a name="eu-vat-accounting"></a>
# 📦 SKILL: eu-vat-accounting
*Domain:* **EU VAT & Cross-Border Tax**

---
name: eu-vat-accounting
description: >-
  Operational guidelines and checklists for EU VAT Directives, cross-border B2B/B2C transactions, Reverse Charge mechanism, One Stop Shop (OSS/IOSS), Identifikovaná osoba status, VIES validation, DAC7, and pan-European financial standards (IFRS, local GAAP, Transfer Pricing).
---
# EU VAT, Cross-Border Transactions & Pan-European Accounting

A comprehensive operational manual for navigating the European Union Value Added Tax system, cross-border digital and physical trade, and European financial reporting standards.

---

## 1. European Union VAT Architecture

The European VAT system is harmonized under:
- **Council Directive 2006/112/EC** (The EU VAT Directive): Sets the baseline for taxable persons, taxable transactions, place of supply, tax exemptions, and rates.
- **Council Implementing Regulation (EU) No 282/2011**: Uniform application of place of supply rules for telecommunications, broadcasting, and electronic services.
- **Council Directive 2020/285/EU**: Modernized SME scheme allowing cross-border VAT exemptions for small businesses.
- **ViDA Initiative (VAT in the Digital Age)**: Introduction of digital reporting requirements, mandatory e-invoicing for cross-border B2B transactions, and single VAT registration.

---

## 2. Czech Implementation & Status Categories

In the Czech Republic, the EU VAT Directive is enacted through the **Act on Value Added Tax** (*Zákon č. 235/2004 Sb., o dani z přidané hodnoty - ZDPH*).

### Business Categories:
1. **Neplátce DPH (Non-VAT Registered)**:
   - Turnover under **2,000,000 CZK** in 12 consecutive calendar months (§ 6 ZDPH).
   - Invoices without VAT, cannot deduct input VAT on domestic business purchases.
2. **Plátce DPH (Full VAT Payer)**:
   - Compulsory registration upon crossing the 2,000,000 CZK threshold (application due within 10 days after the end of the month in which the limit was exceeded).
   - Voluntary registration allowed (subject to proving economic activity).
   - Charges VAT on domestic sales, deducts input VAT (*odpočet na vstupu*), files monthly/quarterly VAT return and *Kontrolní hlášení*.
3. **Identifikovaná osoba (Identified Person - § 6g to § 6i ZDPH)**:
   - Essential category for Czech digital businesses, freelancers, and small entities not registered for domestic VAT.
   - **Trigger 1 (§ 6g)**: Acquisition of goods from another EU member state exceeding 326,000 CZK/year.
   - **Trigger 2 (§ 6h)**: Purchase of services with place of supply in CZ from an EU or non-EU foreign provider (e.g. Google Workspace, Meta Ads, OpenAI, AWS, Stripe, GitHub, Hetzner, Adobe).
   - **Trigger 3 (§ 6i)**: Provision of cross-border B2B services to a customer in another EU member state under § 9 odst. 1 (where the customer pays tax under reverse charge).
   - **Operating Rules for Identifikovaná osoba**:
     - Remains a **non-VAT payer domestically** (invoices domestic Czech clients without VAT).
     - Receives a Czech VAT ID (`CZ...`).
     - Files a VAT return **only in the months** when an EU/foreign cross-border service was acquired, and pays 21% VAT to the Czech Financial Office (with no right to input tax deduction).
     - Files a *Souhrnné hlášení* (Recapitulative statement) only in the months when services were provided to an EU business.

---

## 3. Cross-Border B2B Supply & Reverse Charge

### The General Rule for Services (B2B):
- **Article 44 of the EU VAT Directive / § 9 odst. 1 ZDPH**:
  > The place of supply of services to a taxable person (business) is the place where that person has established their business.
- **Result**: The transaction is not taxed in the supplier's country. Tax liability shifts entirely to the customer.

### Operational Reverse Charge Checklist:
1. **Mandatory VIES Verification**:
   - Check the customer's VAT ID in the official European Commission VIES database: `https://ec.europa.eu/taxation_customs/vies/`
   - Store or print the VIES validation certificate (with timestamp and consultation number) in your accounting records.
2. **Invoice Requirements (Directive 2010/45/EU)**:
   - Must show the supplier's full name, address, and VAT ID.
   - Must show the customer's full name, address, and valid EU VAT ID.
   - **Mandatory Reverse Charge Clause**:
     - English: *"Invoice subject to the VAT Reverse Charge mechanism pursuant to Article 196 of Council Directive 2006/112/EC. VAT to be accounted for by the recipient."*
     - Czech: *"Daň odvede zákazník dle § 9 odst. 1 a § 92a zákona č. 235/2004 Sb. (Reverse charge - přenesená daňová povinnost)."*
   - Net amount only (0% VAT shown on the invoice).
3. **Reporting via Souhrnné hlášení (EC Sales List)**:
   - Filed electronically by the **25th of the following month**.
   - Code **3**: Provision of services with place of supply in another Member State pursuant to Art. 44 / § 9 odst. 1.
   - Code **0**: Intra-Community supply of goods (*Dodání zboží do jiného členského státu*).

### Intra-Community Supply of Goods (B2B):
- **Article 138 EU VAT Directive / § 64 ZDPH**:
  - Supply of goods to a VAT-registered business in another Member State is **exempt with credit** (0% VAT).
  - **Condition**: The goods must physically leave the territory of the supplier's Member State and enter the customer's Member State.
  - **Burden of Proof (Implementing Regulation 2018/1912)**: At least two non-contradictory pieces of evidence prepared by independent parties (e.g. signed CMR consignment note, bill of lading, carrier tracking document, bank receipt).

---

## 4. Cross-Border B2C E-Commerce & The One Stop Shop (OSS)

For sales of goods and digital services to non-business consumers (B2C) across the European Union:

### Pan-European Distance Selling Threshold:
- **€10,000 / 256,000 CZK threshold**: Total cross-border B2C sales across all other 26 EU member states combined in a calendar year.
- **Below €10,000**: Seller may apply domestic VAT rates (e.g. Czech 21%) and pay to the home tax authority.
- **Above €10,000**: VAT must be charged at the **destination country's statutory rate** (e.g., 19% for Germany, 20% for France, 25% for Sweden).

### The One Stop Shop (OSS - Režim jednoho správního místa):
Eliminates the requirement to register for VAT in every individual EU destination country:
1. **Union Scheme (*Režim EU*)**:
   - Covers intra-EU distance sales of goods and B2C services.
   - Registration with the home tax authority (in CZ: Finanční úřad pro Jihomoravský kraj - Územní pracoviště Brno I).
   - Single quarterly electronic tax return filed by the end of the month following the calendar quarter.
   - Single quarterly payment in EUR to the home authority, which automatically redistributes funds to the destination Member States.
2. **Import Scheme (IOSS - *Dovozní režim*)**:
   - Covers distance sales of goods imported from third countries (outside the EU) in consignments with an intrinsic value not exceeding **€150**.
   - Simplifies customs clearance; VAT is collected directly at checkout and remitted monthly via IOSS.

---

## 5. European Platform Economy & DAC7

Under **Council Directive (EU) 2021/514 (DAC7)**:
- Digital platform operators (marketplaces, ride-hailing apps like Uber/Bolt, accommodation platforms like Airbnb/Booking, freelancing platforms) are legally obligated to collect and report annual seller earnings to EU tax administrations.
- **Data reported**: Seller identification, tax identification numbers (TIN/DIČ), bank account numbers, total gross remuneration paid, and transaction counts.
- **Automatic Exchange of Information**: The Czech Financial Administration automatically matches DAC7 data against reported DPFO/DPPO returns to detect undeclared income.

---

## 6. European Financial Reporting & Accounting Standards

### IFRS / IAS vs. European National GAAPs:
- **IFRS (International Financial Reporting Standards)**: Mandatory for consolidated financial statements of publicly listed companies across the EU (Regulation (EC) No 1606/2002); widely used by large cross-border corporate groups.
- **Core Pan-European Accounting Principles**:
  1. **True and Fair View (*Věrný a poctivý obraz*)**: Overriding qualitative standard.
  2. **Accrual Principle (*Akruální báze / Časové rozlišení*)**: Revenues and costs are recognized in the period they occur, not when cash is transferred:
     - Deferred expenses / accrued income (*Náklady / Příjmy příštích období*).
     - Accrued expenses / deferred income (*Výdaje / Výnosy příštích období*).
  3. **Prudence Principle (*Zásada opatrnosti*)**: Recognizing anticipated liabilities, foreseeable losses, and bad debt impairments (*opravné položky a rezervy*), while not recognizing anticipated profits.
  4. **Going Concern (*Předpoklad trvání podniku*)**: Valuation assumes the entity will continue operational activities for at least 12 months.

### Transfer Pricing within EU Corporate Groups:
- **Arm's Length Principle (§ 23 odst. 7 ZDP / OECD Guidelines)**:
  > Prices charged in commercial or financial transactions between associated enterprises (cross-border sister/parent entities) must reflect market prices that would have been agreed between independent entities under identical circumstances.
- **Documentation Standards**:
  - **Master File**: Overview of the global group, IP ownership, financial arrangements.
  - **Local File**: Detailed transactional analysis of local entity, functional and risk analysis (*funkční a riziková analýza*), selection of transfer pricing method (CUP, Cost Plus, Resale Price, TNMM).
  - Penalty for non-compliance: Unilateral retroactive tax base adjustments by tax authorities with 20% penalty and statutory interest on arrears.

---

<a name="internal-medicine-hematology"></a>
# 📦 SKILL: internal-medicine-hematology
*Domain:* **Clinical Medicine**

---
name: internal-medicine-hematology
description: >-
  Internal medicine, hematology, complete blood count (CBC) interpretation, anemia classification, coagulation profiles (INR, D-dimer), biochemistry panels (liver, renal, lipids, electrolytes), and inflammatory biomarkers.
---
# Internal Medicine, Clinical Hematology & Laboratory Diagnostics

A master clinical manual for interpreting hematological profiles, serum biochemistry, coagulation cascades, metabolic markers, and organ function panels in general practice and hospital internal medicine.

---

## 1. Complete Blood Count (CBC / *Krevní obraz*) & Differentials

### A. Red Blood Cell Parameters & Reference Values:
- **Hemoglobin (Hb)**: Men **$135–175\text{ g/L}$**; Women **$120–160\text{ g/L}$**.
- **Hematocrit (Ht)**: Men $0.40–0.50$ (40–50%); Women $0.36–0.46$ (36–46%).
- **Erythrocytes (RBC)**: Men $4.3–5.9 \times 10^{12}\text{/L}$; Women $3.8–5.2 \times 10^{12}\text{/L}$.
- **Mean Corpuscular Volume (MCV)**: **$80–100\text{ fL}$** (Key branching metric for anemia classification).
- **Mean Corpuscular Hemoglobin (MCH)**: $27–33\text{ pg}$.
- **Red Cell Distribution Width (RDW)**: $11.5–14.5\%$ (Anisocytosis index; elevated in nutritional deficiencies).

### B. Algorithmic Differential Diagnosis of Anemia:

```
                                  [Hemoglobin Low (Anemia)]
                                              |
                   +--------------------------+--------------------------+
                   |                                                     |
         [Microcytic (MCV < 80 fL)]                           [Macrocytic (MCV > 100 fL)]
                   |                                                     |
    +--------------+--------------+                       +--------------+--------------+
    |                             |                       |                             |
[Iron Deficiency Anemia]   [Anemia of Chronic Disease]  [Megaloblastic]         [Non-Megaloblastic]
- Low Ferritin (< 30 ug/L) - Normal/High Ferritin       - Vitamin B12 Defic.    - Alcoholism / Liver disease
- Low Iron, High TIBC      - Low Iron, Low TIBC         - Folate Deficiency     - Reticulocytosis (hemolysis)
- High RDW                 - High ESR / CRP             - Hypersegmented PMNs   - Hypothyroidism / MDS
                                                        - Neuropathy (B12 only)
```

- **Normocytic Anemia (MCV 80–100 fL)**:
  - Check **Reticulocyte Count**:
    - **High Reticulocytes ($> 2.5\%$)**: Active bone marrow response to peripheral destruction/loss -> **Acute Hemorrhage** or **Hemolysis** (Check: unconjugated bilirubin $\uparrow$, LDH $\uparrow$, haptoglobin $\downarrow$, direct Coombs test).
    - **Low / Normal Reticulocytes**: Hypoproliferative bone marrow -> **Chronic Kidney Disease** (EPO deficiency), early iron/mixed deficiency, endocrine disorders, aplastic anemia, leukemia.

### C. White Blood Cells & Leukogram ($4.0–10.0 \times 10^9\text{/L}$):
- **Neutrophils ($45–70\%$ / $2.0–7.0 \times 10^9\text{/L}$)**:
  - Neutrophilia with "left shift" (increased band forms $> 5\%$, toxic granulation): Hallmark of **acute bacterial infections**, tissue necrosis (MI, burns), or steroid therapy.
- **Lymphocytes ($20–45\%$ / $1.0–4.0 \times 10^9\text{/L}$)**:
  - Lymphocytosis: Typical for viral infections (EBV, CMV, influenza), pertussis, chronic lymphocytic leukemia (CLL).
- **Eosinophils ($1–5\%$ / $0.05–0.5 \times 10^9\text{/L}$)**:
  - Eosinophilia ($> 0.5 \times 10^9\text{/L}$): Allergic disorders (asthma, eczema, drug reactions), parasitic infections (helminths), eosinophilic granulomatosis with polyangiitis (EGPA / Churg-Strauss).
- **Platelets ($150–450 \times 10^9\text{/L}$)**:
  - Thrombocytopenia ($< 150 \times 10^9\text{/L}$): Critical bleeding risk when $< 20–30 \times 10^9\text{/L}$. Causes: Immune Thrombocytopenia (ITP), Thrombotic Thrombocytopenic Purpura (TTP - emergency!), drug-induced (heparin-induced thrombocytopenia - HIT), liver cirrhosis with splenomegaly.

---

## 2. Coagulation & Thrombosis Profiling

### A. Standard Coagulation Tests:
- **Prothrombin Time (PT / Quick / INR)**:
  - Evaluates extrinsic and common pathways (Factors VII, X, V, II, I).
  - Normal INR: **$0.8–1.2$**.
  - Therapeutic target on Warfarin: **$2.0–3.0$** (Deep vein thrombosis, PE, non-valvular AF) or **$2.5–3.5$** (mechanical mitral heart valves).
- **Activated Partial Thromboplastin Time (aPTT)**:
  - Evaluates intrinsic and common pathways (Factors XII, XI, IX, VIII, X, V, II, I). Normal: **$25–35\text{ seconds}$** (ratio $0.8–1.2$).
  - Monitored during Unfractionated Heparin (UFH) therapy (target ratio 1.5–2.5).
- **Fibrinogen (Factor I)**:
  - Normal: **$2.0–4.0\text{ g/L}$**. Acute phase protein; severe depletion ($< 1.0–1.5\text{ g/L}$) occurs in Disseminated Intravascular Coagulation (DIC) and massive obstetric hemorrhage.
- **D-Dimer**:
  - Specific degradation product of cross-linked fibrin. Normal: **$< 0.5\text{ mg/L FEU}$**.
  - **Clinical Rule**: D-Dimer has very high sensitivity ($> 95\%$) but low specificity. Its clinical utility lies entirely in its **Negative Predictive Value**: a normal D-dimer safely rules out Deep Vein Thrombosis (DVT) and Pulmonary Embolism (PE) in patients with low-to-intermediate pre-test clinical probability (Wells score).

---

## 3. Comprehensive Metabolic & Organ Panels

### A. Renal Function Panel:
- **Serum Creatinine**: Men $62–106\ \mu\text{mol/L}$; Women $44–84\ \mu\text{mol/L}$. (Dependent on muscle mass).
- **eGFR (Estimated Glomerular Filtration Rate - CKD-EPI Formula)**:
  - **$\ge 90\text{ mL/min/1.73m}^2$**: Normal (Stage 1 CKD if kidney damage markers present).
  - **$60–89\text{ mL/min/1.73m}^2$**: Mild reduction (Stage 2).
  - **$30–59\text{ mL/min/1.73m}^2$**: Moderate reduction (Stage 3a/3b - drug dosage adjustment required).
  - **$< 15\text{ mL/min/1.73m}^2$**: End-Stage Renal Disease (Stage 5 - dialysis requirement).
- **Blood Urea Nitrogen / Urea**: $2.5–7.5\text{ mmol/L}$. Elevated Urea with normal Creatinine indicates dehydration (pre-renal azotemia) or upper gastrointestinal bleeding.

### B. Hepatic Panel (Liver Function Tests - LFTs):
- **ALT (Alanine Aminotransferase)**: $< 0.8\ \mu\text{kat/L}$ (specific marker of hepatocellular injury/necrosis).
- **AST (Aspartate Aminotransferase)**: $< 0.8\ \mu\text{kat/L}$.
  - **De Ritis Ratio ($\text{AST} / \text{ALT}$)**: $> 2.0$ strongly indicates alcoholic hepatitis or advanced cirrhosis; $< 1.0$ typical for non-alcoholic fatty liver disease (NAFLD/NASH) or viral hepatitis.
- **GGT (Gamma-Glutamyl Transferase)** & **ALP (Alkaline Phosphatase)**: Markers of biliary stasis (cholestasis) or biliary tree obstruction. GGT is a sensitive marker of alcohol induction and hepatic enzyme stimulation.
- **Bilirubin**: Total $< 21\ \mu\text{mol/L}$; Direct (conjugated) $< 5\ \mu\text{mol/L}$. Jaundice becomes clinically apparent when bilirubin exceeds $40–50\ \mu\text{mol/L}$.

### C. Lipid Panel & Cardiovascular Target Guidelines:
- **Total Cholesterol**: $< 5.0\text{ mmol/L}$.
- **Triglycerides**: $< 1.7\text{ mmol/L}$.
- **HDL-Cholesterol**: $> 1.0\text{ mmol/L}$ (men); $> 1.2\text{ mmol/L}$ (women).
- **LDL-Cholesterol (Target Goals by ESC Cardiovascular Risk Tier)**:
  - **Low Risk**: $< 3.0\text{ mmol/L}$ ($< 116\text{ mg/dL}$).
  - **Moderate Risk**: $< 2.6\text{ mmol/L}$ ($< 100\text{ mg/dL}$).
  - **High Risk**: $< 1.8\text{ mmol/L}$ ($< 70\text{ mg/dL}$) and $\ge 50\%$ reduction from baseline.
  - **Very High Risk** (Known CAD, post-stenting/CABG, diabetes with organ damage, severe CKD): **$< 1.4\text{ mmol/L}$ ($< 55\text{ mg/dL}$)** and $\ge 50\%$ reduction. Managed with high-intensity statins (*Atorvastatin 40–80 mg, Rosuvastatin 20–40 mg*) + Ezetimibe + PCSK9 inhibitors if needed.

### D. Carbohydrate Metabolism:
- **Fasting Plasma Glucose**:
  - Normal: $3.9–5.5\text{ mmol/L}$.
  - Impaired Fasting Glucose (Prediabetes): $5.6–6.9\text{ mmol/L}$.
  - Diabetes Mellitus: $\ge 7.0\text{ mmol/L}$ (confirmed on two separate days) or random glucose $\ge 11.1\text{ mmol/L}$ with symptoms.
- **Glycated Hemoglobin (HbA1c)**:
  - Normal: $< 38\text{ mmol/mol}$ ($< 5.7\%$).
  - Prediabetes: $39–47\text{ mmol/mol}$ ($5.7–6.4\%$).
  - Diabetes diagnostic: $\ge 48\text{ mmol/mol}$ ($\ge 6.5\%$). Reflects average glycemic control over the preceding 2–3 months (erythrocyte lifespan).

---

## 4. Inflammatory & Infection Biomarkers

- **C-Reactive Protein (CRP)**:
  - Acute phase reactant produced by the liver under IL-6 stimulation.
  - Normal: **$< 5.0\text{ mg/L}$**.
  - Mild elevation ($10–40\text{ mg/L}$): Viral infections, mild localized inflammation, chronic autoimmune disease.
  - Marked elevation ($> 50–100+\text{ mg/L}$): Acute invasive **bacterial infections**, major trauma, sepsis, acute pancreatitis.
- **High-Sensitivity CRP (hs-CRP)**:
  - Assesses baseline vascular microinflammation and atherogenic cardiovascular risk ($< 1.0\text{ mg/L}$ low risk, $1.0–3.0$ average, $> 3.0$ high risk).
- **Procalcitonin (PCT)**:
  - Prohormone produced by thyroid C-cells and ubiquitous parenchymal tissues in response to bacterial endotoxins.
  - Normal: $< 0.1\ \mu\text{g/L}$. Values $> 0.5–2.0\ \mu\text{g/L}$ strongly support severe systemic bacterial infection/sepsis and guide initiation and de-escalation of antibacterial therapy.

---

<a name="intl-contract-drafting-ip"></a>
# 📦 SKILL: intl-contract-drafting-ip
*Domain:* **International Law & IP**

---
name: intl-contract-drafting-ip
description: >-
  International commercial contracts and cross-border intellectual property: UN CISG 1980 (Vienna Sales Convention), Incoterms 2020 delivery rules, cross-border contract engineering (Force Majeure, Hardship, Liability caps), international IP protection (WIPO Madrid System, EUIPO EUTM, PCT, EPO, Unitary Patent UPC), and software licensing (SaaS, SLA, Open Source compliance, IP assignment).
---
# International Contract Engineering & Cross-Border Intellectual Property

An exhaustive professional manual for international transaction lawyers, trade compliance officers, IP attorneys, and corporate structuring specialists negotiating and enforcing cross-border commercial transactions and intellectual property rights.

---

## 1. The UN Convention on Contracts for the International Sale of Goods (CISG 1980)

The **Vienna Sales Convention (CISG)** applies automatically to contracts of sale of goods between parties whose places of business are in different Contracting States (Article 1(1)(a)):

### A. Core Operational Principles:
- **Automatic Application & Opt-Out (Article 6)**: Parties may exclude the application of CISG entirely or derogate from any of its provisions. To exclude CISG effectively, standard governing law clauses must explicitly state: *"This Agreement shall be governed by the laws of [Country], excluding the United Nations Convention on Contracts for the International Sale of Goods (CISG 1980)"*.
- **Excluded Sales (Article 2)**: Consumer goods, auction sales, execution or other authority sales, stocks, shares, securities, negotiable instruments, vessels, aircraft, electricity.
- **Contract Formation**: Offer and acceptance rule; revocability of offers (Article 16); battle of forms / altered terms treated as rejection and counter-offer unless non-material (Article 19).

### B. Buyer & Seller Remedies:
- **Fundamental Breach (*Podstatné porušení smlouvy* - Article 25)**: A breach is fundamental if it results in such detriment to the other party as substantially to deprive them of what they are entitled to expect under the contract.
  - Fundamental breach gives the innocent party the immediate right to **declare the contract avoided (*odstoupení od smlouvy* - Articles 49, 64)** and demand restitution.
- **Notice of Lack of Conformity (Article 39)**:
  - The buyer loses the right to rely on a lack of conformity of the goods if they do not give notice to the seller specifying the nature of the lack of conformity within a **reasonable time** after discovery (absolute longstop period of **2 years** from handover).

---

## 2. Incoterms 2020 Rules & Logistics Risk Allocation

Published by the International Chamber of Commerce (ICC), **Incoterms 2020** defines the exact point of delivery, transfer of risk of loss/damage, and division of transport/customs costs:

| Term | Category | Place of Risk Transfer | Export Clearance | Import Clearance | Marine Insurance |
|---|---|---|---|---|---|
| **EXW** (Ex Works) | Any Mode | At seller's factory/warehouse before loading | Buyer | Buyer | None required |
| **FCA** (Free Carrier) | Any Mode | Loaded on carrier at seller's premises or named terminal | Seller | Buyer | None required |
| **CPT** (Carriage Paid To) | Any Mode | Handed over to first carrier (freight paid to destination) | Seller | Buyer | None required |
| **CIP** (Carriage & Insurance) | Any Mode | Handed over to first carrier | Seller | Buyer | **Mandatory Institute Cargo Clauses (A)** (All Risks) |
| **DAP** (Delivered at Place) | Any Mode | At destination ready for unloading | Seller | Buyer | None required |
| **DPU** (Delivered Place Unloaded) | Any Mode | At destination **unloaded** from arriving vehicle | Seller | Buyer | None required |
| **DDP** (Delivered Duty Paid) | Any Mode | At destination ready for unloading, **taxes & import duties paid** | Seller | **Seller** (highest risk/cost for seller) | None required |
| **FOB** (Free on Board) | Sea/Waterway | On board the vessel at named port of shipment | Seller | Buyer | None required |
| **CIF** (Cost, Insurance & Freight)| Sea/Waterway | On board the vessel at port of shipment | Seller | Buyer | **Mandatory Institute Cargo Clauses (C)** (Basic risks) |

---

## 3. High-Stakes Contract Architecture & Protective Clauses

When drafting international commercial agreements (IT outsourcing, wholesale, distribution, licensing):

### A. Force Majeure & Hardship (ICC 2020 Standards):
- **Force Majeure Clause**: Relieves a party from liability for failure to perform if caused by an impediment beyond reasonable control, which could not reasonably have been foreseen at the time of conclusion, and could not reasonably have been avoided or overcome (armed conflict, trade embargoes, state acts, natural catastrophes).
- **Hardship / Change of Circumstances (*Rebus sic stantibus*)**: When performance becomes excessively onerous due to unforeseen economic events. Mandates renegotiation of contractual terms within 30 days; failure gives right to terminate or submit to arbitration for equitable adjustment.

### B. Limitation of Liability & Liquidated Damages:
- **Liability Caps**: Typically capping aggregate contractual damages at 100% of the total fees paid under the agreement in the preceding 12 months.
- **Carve-outs from Caps**: Gross negligence (*hrubá nedbalost*), willful misconduct (*úmysl*), breach of confidentiality (NDA), and IP infringement indemnity must remain uncapped under mandatory European civil law doctrines.
- **Liquidated Damages vs Penalties**: In Anglo-American jurisdictions, penalties intended as a deterrent are unenforceable, and clauses must reflect a genuine pre-estimate of loss. In Continental civil law (Germany, Czechia, France), contractual penalties (*smluvní pokuty*) are fully enforceable, subject only to equitable judicial moderation.

---

## 4. Cross-Border Intellectual Property Protection

### A. Trademarks & Brand Architecture:
1. **WIPO Madrid System (Madrid Protocol)**:
   - File a single international application through the national IP office (Rospatent, ÚPV ČR) designating multiple target jurisdictions (over 130 member countries). Cost-effective centralized renewals every 10 years. Dependency period: International registration depends on the basic national mark for 5 years (*central attack* risk).
2. **European Union Trade Mark (*EUTM* via EUIPO, Alicante)**:
   - A single unitary registration protecting the mark across all 27 EU Member States. An opposition based on prior rights in even one member country blocks the entire EU-wide registration (can be converted into national filings).

### B. Patents & Innovations:
1. **Patent Cooperation Treaty (*PCT* via WIPO)**: Centralized international filing establishing a global priority date, followed by national phase entry at month 30/31.
2. **European Patent (*EP* via EPO, Munich)**: Centralized examination, validated nationally in designated Contracting States.
3. **Unitary Patent (*UP*) & Unified Patent Court (*UPC*)**: Direct unitary effect across participating EU member states with single centralized litigation before the Unified Patent Court, eliminating fragmented national litigation.

---

## 5. Software Licensing, SaaS & IP Assignment Engineering

### A. Software as a Service (SaaS) & Service Level Agreements (SLA):
- **License vs Service**: SaaS is legally classified as a service, not a software copyright license; customers obtain access to functionality hosted on remote servers without receiving copy of object or source code.
- **SLA Metrics**: Availability commitment (e.g. 99.9% uptime excluding scheduled maintenance), latency thresholds, Response Time by severity levels (Sev 1 Critical: < 1 hour; Sev 2 Major: < 4 hours), and Service Credits remedy (percentage credit against monthly fees as sole remedy).

### B. IP Assignment in Software Development (Work for Hire):
- In international software contracting, developers must execute a strict **IP Assignment Agreement**:
  - Full present assignment of all existing and future intellectual property rights, copyrights, patents, and trade secrets created during engagement (*"hereby assigns"*).
  - Explicit transfer of source code, documentation, architectures, and design tokens.
  - Irrevocable waiver of moral rights (*osobnostní práva*) to the maximum extent permitted by applicable governing law.

### C. Open Source Software (OSS) Compliance:
- **Permissive Licenses (MIT, Apache 2.0, BSD)**: Minimal restrictions; requires preservation of copyright notice and disclaimer. Apache 2.0 provides express patent license grants.
- **Copyleft Viral Licenses (GPLv2, GPLv3, AGPLv3)**:
  - If proprietary corporate software statically links or incorporates GPL code, the entire combined derivative work must be disclosed in open source under GPL.
  - AGPLv3 triggers copyleft obligations over network interactions (SaaS/Cloud), requiring disclosure of server source code. Commercial audits require strict automated OSS dependency scanning (Black Duck, Snyk, FOSSA).

---

<a name="network-hardware-firewalls"></a>
# 📦 SKILL: network-hardware-firewalls
*Domain:* **Enterprise Network & Firewalls**

---
name: network-hardware-firewalls
description: >-
  Enterprise network engineering, routing and switching for Cisco (IOS-XE, ASA, Firepower), Ubiquiti UniFi (UDM, switches, VLAN isolation, traffic rules), TP-Link Omada SDN, physical/virtual firewalls (FortiGate, pfSense/OPNsense, MikroTik RouterOS v7), Linux nftables/iptables, and Windows Advanced Firewall.
---
# Enterprise Network Hardware, Routing & Firewall Engineering

A comprehensive operational guide for designing, deploying, hardening, and troubleshooting enterprise and branch network infrastructure across physical appliances, SDN ecosystems, next-generation firewalls, and host-level packet filters.

---

## 1. Cisco Enterprise Routing, Switching & Edge Security

### Core IOS-XE Switching & VLAN Segmentation:
```ios
! Configure VLANs with standard naming and security isolation
vlan 10
 name CORPORATE_DATA
vlan 20
 name MANAGEMENT_INFRA
vlan 30
 name IOT_ISOLATED
vlan 99
 name NATIVE_UNUSED
exit

! Trunk Port Configuration (802.1Q) to Upstream Firewall / Core Switch
interface GigabitEthernet0/0/1
 description TRUNK-TO-FIREWALL
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30
 switchport nonegotiate
 no shutdown
exit

! Hardened Access Port with Port Security
interface GigabitEthernet0/0/2
 description WORKSTATION-SECURE
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security mac-address sticky
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit
```

### Layer 2 Infrastructure Protection (DHCP Snooping & DAI):
```ios
! Prevent rogue DHCP servers and ARP spoofing
ip dhcp snooping
ip dhcp snooping vlan 10,20,30
no ip dhcp snooping information option

! Set uplink trunk as trusted DHCP port
interface GigabitEthernet0/0/1
 ip dhcp snooping trust
 ip arp inspection trust
exit

! Enable Dynamic ARP Inspection (DAI)
ip arp inspection vlan 10,20,30
ip arp inspection validate src-mac dst-mac ip
```

### Cisco IOS-XE Routing & Access Control Lists (ACLs):
```ios
! Standard Named Extended Access Control List
ip access-list extended BLOCK_IOT_TO_LAN
 remark Allow established return traffic
 permit tcp 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 established
 remark Allow DNS to local resolver only
 permit udp 192.168.30.0 0.0.0.255 host 192.168.10.5 eq 53
 remark Block all other cross-VLAN traffic
 deny ip 192.168.30.0 0.0.0.255 192.168.0.0 0.0.255.255
 remark Allow IoT outbound to WAN
 permit ip 192.168.30.0 0.0.0.255 any
exit

! IPsec Site-to-Site Tunnel Interface (VTI) on IOS-XE
crypto ikev2 proposal IKEV2-AES-GCM
 encryption aes-gcm-256
 prf sha384
 group 19 20
exit

crypto ikev2 policy IKEV2-POLICY
 proposal IKEV2-AES-GCM
exit

crypto ikev2 profile IKEV2-PROFILE
 match identity remote address <REMOTE_PEER_IP> 255.255.255.255
 identity local address <LOCAL_PUBLIC_IP>
 authentication remote pre-share key <PRE_SHARED_KEY>
 authentication local pre-share key <PRE_SHARED_KEY>
 lifetime 86400
exit

crypto ipsec transform-set TS-AES-GCM esp-gcm 256
 mode tunnel
exit

crypto ipsec profile IPSEC-PROFILE
 set transform-set TS-AES-GCM
 set ikev2-profile IKEV2-PROFILE
exit

interface Tunnel100
 description SECURE-VTI-TUNNEL-BRANCH
 ip address 10.255.255.1 255.255.255.252
 tunnel source GigabitEthernet0/0/0
 tunnel mode ipsec ipv4
 tunnel destination <REMOTE_PEER_IP>
 tunnel protection ipsec profile IPSEC-PROFILE
 ip mtu 1400
 ip tcp adjust-mss 1360
exit
```

---

## 2. Ubiquiti UniFi Ecosystem & Enterprise Gateway Architecture

### Network Architecture & Architecture Matrix:
- **Topology Hierarchy**: UniFi Dream Machine (UDM Pro / SE) -> USW Enterprise/Pro Switch (10G SFP+ DAC / Optical trunk) -> U6/U7 Enterprise Access Points.
- **VLAN Isolation Model**:
  - `Default (VLAN 1)`: UniFi management plane only (Gateways, Switches, APs). Client access strictly prohibited.
  - `VLAN 10 (Corporate)`: Trusted corporate laptops and workstations. Full outbound WAN, managed inter-VLAN access.
  - `VLAN 20 (Servers/DMZ)`: Internal services, reverse proxies, NAS. Isolated with selective port forwarding.
  - `VLAN 30 (IoT)`: Smart devices, cameras, appliances. Total isolation from RFC1918 subnets, WAN access only.
  - `VLAN 40 (Guest)`: Isolated via Client Device Isolation (L2 isolation), captive portal or voucher system, bandwidth throttling.

### UniFi Firewall Rules Architecture (Rule Order & Execution):
UniFi processes firewall rules in strict order: **WAN / LAN / Guest** -> **In / Out / Local**.
1. **Rule 2000 (Drop Invalid State)**:
   - Type: `LAN In` | Action: `Drop` | Protocol: `All` | State: `Invalid`
2. **Rule 2001 (Allow Established & Related)**:
   - Type: `LAN In` | Action: `Accept` | Protocol: `All` | State: `Established`, `Related`
3. **Rule 2002 (Allow Inter-VLAN DNS/NTP to Core Server)**:
   - Type: `LAN In` | Action: `Accept` | Protocol: `UDP` | Source: `Any` | Destination: `Port Group: DNS_NTP (53, 123)` on Core Server IP.
4. **Rule 2003 (Block IoT to Private Subnets RFC1918)**:
   - Type: `LAN In` | Action: `Drop` | Source: `Network: IoT` | Destination: `Port/IP Group: RFC1918_ALL (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)`
5. **Rule 2004 (Block Gateway Web/SSH Access from Untrusted VLANs)**:
   - Type: `LAN Local` | Action: `Drop` | Source: `Networks: IoT, Guest` | Destination: `Port Group: MGMT_PORTS (22, 443, 80, 8443)`

### UniFi Edge Features & Advanced Services:
- **Deep Packet Inspection (DPI) & Traffic Rules**: Enforce application blocking (P2P, malicious domains, specific cloud apps) at wire speed.
- **Teleport & WireGuard VPN**: Native zero-configuration remote access using WireGuard protocol with ChaCha20-Poly1305 encryption.
- **mDNS Repeater / Reflector**: Enable selectively on IoT VLAN to allow Chromecast/AirPlay discovery from Corporate VLAN without opening full L2/L3 access.

---

## 3. TP-Link Omada SDN Infrastructure

### Omada Architecture & Deployment:
- **Centralized Controller**: Hardware (OC200, OC300), Software (Docker / Linux VM), or Omada Cloud-Based Controller.
- **Hardware Integration**: Multi-Gigabit VPN Gateways (ER605, ER7206, ER8411) + JetStream L2+/L3 Managed Switches + Omada EAP600/700 APs.

### Multi-WAN Load Balancing & Failover:
1. **Link Backup / Failover**: Primary WAN (High-speed Fiber) + Secondary WAN (Backup 5G/LTE or VDSL). Failover detection interval set to 3 seconds with DNS probe targets (`1.1.1.1`, `8.8.8.8`).
2. **Policy Routing**: Force critical server and administrative traffic through static IP on WAN1; offload streaming and general guest traffic to WAN2.

### Omada ACL Hierarchy & Rule Execution:
- **Gateway ACLs**: Apply at the router level for WAN and inter-network routing decisions.
- **Switch ACLs**: Hardware-enforced on JetStream switch ASICs. Eliminates inter-port communication at Layer 2 wire speed before packets even reach the gateway.
- **EAP ACLs**: Applied directly at wireless APs to isolate Wi-Fi clients from wired infrastructure.
- **Omada Isolation Matrix**:
  - Create IP Group: `RFC1918_Subnets` (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`).
  - Rule `LAN_Isolate_IoT`: Policy: `Deny` | Source: `Subnet_IoT` | Destination: `RFC1918_Subnets`.
  - Direction: Bidirectional isolation with allow established state.

---

## 4. Next-Generation Physical & Virtual Firewalls

### Fortinet FortiGate (FortiOS):
```fortios
# Configure Security Zones and VLAN Interface
config system interface
    edit "VLAN_CORP"
        set vdom "root"
        set ip 192.168.10.1 255.255.255.0
        set allowaccess ping
        set interface "port1"
        set vlanid 10
    next
end

# Hardened Firewall Policy with UTM Inspection
config firewall policy
    edit 10
        set name "CORP_TO_WAN_SECURE"
        set srcintf "VLAN_CORP"
        set dstintf "wan1"
        set action accept
        set srcaddr "all"
        set dstaddr "all"
        set schedule "always"
        set service "ALL"
        set utm-status enable
        set ssl-ssh-profile "deep-inspection"
        set av-profile "default"
        set ips-sensor "high_security"
        set application-list "default"
        set nat enable
    next
end
```

### pfSense & OPNsense (Packet Filter - pf):
- **Aliases**: Centralize IP, port, and URL table aliases for dynamic firewall rules (e.g., `Spamhaus_DROP`, `Emerging_Threats`).
- **pf Rules Processing**: First match wins for rules with `quick` keyword.
- **High Availability (CARP & XMLRPC Sync)**:
  - Configure redundant master/backup nodes sharing Virtual IPs via CARP (Common Address Redundancy Protocol).
  - PFSYNC synchronizes state tables in real time over a dedicated crossover link. Node failover causes zero dropped TCP connections.
- **Intrusion Detection (Suricata / Snort)**:
  - Run in Inline IPS Mode using Netmap driver.
  - Automatically drop malicious signatures (ET Open, Snort Community, Abuse.ch SSLBL).

### MikroTik RouterOS v7:
```routeros
# FastTrack & State Tracking Hardening
/ip firewall filter
add chain=input action=accept connection-state=established,related,untracked comment="Accept established, related"
add chain=input action=drop connection-state=invalid comment="Drop invalid"
add chain=input action=accept protocol=icmp comment="Allow ICMP"
add chain=input action=accept protocol=udp dst-port=13231 comment="Allow WireGuard"
add chain=input action=drop in-interface-list=WAN comment="Drop all other WAN traffic"

add chain=forward action=fasttrack-connection connection-state=established,related hw-offload=yes comment="FastTrack Hardware Offload"
add chain=forward action=accept connection-state=established,related,untracked
add chain=forward action=drop connection-state=invalid

# Raw Pre-routing Table for SYN-Flood and Port Scan Mitigation
/ip firewall raw
add chain=prerouting action=drop tcp-flags=fin,syn,rst,psh,ack,urg,!fin,!syn,!rst,!psh,!ack,!urg comment="Drop NULL packets"
add chain=prerouting action=drop tcp-flags=fin,syn,!rst,!psh,!ack,!urg comment="Drop SYN-FIN packets"
add chain=prerouting action=drop in-interface-list=WAN src-address-list=black_list comment="Drop blacklisted IPs"
```

---

## 5. Modern Host-Level Firewalls (Linux & Windows)

### Linux `nftables` Enterprise Ruleset (`/etc/nftables.conf`):
```nftables
#!/usr/sbin/nft -f
flush ruleset

table inet filter {
    # Dynamic set for rate limiting and brute-force banning
    set ban_list {
        type ipv4_addr
        flags timeout
    }

    chain input {
        type filter hook input priority filter; policy drop;

        # Connection state tracking
        ct state established,related accept
        ct state invalid drop

        # Loopback interface
        iif "lo" accept

        # Rate-limited ICMP
        ip protocol icmp icmp type { echo-request, echo-reply } limit rate 5/second accept
        ip6 nexthdr ipv6-icmp accept

        # Drop and ban SSH brute-force attackers (>5 attempts in 1 minute -> ban 1 hour)
        tcp dport 22 ct state new,untracked meter ssh_meter { ip saddr limit rate over 5/minute } add @ban_list { ip saddr timeout 1h } drop
        ip saddr @ban_list drop

        # Hardened management access
        tcp dport 22 accept
        tcp dport { 80, 443 } accept
    }

    chain forward {
        type filter hook forward priority filter; policy drop;
    }

    chain output {
        type filter hook output priority filter; policy accept;
    }
}
```

### Windows Advanced Firewall Hardening via PowerShell:
```powershell
# Enforce Outbound and Inbound Drop by Default on all profiles
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
Set-NetFirewallProfile -Profile Domain,Public,Private -DefaultInboundAction Block
Set-NetFirewallProfile -Profile Public -DefaultOutboundAction Block

# Enable logging of dropped packets
Set-NetFirewallProfile -Profile Domain,Public,Private -LogFileName "%SystemRoot%\system32\LogFiles\Firewall\pfirewall.log" -LogMaxSizeKilobytes 32768 -LogDroppedConnections True

# Allow Outbound DNS, HTTP, HTTPS for system updates only
New-NetFirewallRule -DisplayName "Outbound-Core-DNS" -Direction Outbound -Action Allow -Protocol UDP -RemotePort 53
New-NetFirewallRule -DisplayName "Outbound-Core-HTTP-HTTPS" -Direction Outbound -Action Allow -Protocol TCP -RemotePort 80,443

# Allow Inbound Hardened Management from Specific Administrative Subnet
New-NetFirewallRule -DisplayName "MGMT-Inbound-WinRM-Hardened" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 5986 -RemoteAddress 192.168.20.0/24

---

<a name="neurology-neurosurgery-triage"></a>
# 📦 SKILL: neurology-neurosurgery-triage
*Domain:* **Clinical Medicine**

---
name: neurology-neurosurgery-triage
description: >-
  Neurology, neurosurgery, stroke management (thrombolysis, mechanical thrombectomy), intracranial pressure, traumatic brain injuries (epidural/subdural hematomas), cranial nerves, and emergency triage (SNOOP4 headache red flags).
---
# Neurology, Neurosurgery & Emergency Clinical Triage

A master clinical manual for evaluating acute neurological emergencies, acute stroke protocols, brain injury mechanics, neurosurgical interventions, intracranial pressure crises, and systematic symptom triage.

---

## 1. Acute Cerebrovascular Accidents (Stroke Protocol)

Time is brain: approximately 1.9 million neurons are lost for every minute acute cerebral ischemia goes untreated.

### A. Stroke Classification:
1. **Ischemic Stroke (85%)**: Thrombotic or embolic occlusion of a cerebral artery.
2. **Hemorrhagic Stroke (15%)**:
   - **Intracerebral Hemorrhage (ICH - 10%)**: Rupture of deep penetrating arterioles damaged by chronic hypertension (Charcot-Bouchard microaneurysms) or cerebral amyloid angiopathy (lobar hemorrhages in the elderly).
   - **Subarachnoid Hemorrhage (SAH - 5%)**: Rupture of a saccular "berry" aneurysm at Circle of Willis bifurcations or arteriovenous malformation (AVM).

### B. Pre-Hospital & Emergency Triage:
- **FAST Assessment**:
  - **F (Face)**: Facial asymmetry, unilateral corner of mouth droop when asked to smile.
  - **A (Arms)**: Pronator drift; patient closes eyes and extends both arms forward palms up for 10 seconds. Unilateral downward drift or pronation indicates motor cortex / corticospinal pathway lesion.
  - **S (Speech)**: Slurred, dysarthric, or aphasic speech (Broca's expressive vs. Wernicke's receptive aphasia).
  - **T (Time)**: Record exact time last known well / symptom onset. Activate emergency medical services (**155 / 112**).

### C. Hyperacute Reperfusion Windows:
1. **Intravenous Thrombolysis (IVT)** with recombinant tissue plasminogen activator (**rtPA / Alteplase** 0.9 mg/kg or Tenecteplase):
   - **Window**: Within **4.5 hours** of witnessed symptom onset.
   - **Key Absolute Contraindications**: Acute intracranial hemorrhage on non-contrast CT, active internal bleeding, stroke or severe head trauma within past 3 months, history of intracranial hemorrhage, blood pressure $> 185/110\text{ mmHg}$ refractory to IV antihypertensives, platelets $< 100 \times 10^9\text{/L}$, INR $> 1.7$, therapeutic use of direct oral anticoagulants (DOAC) within 48 hours.
2. **Endovascular Mechanical Thrombectomy (EVT)**:
   - Catheter-based retrieval of large thrombus using stent-retrievers and aspiration catheters.
   - **Standard Window**: Within **6 hours** for Large Vessel Occlusion (LVO) of the internal carotid artery (ICA) or middle cerebral artery (MCA-M1).
   - **Extended Window (6 to 24 hours)**: Under DAWN / DEFUSE-3 clinical criteria utilizing CT/MR perfusion imaging showing a significant mismatch between salvageable ischemic penumbra and small non-viable ischemic core.

---

## 2. Neurosurgery: Intracranial Pressure & Hemorrhagic Emergencies

### A. The Monro-Kellie Doctrine & Elevated Intracranial Pressure (ICP):
The rigid, non-compliant adult cranium contains three fixed components:
$$\text{Volume}_{\text{intracranial}} = V_{\text{brain}} (80\%) + V_{\text{blood}} (10\%) + V_{\text{CSF}} (10\%) = \text{Constant}$$
- **Normal ICP**: **$5–15\text{ mmHg}$**. Pathological threshold requiring active intervention: **$> 20–22\text{ mmHg}$**.
- **Cerebral Perfusion Pressure (CPP)**:
  $$\text{CPP} = \text{Mean Arterial Pressure (MAP)} - \text{ICP}$$
  Target CPP in neuro-trauma is maintained at **$60–70\text{ mmHg}$**.
- **Cushing's Triad (Sign of Impending Brainstem Herniation)**:
  1. **Marked Arterial Hypertension** (compensatory sympathetic surge to maintain CPP, with widened pulse pressure).
  2. **Bradycardia** (reflex baroreceptor vagal stimulation).
  3. **Irregular, Depressed Respiration** (Cheyne-Stokes or ataxic breathing due to medullary compression).

### B. Traumatic Extra-Axial Hematomas:
- **Epidural Hematoma (EDH)**:
  - **Vessel**: Rupture of the **Middle Meningeal Artery (MMA)** secondary to a temporal bone fracture at the pterion.
  - **CT Appearance**: High-density **biconvex (lenticular / lemon-shaped)** collection limited by cranial sutures (periosteum tightly adhered to sutures).
  - **Clinical Course**: Classical "lucid interval" (momentary concussive loss of consciousness -> temporary recovery of lucidity for hours -> rapid neurological deterioration into coma with ipsilateral fixed dilated pupil / "blown pupil" from uncal herniation compressing CN III).
  - **Intervention**: Emergent decompressive craniotomy with surgical clot evacuation and arterial ligation.
- **Subdural Hematoma (SDH)**:
  - **Vessel**: Tearing of **cortical bridging veins** crossing the subdural space to the superior sagittal sinus.
  - **CT Appearance**: **Crescent-shaped (concave / banana-shaped)** collection extending freely across suture lines along the cerebral hemisphere.
  - **Acute SDH**: High-density hyperdense collection from high-energy acceleration-deceleration trauma; high mortality.
  - **Chronic SDH**: Hypodense or isodense collection in elderly patients or alcoholics following minor, often forgotten falls; insidious onset of cognitive decline, gait ataxia, and headache. Treated via burr hole drainage.

### C. Aneurysmal Subarachnoid Hemorrhage (aSAH):
- **Symptom**: Sudden, explosive onset of maximum intensity headache (**"Thunderclap Headache"**, reaching 10/10 peak within seconds; "worst headache of my life").
- **Diagnostic Protocol**: Immediate non-contrast brain CT (sensitivity $> 98\%$ within 6 hours). If CT is negative but clinical suspicion remains high, perform Lumbar Puncture (LP) after 6–12 hours to detect **xanthochromia** (yellow CSF discoloration from spectrophotometric hemoglobin breakdown).
- **Neurosurgical Repair**: Urgent digital subtraction angiography (DSA) followed by **Endovascular Coiling** (filling aneurysm lumen with detachable platinum coils) or **Open Microsurgical Clipping** across aneurysm neck to prevent re-bleeding.

---

## 3. Cranial Nerves & Clinical Neurological Examination

Systematic assessment:
- **CN I (Olfactory)**: Smell testing.
- **CN II (Optic)**: Visual acuity, visual fields by confrontation, pupillary light reflex (afferent limb), fundoscopy.
- **CN III, IV, VI (Oculomotor, Trochlear, Abducens)**: Extraocular movements, ptosis, pupillary constriction (efferent CN III).
  - CN III Palsy: Down-and-out eye position, complete ptosis, dilated non-reactive pupil (Emergency rule: painful "blown pupil" is a Posterior Communicating Artery aneurysm compressing CN III until proven otherwise!).
  - CN VI Palsy: Inability to abduct the eye laterally (diplopia on lateral gaze; sensitive early marker of elevated ICP).
- **CN V (Trigeminal)**: Facial sensation (V1, V2, V3 branches), corneal reflex (sensory limb), muscles of mastication.
- **CN VII (Facial)**: Muscles of facial expression.
  - **Central Facial Palsy** (Stroke): Forehead wrinkling is **spared** (bilateral cortical innervation to upper face); only lower face droops.
  - **Peripheral Facial Palsy** (Bell's Palsy): **Entire ipsilateral half of face is paralyzed**, including inability to wrinkle forehead or close the eye (Bell's phenomenon).
- **CN VIII (Vestibulocochlear)**: Hearing (Weber & Rinne tuning fork tests) and vestibular balance.
- **CN IX, X (Glossopharyngeal, Vagus)**: Palatal elevation, uvula deviation (deviates away from side of lesion), gag reflex, swallowing.
- **CN XI (Accessory)**: Trapezius and Sternocleidomastoid strength (shoulder shrug, head turn against resistance).
- **CN XII (Hypoglossal)**: Tongue protrusion (deviates **toward** the side of a peripheral lesion / "licks the lesion").

---

## 4. Emergency Headache Triage: The SNOOP4 Red Flag Rule

When evaluating any headache, systematically check the **SNOOP4** criteria. A positive finding demands urgent neuroimaging (CT/MRI) and medical workup:

- **S (Systemic Symptoms)**: Fever, night sweats, unexplained weight loss, or known systemic cancer / immunocompromised status (HIV).
- **N (Neurologic Symptoms / Signs)**: Focal weakness, sensory loss, confusion, altered mental status, seizures, or papilledema on fundus exam.
- **O (Onset Sudden / Abrupt)**: Reaches peak intensity in $< 1\text{ minute}$ ("Thunderclap Headache" - rule out SAH, cerebral venous sinus thrombosis, cervical artery dissection).
- **O (Older Age of Onset)**: New onset headache in a patient **$> 50\text{ years}$**. (Must rule out **Giant Cell / Temporal Arteritis**: scalp tenderness, jaw claudication, elevated ESR $> 50\text{ mm/h}$; requires immediate high-dose corticosteroids to prevent permanent ischemic optic neuropathy / blindness!).
- **P4 (Pattern Change & Positional Characteristics)**:
  - **Progressive**: Headache frequency and severity worsening steadily over weeks.
  - **Positional**: Worsens markedly when recumbent / lying flat (suggests elevated ICP or mass lesion) or worsens upright (suggests spontaneous intracranial hypotension / low CSF leak).
  - **Papilledema**: Swollen optic discs indicating elevated intracranial pressure.
  - **Precipitated by Valsalva**: Triggered by coughing, sneezing, bending over, or strenuous exercise (rule out Chiari malformation or posterior fossa lesion).

---

<a name="ophthalmology-vision-care"></a>
# 📦 SKILL: ophthalmology-vision-care
*Domain:* **Clinical Medicine**

---
name: ophthalmology-vision-care
description: >-
  Ophthalmology, vision diagnostics, glaucoma, intraocular pressure management, retinal diseases (hypertensive/diabetic retinopathy, retinal detachment), macular degeneration, cataracts, and dry eye syndrome.
---
# Clinical Ophthalmology, Vision Disorders & Retinal Pathologies

A comprehensive clinical manual for evaluating ocular complaints, measuring intraocular pressure, screening for sight-threatening retinal and vascular emergencies, and managing common anterior and posterior segment pathologies.

---

## 1. Anatomy of the Eye & Optical Pathway

Key anatomical structures and their clinical significance:
- **Cornea**: Main refractive element of the eye ($\approx 43\text{ diopters}$); completely avascular, nourished by tears and anterior chamber aqueous humor.
- **Anterior Chamber & Trabecular Meshwork**: The iridocorneal angle contains the trabecular meshwork draining aqueous humor into Schlemm's canal to maintain Intraocular Pressure (IOP).
- **Crystalline Lens**: Provides dynamic optical accommodation ($\approx 15–20\text{ diopters}$).
- **Vitreous Body**: Gel filling the posterior segment; liquefies and detaches with age (Posterior Vitreous Detachment - PVD).
- **Retina & Macula Lutea**: High-resolution neural sensory layer. The **Fovea centralis** (center of the macula) contains only high-density cones for fine detail and color vision.
- **Optic Disc**: Exit point of retinal ganglion cell axons forming the optic nerve (CN II). Contains no photoreceptors (physiological blind spot).

---

## 2. Intraocular Pressure (IOP) & Glaucoma (*Zelený zákal*)

Glaucoma is an optic neuropathy characterized by progressive loss of retinal ganglion cells, characteristic optic nerve cupping, and irreversible visual field deficits.

### A. Tonometry & Clinical Parameters:
- **Normal Intraocular Pressure**: **$10–21\text{ mmHg}$** (measured via Goldmann applanation tonometry - the gold standard).
- **Cup-to-Disc Ratio (C/D Ratio)**:
  - Normal: $\le 0.3–0.4$.
  - Pathological: $> 0.5–0.6$ or asymmetry $> 0.2$ between eyes suggests glaucomatous optic nerve atrophy.
  - Thinning of the neuroretinal rim obeys the ISNT rule (Inferior $\ge$ Superior $\ge$ Nasal $\ge$ Temporal in healthy eyes; violation of ISNT indicates rim loss).

### B. Primary Open-Angle Glaucoma (POAG):
- The "Silent Thief of Sight": Completely painless, normal anterior chamber angle, insidious progression.
- Progressive visual field loss: Begins with arcuate scotomas and nasal step; progresses to severe peripheral constriction (**tunnel vision**). Central vision is preserved until terminal stages.

### C. Acute Angle-Closure Glaucoma (Ophthalmic Emergency):
- **Pathophysiology**: Pupillary block causes the iris root to bow forward, completely obstructing the trabecular meshwork. IOP spikes acutely to **$40–80\text{ mmHg}$**.
- **Clinical Symptoms**:
  - Severe unilateral deep ocular pain and ipsilateral headache.
  - Nausea and vomiting (often misdiagnosed as acute migraine or abdominal crisis).
  - Blurred vision with characteristic **rainbow-colored halos around lights**.
  - Ocular examination: Red injected conjunctiva, cloudy steamy cornea, mid-dilated non-reactive pupil, eyeball feels **stony hard** on digital palpation.
- **Emergency Medical Management**:
  1. IV Mannitol 20% (1–2 g/kg) to draw fluid osmotically from the vitreous.
  2. Oral/IV Acetazolamide (Diamox 500 mg) to inhibit aqueous humor secretion.
  3. Topical eye drops: Pilocarpine 2% (miotic to pull iris away from angle), Timolol 0.5%, Apraclonidine 1%.
  4. Definitive surgical intervention: Laser Peripheral Iridotomy (LPI) in both affected and contralateral fellow eye.

### D. Glaucoma Pharmacotherapy:
- **Prostaglandin Analogs** (*Latanoprost, Bimatoprost, Travoprost*): First-line; increases uveoscleral outflow. Once daily at bedtime. (Side effects: iris darkening, eyelash lengthening).
- **Beta-Blockers** (*Timolol 0.25%–0.5%*): Decreases aqueous humor production. (Contraindicated in bronchial asthma, severe COPD, bradycardia, or 2nd/3rd degree AV block).
- **Carbonic Anhydrase Inhibitors** (*Dorzolamide, Brinzolamide*): Inhibits active secretion of bicarbonate into aqueous humor.
- **Alpha-2 Agonists** (*Brimonidine*): Dual action (reduces production and increases uveoscleral outflow).

---

## 3. Retinal & Systemic Vascular Pathologies

The retina is the only place in the human body where microvasculature can be visualized directly and non-invasively.

### A. Hypertensive Retinopathy (Keith-Wagener-Barker Classification):
Reflects systemic damage occurring simultaneously in cerebral, coronary, and renal microcirculation:
- **Grade 1**: Generalized, mild arteriolar attenuation and tortuosity ("silver/copper wiring").
- **Grade 2**: Definite focal arteriolar narrowing and arteriovenous (AV) crossing changes (*Salus-Gunn sign* - vein deflection and compression at crossings).
- **Grade 3**: Flame-shaped retinal hemorrhages, hard lipid exudates (macular star), and **cotton-wool spots** (microinfarcts of the nerve fiber layer).
- **Grade 4**: All of Grade 3 plus **Papilledema (bilateral optic disc swelling)**. Indicates malignant / accelerated hypertension requiring immediate ICU admission!

### B. Retinal Detachment (*Odchlípení sítnice* - Emergency):
- Separation of the neurosensory retina from the underlying retinal pigment epithelium (RPE).
- **The Classical Warning Triad**:
  1. **Photopsia**: Sudden persistent flashes of light in peripheral vision.
  2. **Sudden shower of floaters**: New onset of dense black spots, webs, or "soot shower" (vitreous hemorrhage).
  3. **Visual field defect**: A dark, painless "curtain" or shadow spreading from the periphery toward the center.
- **Immediate Action**: Patient must remain quiet; emergency referral to vitreoretinal surgery (Pneumatic retinopexy, Pars Plana Vitrectomy - PPV, or Scleral Buckle).

### C. Age-Related Macular Degeneration (AMD / *Makulární degenerace*):
- Leading cause of irreversible central blindness in individuals $> 60$ years.
- **Dry (Non-neovascular) AMD (85–90%)**:
  - Deposition of yellowish metabolic waste products (**Drusen**) beneath the RPE.
  - Slow progressive loss of central vision; metamorphopsia (straight lines appear wavy on an **Amsler grid**).
- **Wet (Neovascular / Exudative) AMD (10–15%)**:
  - Growth of abnormal choroidal neovascular membranes (CNV) breaking through Bruch's membrane, leaking blood and lipid.
  - Sudden, rapid loss of central vision.
  - Treatment: Immediate **anti-VEGF intravitreal injections** (*Aflibercept / Eylea, Ranibizumab / Lucentis, Faricimab*) administered directly into the vitreous cavity under sterile conditions to halt neovascularization.

---

## 4. Anterior Segment & Refractive Conditions

### A. Cataracts (*Šedý zákal*):
- Progressive clouding and opacification of the natural crystalline lens (nuclear sclerosis, cortical, or posterior subcapsular).
- Symptoms: Gradual painless blurring, glare and halos around headlights at night, loss of color contrast.
- Definitive Treatment: **Phacoemulsification** with ultrasound breakdown of the cloudy lens through a micro-incision ($< 2.2\text{ mm}$), followed by folding and implantation of an artificial Intraocular Lens (IOL - Monofocal, Toric for astigmatism, or Multifocal).

### B. Dry Eye Syndrome & Computer Vision Syndrome:
- Etiology: Evaporative dry eye due to **Meibomian Gland Dysfunction (MGD)** (poor lipid layer causes rapid tear evaporation) or Aqueous-deficient dry eye (Sjögren's syndrome, aging).
- Diagnosis: **Tear Break-Up Time (TBUT)**: Fluorescein instilled; TBUT $< 10\text{ seconds}$ indicates unstable tear film.
- Management:
  - Preservative-free artificial tears containing high-concentration **Hyaluronic Acid (0.15%–0.3%)** or lipid-containing emulsions.
  - Eyelid hygiene: Warm compresses (10 minutes) followed by gentle eyelid margin massage to melt inspissated meibomian wax.
  - Ergonomics: The **20-20-20 Rule** (every 20 minutes, look at an object 20 feet / 6 meters away for at least 20 seconds).

---

<a name="orthopedics-knee-rehab"></a>
# 📦 SKILL: orthopedics-knee-rehab
*Domain:* **Clinical Medicine**

---
name: orthopedics-knee-rehab
description: >-
  Orthopedics, knee joint anatomy, pathology (meniscus, ACL/PCL, gonarthrosis, chondromalacia), clinical tests (Lachman, McMurray), imaging, conservative therapies (PRP, hyaluronic acid), arthroscopy, and rehabilitation protocols.
---
# Clinical Orthopedics, Knee Pathology & Rehabilitation

A master clinical and surgical reference for diagnosing knee pain, evaluating ligamentous and meniscal injuries, managing knee osteoarthritis (gonarthrosis), interpreting imaging, and guiding rehabilitation protocols.

---

## 1. Functional Anatomy & Biomechanics of the Knee

The knee joint comprises two primary articulations:
1. **Tibiofemoral Joint**: Weight-bearing articulation between femoral condyles and tibial plateau.
2. **Patellofemoral Joint**: Articulation between the patella and the femoral trochlear groove; acts as a biomechanical lever maximizing quadriceps extensor mechanical advantage.

### Critical Stabilizing Structures:
- **Anterior Cruciate Ligament (ACL / *Přední zkřížený vaz*)**:
  - Originates from medial wall of lateral femoral condyle; inserts anteriorly on tibial intercondylar area.
  - Primary restraint against **anterior tibial translation** and secondary restraint against internal tibial rotation.
- **Posterior Cruciate Ligament (PCL / *Zadní zkřížený vaz*)**:
  - Stronger than ACL; primary restraint against **posterior tibial displacement**.
- **Collateral Ligaments**:
  - Medial Collateral Ligament (**MCL**): Resists valgus (inward collapse) forces.
  - Lateral Collateral Ligament (**LCL**): Resists varus (outward bowing) forces.
- **Menisci (Fibrocartilaginous Shock Absorbers)**:
  - **Medial Meniscus**: C-shaped, larger diameter, firmly attached to joint capsule and deep MCL fibers; significantly less mobile and more prone to degenerative and shear tears.
  - **Lateral Meniscus**: O-shaped, more circular, mobile, not attached to LCL.
  - **Vascular Zones**:
    - **Red-Red Zone (Outer 10–30%)**: Good blood supply from genicular arteries; high potential for surgical suture repair.
    - **Red-White Zone (Middle third)**: Marginal vascularity; repairable in young patients.
    - **White-White Zone (Inner two-thirds)**: Completely avascular; nourished exclusively by synovial fluid diffusion. Does not heal; symptomatic tears require conservative therapy or minimal partial resection (*parciální menisektomie*).

---

## 2. Orthopedic Physical Examination & Special Tests

Perform systematically with the patient relaxed in supine position:

### A. Effusion & Fluid Assessment:
- **Ballottement Test (Patellar Tap)**: Compress suprapatellar pouch downwards; push patella sharply against femur. A distinct tap or bounce indicates moderate-to-large intra-articular joint effusion (*hydrops / hemartros*).
- **Bulge Sign (Wipe Test)**: Stroke medial side of knee upwards 2-3 times to milk fluid; stroke lateral side downwards. A wave or bulge appearing on the medial side indicates small fluid effusion (4–8 ml).

### B. Cruciate Ligament Stability Tests:
- **Lachman Test (Gold Standard for ACL tear, sensitivity 85–95%)**:
  - Knee flexed to **$20^\circ–30^\circ$**. Stabilize distal femur with one hand; pull proximal tibia anteriorly with the other.
  - Positive finding: Increased anterior translation with a **soft, mushy endpoint** (compared to a crisp, firm endpoint in the healthy contralateral knee).
- **Anterior Drawer Test**: Knee flexed to $90^\circ$, foot stabilized on table. Pull tibia forward. (Less sensitive than Lachman due to hamstring spasm and meniscal wedging).
- **Pivot-Shift Test**: Pathognomonic for functional rotational ACL instability (requires high relaxation).
- **Posterior Drawer & Sag Sign (Godfrey's Test)**: Knee flexed to $90^\circ$. Observer looks from lateral profile. If the proximal tibia sags posteriorly relative to the femoral condyles, the PCL is torn.

### C. Meniscal Examination:
- **McMurray Test**:
  - Knee maximally flexed. Apply external rotation and valgus stress while extending knee -> tests **medial meniscus**. Apply internal rotation and varus stress while extending -> tests **lateral meniscus**.
  - Positive finding: Palpable or audible "clunk", snap, or sharp pain along the joint line.
- **Joint Line Tenderness**: Precise palpation along the medial and lateral joint lines. Highly sensitive for meniscal injury.
- **Thessaly Test**: Patient stands on injured leg flexed to $20^\circ$ and rotates torso internally/externally three times. Joint line discomfort indicates meniscal pathology.

---

## 3. Knee Pathologies & Differential Diagnosis

### A. Knee Osteoarthritis (*Gonartróza*):
- Progressive degeneration of articular cartilage, subchondral bone sclerosis, osteophyte formation, and synovial inflammation.
- **Kellgren-Lawrence Radiographic Grading**:
  - **Grade 1**: Doubtful narrowing of joint space, possible osteophytic lipping.
  - **Grade 2**: Definite osteophytes, possible joint space narrowing.
  - **Grade 3**: Moderate multiple osteophytes, definite joint space narrowing, some subchondral sclerosis.
  - **Grade 4**: Severe joint space narrowing (bone-on-bone contact), large osteophytes, severe subchondral sclerosis, bony deformities.
- **Standard Imaging**: Weight-bearing standing AP and lateral radiographs; 45° flexed PA view (Rosenberg view) best visualizes cartilage loss in the posterior weight-bearing condyles.

### B. Chondromalacia Patellae & Patellofemoral Pain Syndrome (PFPS):
- Softening, fissuring, and erosion of the retro-patellar hyaline cartilage.
- Clinical presentation: Retropatellar or peripatellar aching pain exacerbated by descending stairs, squatting, kneeling, or prolonged sitting with flexed knees ("movie sign" / "theater sign").
- Etiology: Patellar maltracking, vastus medialis oblique (VMO) weakness, tight lateral retinaculum, increased Q-angle, overpronation of the foot.

### C. Baker's Cyst (Popliteal Cyst):
- Distension of the gastrocnemius-semimembranosus bursa in the popliteal fossa.
- **Crucial Rule**: In adults, a Baker's cyst is almost always secondary to an underlying intra-articular pathology (meniscal tear, cartilage degeneration) causing chronic effusion.
- **Red Flag**: A ruptured Baker's cyst presents with acute calf swelling, erythema, and pain, mimicking Deep Vein Thrombosis (DVT). Must perform venous Doppler ultrasound to differentiate.

---

## 4. Conservative & Biological Therapies

### A. Intra-Articular Injections:
1. **Hyaluronic Acid (HA / Viscosupplementation)**:
   - High-molecular-weight cross-linked HA mimics natural synovial fluid viscoelasticity, stimulates endogenous hyaluronan production, and reduces cartilage shear stress.
   - Indicated primarily for mild-to-moderate gonarthrosis (Grade 1 to 3) and chondromalacia.
2. **Platelet-Rich Plasma (PRP / ACP)**:
   - Autologous plasma centrifuged to concentrate platelets 3–6 times baseline.
   - Degranulation releases growth factors (PDGF, TGF-$\beta$, VEGF, IGF-1) modulating inflammation and stimulating tissue repair. Superior long-term pain relief (6–12 months) compared to corticosteroids in early osteoarthritis.
3. **Corticosteroids (Triamcinolone, Betamethasone)**:
   - Potent, rapid anti-inflammatory relief during acute inflammatory flares with massive joint effusion.
   - **Clinical Warning**: Repeated intra-articular steroid injections are chondrotoxic and accelerate cartilage degeneration. Limit strictly to maximum 3–4 injections per year.

### B. Physiotherapy & Biomechanical Correction:
- Non-impact cardiovascular loading: Swimming, stationary cycling with high saddle height (minimizing patellofemoral compressive force).
- Target strengthening: Vastus Medialis Oblique (VMO), hip abductors (Gluteus Medius to prevent valgus knee collapse), and hamstring flexibility.
- Foot orthotics: Custom medial arch supports to correct excessive pronation that creates rotational torque at the knee joint.

---

## 5. Surgical Interventions & Rehabilitation Protocols

### A. Arthroscopic Surgery:
- **Partial Meniscectomy**: Debridement and contouring of non-repairable, avascular tears; preserving the maximal circumferential stable meniscal rim.
- **Meniscal Repair**: Suture anchors (all-inside, inside-out) for vascular peripheral tears. Requires restricted weight-bearing and limited flexion ($< 90^\circ$) for 4–6 weeks post-op.
- **ACL Reconstruction**: Anatomic replacement using autografts (semitendinosus/gracilis hamstring tendon or bone-patellar tendon-bone BTB).

### B. Knee Rehabilitation Protocol Phases:
- **Phase 1 (Weeks 0–2)**:
  - Swelling control (Cryotherapy, compression).
  - **Restore full passive knee extension** immediately (crucial to prevent flexion contractures).
  - Isometric quadriceps sets, straight leg raises (SLR) without extension lag.
- **Phase 2 (Weeks 2–6)**:
  - Progress active flexion to $120^\circ$.
  - Closed kinetic chain exercises (mini-squats $0–45^\circ$, leg press).
  - Stationary cycling as soon as $100^\circ$ flexion achieved.
- **Phase 3 (Weeks 6–12)**:
  - Proprioception and neuromuscular control (balance boards, Bosu ball).
  - Progressive resistance training; single-leg stability exercises.
- **Phase 4 (Months 3–6+)**:
  - Plyometrics, agility drills, running progression, sport-specific functional testing.

---

<a name="proctology-colorectal-surgery"></a>
# 📦 SKILL: proctology-colorectal-surgery
*Domain:* **Clinical Medicine**

---
name: proctology-colorectal-surgery
description: >-
  Clinical proctology, colorectal surgery, hemorrhoidal disease (Goligher stages 1-4), rubber band ligation, Longo stapled hemorrhoidopexy, HAL-RAR, laser LHP, Milligan-Morgan hemorrhoidectomy, anal fissures, perianal abscesses/fistulas, colonoscopy guidelines, and perioperative care.
---
# Clinical Proctology, Colorectal Surgery & Hemorrhoidal Disease

A master clinical, diagnostic, and surgical manual for evaluating anorectal pathology, staging hemorrhoidal disease, selecting operative and office-based interventions, interpreting endoscopy/colonoscopy findings, and managing perioperative care.

---

## 1. Functional Anatomy & Vascular Architecture of the Anorectum

### A. Vascular Anatomy:
1. **Superior Rectal Artery (SRA)**: Terminal continuation of the Inferior Mesenteric Artery (IMA). Supplies the upper rectum and divides into right anterior, right posterior, and left lateral branches (explaining the classic 3, 7, and 11 o'clock lithotomy positions of primary hemorrhoidal cushions).
2. **Middle Rectal Artery (MRA)**: Arises from the Internal Iliac Artery, supplying lower rectal musculature.
3. **Inferior Rectal Artery (IRA)**: Branch of the Internal Pudendal Artery, traversing the ischioanal fossa to supply the anal canal below the dentate line.
4. **Venous Drainage**:
   - **Internal Hemorrhoidal Plexus**: Drains into the superior rectal vein $\rightarrow$ Inferior Mesenteric Vein $\rightarrow$ Portal System (site of porto-caval anastomoses).
   - **External Hemorrhoidal Plexus**: Drains via inferior and middle rectal veins into the Internal Iliac Vein $\rightarrow$ Systemic IVC.

### B. Dentate (Pectinate) Line & Innervation Boundary:
- **Above Dentate Line**: Visceral innervation (autonomic nervous system). Insensitive to sharp pain, cutting, or burning; sensitive only to stretch/distension. Procedures here (Barron ligation, Longo PPH, HAL-RAR) are virtually painless.
- **Below Dentate Line**: Somatic innervation (inferior rectal nerves / pudendal nerve). Rich in nociceptive and tactile receptors. Any incision, excision, or suture placement below the dentate line causes acute, severe pain.
- **Anal Sphincters**:
  - **Internal Anal Sphincter (IAS)**: Smooth involuntary muscle, provides 70–80% of resting anal tone.
  - **External Anal Sphincter (EAS)**: Striated voluntary muscle, recruited for squeeze pressure and continence maintenance.

---

## 2. Hemorrhoidal Disease: Staging & Differential Diagnosis

Hemorrhoidal cushions (*corpus cavernosum recti*) are normal physiological vascular structures facilitating airtight continence. Disease occurs when supportive connective tissue (Treitz muscle / Parks ligament) degenerates, causing cushion enlargement and displacement.

### A. Goligher Clinical Staging (Internal Hemorrhoids):
- **Grade I**: Enlarged vascular cushions, painless bright red rectal bleeding (*rectorrhagia*) on toilet paper or stool surface. **No prolapse**.
- **Grade II**: Prolapse during defecation or straining, but **reduces spontaneously** back into the anal canal.
- **Grade III**: Prolapse during defecation, physical exertion, or coughing. **Requires manual digital reduction** (*musí se reponovat manuálně*).
- **Grade IV**: Permanent prolapse of hemorrhoidal tissue that **cannot be manually reduced** (irreducible), high risk of thrombosis, strangulation, ulceration, and mucus discharge.

### B. External Hemorrhoids & Acute Perianal Thrombosis:
- Arise below the dentate line, covered by squamous anoderm.
- **Acute Hemorrhoidal Thrombosis**: Sudden severe perianal pain associated with a firm, tender, bluish-purple subcutaneous nodule.
  - **Management within $\le 72$ hours of onset**: Immediate surgical excision (*trombektomie*) under local anesthesia provides rapid pain relief.
  - **Management after $> 72$ hours**: Clot organization has begun; conservative therapy (ice packs, topical lidocaine, flavonoids, stool softeners) is preferred as spontaneous resolution occurs in 2–3 weeks.

---

## 3. Conservative & Pharmacological Management

First-line therapy indicated for Grade I–II, or as bridging/supportive care for Grade III–IV:

1. **Dietary & Lifestyle Modification**:
   - High-fiber intake: 25–35 g/day (dietary fiber or soluble **Psyllium** husk with ample water).
   - Fluid intake: $\ge 2.0–2.5\text{ L/day}$.
   - Behavioral: Avoid prolonged sitting on the toilet ($< 3–5\text{ minutes}$), eliminate chronic straining.
2. **Phlebotonics (Micronized Purified Flavonoid Fraction - MPFF)**:
   - **Diosmin + Hesperidin (500 mg or 1000 mg)** (e.g. *Detralex, Diosmin*):
     - Acute flare protocol: $3000\text{ mg/day}$ (1000 mg 3x daily) for 4 days, then $2000\text{ mg/day}$ (1000 mg 2x daily) for 3 days.
     - Maintenance therapy: $1000\text{ mg/day}$ (e.g. 500 mg 2x daily or 1000 mg 1x daily) for 2–3 months.
     - Mechanism: Increases venous tone, improves lymphatic drainage, reduces capillary permeability and microvascular inflammation.
3. **Topical Formulations**:
   - Hyaluronic acid suppositories/ointments (*Proktis-M*): Promotes tissue re-epithelialization and healing.
   - Short-term corticosteroid/anesthetic ointments (hydrocortisone, cinchocaine, lidocaine): Limit use to $\le 7–10\text{ days}$ to prevent anoderm atrophy.

---

## 4. Office-Based Minimally Invasive Interventions

### A. Rubber Band Ligation (Barron Ligation / *Ligatura latexovými kroužky*):
- **Primary Indication**: Grade II and selected Grade III internal hemorrhoids.
- **Technique**: An elastic latex ring is applied tightly around the apex of the hemorrhoidal cushion at least 1.5–2.0 cm **above the dentate line** via anoscope.
- **Mechanism**: Ischemia leads to necrosis and sloughing of the cushion within 5–7 days, forming a scarred base that fixes mucosa to the muscularis.
- **Session Rule**: Typically 1–2 cushions banded per session; repeated at 4–6 week intervals to avoid severe vasovagal syncope or urinary retention.
- **Critical Red Flag**: Pelvic sepsis (Triad: severe pain, fever, urinary retention) requires urgent broad-spectrum IV antibiotics and surgical exploration.

### B. Sclerotherapy & Infrared Coagulation (IRC):
- Useful for bleeding Grade I–II cushions; polidocanol 1–3% injection into submucosa inducing aseptic fibrosis.

---

## 5. Surgical Interventions & Operative Decision Matrix

When conservative and office treatments fail, or for primary Grade III–IV disease:

### A. The Longo Procedure (PPH - Procedure for Prolapse and Hemorrhoids / Stapled Hemorrhoidopexy):
- **Indication**: Grade III internal hemorrhoids with circular mucosal prolapse (*cirkulární prolaps*).
- **Surgical Mechanism**:
  - A specialized circular stapling device (33 mm) is inserted transanally.
  - A pursestring suture is placed in the mucosa/submucosa 3–4 cm proximal to the dentate line.
  - The stapler excises a circular 2–3 cm sleeve of redundant rectal mucosa while simultaneously re-approximating the edges with a circular row of titanium staples.
  - **Effects**:
    1. Lifts and fixes prolapsed cushions back to their anatomical position (*hemorrhoidopexy*).
    2. Interrupts arterial blood flow from the superior rectal artery branches, causing subsequent cushion shrinkage.
- **Advantages**:
  - Substantially lower post-operative pain compared to excisional surgery (incision placed in insensitive visceral nerve zone above dentate line).
  - Rapid recovery: Return to normal physical activities within 5–7 days.
  - Preservation of the sensitive anoderm and anal transition zone.
- **Specific Risks**: Staple line bleeding (requires inspection and absorbable hemostatic oversewing), early fecal urgency or tenesmus (usually transient for 2–4 weeks), rare rectovaginal fistula.

### B. HAL-RAR (Doppler-Guided Hemorrhoidal Artery Ligation & Recto-Anal Repair):
- **Indication**: Grade II–IV internal hemorrhoids.
- **Technique**: A specialized proctoscope with a Doppler ultrasound probe identifies 6–8 terminal arterial branches at 2–3 cm above the dentate line. Suture ligation cuts off inflow (HAL). A continuous running mucopexy suture then lifts prolapsing cushions (RAR).
- **Advantages**: Completely non-excisional, no open surgical wounds, minimal pain, recovery within 3–5 days.

### C. Laser Hemorrhoidoplasty (LHP):
- **Technique**: A 1470 nm diode laser fiber is introduced into the hemorrhoidal cushion under mucosal puncture. Thermal energy coagulates the vascular plexus causing tissue contraction and submucosal fibrosis.
- **Advantages**: Minimal pain, outpatient setting, sphincter preservation.

### D. Excisional Hemorrhoidectomy (Milligan-Morgan / Ferguson):
- **Indication**: Severe Grade IV, mixed internal/external disease, extensive skin tags, or failed non-excisional interventions.
- **Technique**: Excision of hemorrhoidal bundles down to the internal sphincter. **Milligan-Morgan** leaves wounds open to heal by secondary intention; **Ferguson** closes anoderm with running absorbable sutures.
- **Advantages**: Gold standard for lowest recurrence rates ($< 3–5\%$).
- **Disadvantages**: Severe postoperative pain lasting 2–3 weeks, healing time 4–6 weeks, risk of anal stenosis or ectropion if excessive anoderm is removed.

---

## 6. Total Colonoscopy & Cancer Screening Protocol

Prior to performing elective proctological surgery in adult patients, thorough endoscopic screening is mandatory:
- **Mandatory Indications for Preoperative Colonoscopy**:
  1. Age $\ge 45–50$ years (routine colorectal screening threshold).
  2. Any "red flag" symptoms: Unexplained weight loss, iron deficiency anemia, altered bowel habits (new-onset diarrhea or constipation), tenesmus, family history of colorectal carcinoma (CRC) or Lynch syndrome.
  3. Dark blood or blood mixed within feces (melena / hematochezia), distinguishing from outlet bright red rectorrhagia.
- **Clinical Rationale**: Coexisting proximal colorectal adenocarcinoma, advanced adenomatous polyps, or Inflammatory Bowel Disease (Crohn's disease, Ulcerative Colitis) must be systematically excluded before undertaking anorectal surgery.

---

## 7. Perioperative Protocol & Anesthesia Preparation

1. **Preoperative Clearance (Předoperační vyšetření)**:
   - Complete Blood Count (Hb, Platelets), Coagulation profile (INR / Quick, aPTT, Fibrinogen), Basic biochemistry (Creatinine, Urea, Electrolytes, Glucose, ALT), ECG, Internal Medicine / GP sign-off within 14 days of surgery.
   - Antiplatelet/Anticoagulant management: Discontinue Clopidogrel 5–7 days prior; DOACs (Apixaban, Rivaroxaban) stopped 24–48 hours prior according to renal clearance.
2. **Bowel Preparation**:
   - Single or double phosphate enema (*Yal*, *Salinické klyzma*) on evening before and morning of surgery; full oral PEG lavage rarely required for purely proctological procedures unless combined with colonoscopy.
3. **Anesthesia Options**:
   - Saddle block (low spinal anesthesia) or short general laryngeal mask anesthesia (LMA).
4. **Postoperative Regimen**:
   - Multimodal analgesia: Paracetamol 1000 mg q6h + NSAIDs (Dexketoprofen / Ibuprofen) scheduled; weak opioid (Tramadol) for breakthrough.
   - Stool Management: Osmotic laxative (**Macrogol / Lactulose**) starting postoperative day 1 to ensure soft, formed stool; avoid both severe constipation and high-frequency liquid diarrhea.
   - Hygiene: Warm sitz baths (*sedací koupele* with chamomile or oak bark / *dubová kůra*) 2–3 times daily after bowel movements.

---

<a name="ru-accounting-tax"></a>
# 📦 SKILL: ru-accounting-tax
*Domain:* **Russian Accounting & Tax**

---
name: ru-accounting-tax
description: >-
  Russian accounting (RSBU/FSBU), corporate and personal taxation (OSNO, USN, PSN, AUSN, NPD), VAT, profit tax, progressive PIT, unified insurance premiums, Single Tax Account (ENS/ENP), reporting (6-NDFL, RSV, EFS-1), tax audits, fines, and Article 54.1 NK RF compliance.
---
# Russian Accounting, Taxation & Tax Audit Defense 

A comprehensive operational manual and regulatory reference for corporate accountants, chief financial officers (CFO), tax advisors, and auditors operating under the statutory legislation of the Russian Federation.

---

## 1. Statutory Architecture & Primary Regulatory Framework

Russian accounting and tax law is strictly formalized under federal codifications:
- **Tax Code of the Russian Federation (Tax Code of the Russian Federation - NK RF)**:
  - *Part I*: General principles of taxation, taxpayer rights and duties, tax control, inspections, Single Tax Account (ENS), and tax offenses (Articles 1–142).
  - *Part II*: Specific taxes and special tax regimes (Articles 143–346.53).
- **Federal Law No. 402-FZ "On Accounting" (Federal Law No. 402-FZ On Accounting)**: Mandatory bookkeeping standards, primary documentation (primary accounting documents), electronic signatures, and annual financial statements.
- **Federal Accounting Standards (Federal Accounting Standards - FSBU)**:
  - `FSBU 5/2019` "Inventories" (Inventories, valuation, net realizable value).
  - `FSBU 6/2020` "Fixed Assets" (Fixed assets, depreciation, revaluation, component depreciation).
  - `FSBU 26/2020` "Capital Investments" (Capital investments, acquisition, commissioning, R&D).
  - `FSBU 14/2022` "Intangible Assets" (Intangible assets, goodwill, software, licenses).
  - `FSBU 25/2018` "Lease Accounting" (Lease accounting, Right-of-Use assets, lease liability).
  - `FSBU 27/2021` "Documents and Document Flow" (Electronic document flow, storage, corrections).
  - `FSBU 28/2023` "Inventory Auditing" (Mandatory physical inventory audit rules).

---

## 2. Tax Regimes & Strategic Decision Matrix

Entities and Individual Entrepreneurs (Individual Entrepreneurs - IP) choose among five statutory tax regimes:

| Tax Regime | Who Can Apply | Revenue Cap | Staff Limit | Key Tax Rates | Tax Invoicing (VAT) |
|---|---|---|---|---|---|
| **OSNO** (General Regime) | Any legal entity / IP without restrictions | Unlimited | Unlimited | Profit: **20%** (25% from 2025); VAT: **20%** / **10%** / **0%**; PIT for IP: **13%–22%** | Full VAT invoices (VAT invoices, electronic document flow EDO, sales/purchases ledgers) |
| **USN Income** (Simplified 6%) | LLC, IP meeting criteria | Up to 450M RUB (indexed) | Up to 130 employees | **6%** on gross revenue (regional rate may be 1%–6%) | VAT-exempt below 60M RUB; over 60M RUB: **5%** VAT (no deduction) or **20%** (with deduction) |
| **USN Income minus Expenses** (15%) | LLC, IP with substantial documented costs (>65-70%) | Up to 450M RUB (indexed) | Up to 130 employees | **15%** on net taxable profit (regional rate 5%–15%); Minimum tax **1%** of gross revenue | Same VAT rules as USN 6% (mandatory VAT registration when exceeding 60M RUB threshold) |
| **AUSN** (Automated Simplified) | Micro-businesses in pilot regions (Moscow, MO, Kaluga, Tatarstan) | Up to 60M RUB | Up to 5 employees; No bank loans | **8%** ("Income") or **20%** ("Income minus Expense"). Zero insurance premiums (except fixed injury fee) | No VAT; fully calculated by FNS via authorized banks |
| **PSN** (Patent System) | Sole proprietors (IP) only; strictly listed activities (retail, craft, transport) | Up to 60M RUB across all patents | Up to 15 employees | **6%** on potential annual income (potential annual imputed income set by regional law) | No VAT; No annual tax return |
| **NPD** (Self-employed) | Physical persons and IP without employees or employer relations | Up to 2.4M RUB / year | 0 employees | **4%** (B2C sales) / **6%** (B2B sales to legal entities/IP) | Invoices via My Tax state mobile application; No insurance premiums required |

---

## 3. The Single Tax Account (Single Tax Account - ENS) & Payment System (ENP)

All federal, regional, and municipal taxes, penalties, and contributions are paid into a single unified account at the Federal Treasury (Article 11.3, 45, 58 NK RF).

### A. Operational Mechanics of ENS:
- **Unified Payment (ENP)**: One payment order with a single treasury account (Tula Treasury regardless of company registration location).
- **Mandatory Notification of Calculated Taxes (Notification of Calculated Tax Sums, KND 1110355)**:
  - Required for advance payments when tax returns are not yet filed (e.g., monthly personal income tax, insurance premiums, quarterly USN advances, transport and property taxes).
  - **Filing Deadline**: Strictly on or before the **25th day** of the month of payment.
  - **Payment Deadline**: Strictly on or before the **28th day** of the respective month.
- **Statutory Distribution Order (Statutory ENS Debit Priority - Art. 45 para. 8 NK RF)**:
  1. Arrears of Personal Income Tax (Personal Income Tax Arrears - chronological priority).
  2. Current Personal Income Tax obligations (Current Personal Income Tax obligations).
  3. Arrears of other taxes, fees, and insurance contributions (Tax and contribution arrears).
  4. Current taxes, advance payments, and insurance contributions (Current taxes and contributions).
  5. Interest (Late payment interest - Peni).
  6. Fines and penalties (Fines and statutory penalties).

---

## 4. Labor Taxation, Payroll & Mandatory Insurance Contributions

### A. Progressive Personal Income Tax (Progressive PIT Scale - Art. 224 NK RF):
From 2025, personal income tax operates under a five-bracket progressive scale:
- Up to **2.4 million RUB** per year: **13%**.
- Over **2.4 million** to **5.0 million RUB**: **15%**.
- Over **5.0 million** to **20.0 million RUB**: **18%**.
- Over **20.0 million** to **50.0 million RUB**: **20%**.
- Over **50.0 million RUB** per year: **22%**.
*Withholding and filing*: Tax agents withhold PIT on every payout date (advances and final payroll). Deadlines: payouts from 1st to 22nd day paid by 28th of current month; payouts from 23rd to last day paid by 5th of next month.

### B. Mandatory Social Insurance Contributions (Mandatory Insurance Contributions - Chapter 34 NK RF):
Contributions cover Pension (OPS), Medical (OMS), and Social Disability/Maternity (OSS):
- **Base Standard Unified Tariff**: **30%** up to the statutory marginal limit (Statutory Base Cap); **15.1%** on excess amounts.
- **SME Reduced Tariff (Reduced SME Tariff)**:
  - Standard **30%** calculated on monthly salary within the Federal Minimum Wage (MROT minimum wage).
  - Reduced **15%** on the entire portion of salary exceeding federal minimum wage (MROT).
- **Accredited IT Companies Tariff**: **7.6%** unified rate (within marginal base) and 0% on excess amounts (Art. 427 NK RF).
- **Industrial Injury Insurance (Occupational injury insurance contributions to SFR, Federal Law No. 125-FZ)**: Separate non-ENS contribution paid to Social Fund of Russia (SFR) based on professional risk class (0.2% to 8.5%).

---

## 5. Mandatory Tax & Accounting Reporting Calendar

1. **Quarterly / Annual Filings**:
   - **Form 6-NDFL (Form 6-NDFL)**: Quarterly by 25th of the month following the quarter (April 25, July 25, October 25, February 25 for annual).
   - **RSV (RSV insurance calculation)**: Quarterly by 25th of the month following the quarter.
   - **Form EFS-1 (Unified Reporting Form EFS-1)**:
     - *Subsection 1.1 (Labor movement / employment / dismissal / GPH contracts)*: Next working day after contract conclusion/termination or order issuance.
     - *Subsection 1.2 (Insurance record / record)*: Annually by January 25.
     - *Section 2 (Injury contributions / injury)*: Quarterly by 25th of following month.
   - **VAT Declaration (VAT Declaration)**: Quarterly by 25th in electronic format via accredited EDO operator.
   - **Profit Tax Declaration (Profit Tax Declaration)**: Quarterly/monthly by 25th; annual by March 25.
   - **USN Declaration (USN Declaration)**: Annual by March 25 for LLCs, April 25 for Sole Proprietors.
   - **Annual Financial Statements (Annual Balance Sheet and Financial Results Report)**: Annual by March 31 uploaded to state database GIPBO (GIR BO state registry).

---

## 6. Tax Control, Desk & Field Audits, Fines & Article 54.1 Defense

### A. Tax Audits Architecture:
- **Desk Audit (Desk Tax Audit - Art. 88 NK RF)**: Automated 3-month review (2 months for VAT) of submitted returns. Tax authorities cross-check VAT via automated risk-tracking systems (ASK NDS-2 / ASK NDS-3 automated VAT risk cross-checking).
- **Field Audit (On-Site Field Tax Audit - Art. 89 NK RF)**: Comprehensive audit covering up to 3 preceding calendar years. Triggers: high tax gap, low tax burden compared to industry average, repeated operations with high-risk counterparties (shell companies / conduit entities), unexplainable losses.

### B. Statutory Tax Penalties & Sanctions (Chapter 16 NK RF):
- **Failure to File Tax Return on Time (Art. 119 NK RF)**: 5% of unpaid tax per month of delay (min. 1,000 RUB, max. 30% of tax amount).
- **Gross Violation of Accounting Rules (Art. 120 NK RF)**: 10,000 to 30,000 RUB; if resulting in tax underpayment: 20% of unpaid tax (min. 40,000 RUB).
- **Underpayment or Non-payment of Tax (Art. 122 NK RF)**:
  - Unintentional underpayment (miscalculation, error): **20%** of unpaid tax amount.
  - Intentional evasion (tax fraud, artificial schemes, shell companies): **40%** of unpaid tax amount.
- **Failure of Tax Agent to Withhold/Transfer PIT (Art. 123 NK RF)**: **20%** of amount due.
- **Failure to Provide Documents / Clarifications upon FNS Request (Art. 126, 129.1 NK RF)**: 200 RUB per missing document under Art. 93; 5,000 to 20,000 RUB under Art. 93.1 (counterparty cross-audits).

### C. Article 54.1 NK RF Defense (Unjustified Tax Benefit & Business Splitting):
- **Prohibition of Tax Base Distortions**: Art. 54.1 NK RF prohibits reduction of tax base resulting from distortion of business facts or fictitious transactions.
- **Two Cumulative Tests for Expense/VAT Deductions**:
  1. The primary purpose of the transaction was not tax avoidance (Business Purpose Test).
  2. The contractual obligation was executed by the party named in the contract or authorized assignee (Reality of transaction and verified counterparty).
- **Business Splitting Defense (Business splitting defense)**:
  - Independent economic viability, separate management, separate staff, distinct material assets, absence of intercompany loans without commercial interest, absence of shared IP addresses and bank access keys.

---

<a name="ru-civil-corporate-law"></a>
# 📦 SKILL: ru-civil-corporate-law
*Domain:* **Russian Business Law**

---
name: ru-civil-corporate-law
description: >-
  Russian civil and commercial law (GK RF Parts 1–4), corporate law (14-FZ LLC, 208-FZ JSC, corporate agreements Art. 67.2, major and interested transactions), commercial contract drafting and enforcement, intellectual property protection (Rospatent, Russian Software Registry, licenses), and real estate legal due diligence (218-FZ).
---
# Russian Civil, Commercial & Corporate Law 

A comprehensive legal and tactical guide for corporate counsels, in-house legal teams, managing directors, and investors operating in the jurisdiction of the Russian Federation.

---

## 1. Statutory Architecture & Hierarchy of Civil Legislation

The civil law system of the Russian Federation is strictly codification-based:
- **Civil Code of the Russian Federation (Civil Code of the Russian Federation - GK RF)**:
  - *Part 1*: Basic provisions, persons, objects of civil rights, deals, representation, statute of limitations, ownership, general law of obligations and contracts (Articles 1–453).
  - *Part 2*: Specific types of contractual obligations (sale, lease, contractor work, transportation, loan, bank account, agency, storage, insurance, tort liability) (Articles 454–1109).
  - *Part 3*: Inheritance law and Private International Law / Conflict of Laws (Conflict of Laws) (Articles 1110–1224).
  - *Part 4*: Intellectual property, copyright, patent law, trademarks, commercial designations, trade secrets (Articles 1225–1551).
- **Federal Law No. 14-FZ "On Limited Liability Companies" (Federal Law On Limited Liability Companies)**.
- **Federal Law No. 208-FZ "On Joint Stock Companies" (Federal Law On Joint Stock Companies)**.
- **Federal Law No. 98-FZ "On Commercial Secrets" (Federal Law On Commercial Secrets)**.
- **Federal Law No. 218-FZ "On State Registration of Real Estate" (Federal Law On State Registration of Real Estate)**.

---

## 2. Commercial Contract Drafting & Risk Engineering

### A. Essential Contract Types & Statutory Regimes:
1. **Supply Agreement (Supply Agreement - Articles 506–524 GK RF)**:
   - Primary B2B sale of goods framework.
   - Crucial terms: Clear specification of goods (nomenclature, quantity, GOST/TU technical standards), delivery conditions (delivery schedules, transport allocation, acceptance protocols, notification of defects under Art. 513 GK RF).
   - Retention of title clause (Retention of title - Art. 491 GK RF).
2. **Contract for Work & Construction (Contract for Work & Construction - Articles 702–768 GK RF)**:
   - Crucial terms: Precise scope of work, technical assignments (technical specifications), initial and completion deadlines (mandatory essential terms under Art. 708 GK RF; absence voids contract), acceptance certificates (KS-2, KS-3 for construction), hidden defect warranties (Art. 724 GK RF).
3. **Lease Agreement (Commercial Lease Agreement - Articles 606–625, 650–655 GK RF)**:
   - Real estate leases for 1 year or longer **require mandatory state registration in the Unified State Register of Real Estate (EGRN)** to possess legal validity against third parties (Art. 651 GK RF).
   - Short-term leases (up to 364 days) take effect upon execution without state registration.
   - Essential provisions: Handover act (Handover and Acceptance Act), utility expenses allocation, unilateral termination terms, permanent improvements ownership (inseparable improvements).
4. **Service Agreement (Paid Service Agreement - Articles 779–783 GK RF)**:
   - Governs consulting, marketing, IT administration, legal services.
   - **Key Statutory Vulnerability (Art. 782 GK RF)**: Either party has a mandatory non-waivable statutory right to unilaterally terminate the contract at any time: the customer by paying actual incurred expenses, the contractor by compensating full damages.

### B. Breach of Contract, Liability & Damage Recovery:
- **Contractual Penalty (Contractual Penalty - Articles 330–333 GK RF)**:
  - Fines (Fixed fine) and late interest penalties (Late payment penalty). Must be stipulated in **written form** (Art. 331).
  - **Judicial Penalty Reduction (Art. 333 GK RF)**: In B2B contracts, reduction of penalty by court is permitted **only upon explicit motion of the debtor** and only if disproportion is objectively proven compared to creditor losses (Resolution of Plenum of the Supreme Court of the Russian Federation No. 7).
- **Damages (Damages - Articles 15, 393 GK RF)**:
  - Composed of actual damage (Actual damages) and lost profits (Lost profits). Requires proof of: (1) fact of breach, (2) existence and exact quantum of loss, (3) direct causal link, (4) fault of the breaching party (fault presumed in B2B under Art. 401 GK RF).
- **Statutory Interest for Use of Money (Statutory Interest for Use of Money - Art. 395 GK RF)**:
  - Calculated based on the key rate (Central Bank of Russia Key Rate) prevailing in the relevant period, unless contract establishes higher late payment rates.
- **Statute of Limitations (Statute of Limitations - Articles 195–208 GK RF)**:
  - General limitation period is **3 years** from when the party knew or should have known of the infringement. Maximum objective limit is **10 years**. Parties cannot shorten or extend limitation periods by agreement (Art. 198 GK RF).

---

## 3. Russian Corporate Law: LLC (Limited Liability Company) & Corporate Governance

### A. Formation and Capital Architecture:
- Minimum charter capital (charter capital): **10,000 RUB**, payable in cash within 4 months from registration.
- **Charter (Articles of Association / Charter)**: Supreme corporate foundation document. Can be customized or selected from 36 standard model charters (Standard Model Charters).
- **Mandatory Notarization**:
  - Decision to increase charter capital must be certified by a notary.
  - Transactions selling shares (LLC membership shares) to third parties require **mandatory notarial certification** (Art. 21 14-FZ), except internal pre-emption rights exercising.
  - Notarial certification of General Meeting decisions and participant attendance is mandatory unless the charter explicitly provides an alternative mechanism (signed protocol by all participants).

### B. Management Bodies & Executive Liability:
- **Sole Executive Body (General Director / CEO)**: Represents the company without power of attorney, concludes contracts, manages bank accounts.
- **Fiduciary Duties (Art. 53.1 GK RF)**: Must act reasonably and in good faith in the interests of the legal entity.
- **Personal Tort Liability of Director**:
  - The company or its participants holding at least 1% of shares may file a derivative lawsuit against the director for compensation of losses caused by bad faith or unreasonable conduct (Plenum of the Supreme Arbitration Court No. 62).
- **Major Transactions (Major Transactions - Art. 46 14-FZ)**:
  - Deals exceeding **25%** of the book value of the company's balance sheet assets require prior approval of the General Meeting or Board of Directors.
- **Transactions with Interested Parties (Interested Party Transactions - Art. 45 14-FZ)**:
  - Transactions where the director, controlling participant, or their close relatives hold an economic interest. Require notification and potential approval.

### C. Shareholder Disputes & Expulsion of a Participant (Expulsion of a Participant):
- Under **Article 10 of Law No. 14-FZ**, participants holding in aggregate at least **10%** of charter capital may judicially demand the expulsion of a participant who grossly violates duties or substantially obstructs the activity of the company (e.g. systematic voting boycott blocking mandatory management appointments).

### D. Corporate Agreements (Corporate Shareholders Agreement - Art. 67.2 GK RF):
- Enables shareholders to agree upon:
  - Voting coordination and deadlock resolution mechanisms (Russian roulette, Texas shootout).
  - Restrictions on share alienation (Tag-along, Drag-along rights).
  - Option contracts for share buyouts (Option Agreement Art. 429.2 GK RF).

---

## 4. Intellectual Property, IT Protection & Software Licensing (Part 4 GK RF)

### A. Protection of Software & Databases:
- Software programs (Computer software programs) are protected as literary works under copyright law (Art. 1261 GK RF). Registration with Rospatent (Rospatent) is optional but creates a public evidentiary presumption of copyright ownership.
- **Register of Russian Software (Unified Register of Russian Software)**:
  - Qualification requirements: Exclusive IP rights held by Russian citizens or Russian organizations (>50% Russian ownership), total royalty payments abroad < 30%, software runs on domestic OS (Astra Linux, RED OS, Alt Linux).
  - Benefits: Zero VAT exemption on software sales and SaaS subscriptions (subclause 26 clause 2 Art. 149 NK RF) and preferential access to public procurement (Federal Law 44-FZ/223-FZ).

### B. Intellectual Property Contracts:
- **Alienation of Exclusive Rights (Assignment of Exclusive Rights - Art. 1234 GK RF)**: Complete transfer of economic copyright; must be in writing; non-payment gives right to judicial termination and recovery of damages.
- **License Agreement (License Agreement - Art. 1235 GK RF)**: Exclusive (Exclusive) vs Non-exclusive (Simple / non-exclusive). Must define territory, permitted ways of use, term, and remuneration.
- **Works Made for Hire (Works Made for Hire - Art. 1295 GK RF)**:
  - To secure IP created by employees, the employer must have: (1) labor contract with IP clause, (2) formal job description (job description), (3) written technical task (written technical assignment), (4) formal acceptance act (acceptance act of work made for hire), (5) separate documented author's remuneration (author remuneration), which cannot be embedded in base salary.

### C. Trademarks (Trademarks - Art. 1477–1515 GK RF):
- Acquired solely through state registration with Rospatent under Nice Classification (MKTU). Protection lasts 10 years (renewable).
- Statutory damages for infringement (Art. 1515 GK RF): Compensation up to **5,000,000 RUB** or double the cost of counterfeit goods or double the license value, without proving actual damages.

---

## 5. Real Estate Legal Due Diligence (Federal Law No. 218-FZ)

Before acquiring real estate or commercial facilities:
1. **Title Verification**: Extract from EGRN (Extract from Unified State Real Estate Register EGRN) confirming registered owner, cadastral boundaries, encumbrances (encumbrances), pledges, ongoing judicial arrests.
2. **Chain of Title Review**: Tracing transitions of ownership for the last 3–5 years to eliminate bankruptcy avoidance risks (Art. 61.2 of Bankruptcy Law) or fraudulent signatures.
3. **Land & Permitted Use (Permitted Land Use Category VRI)**: Ensuring the building conforms to statutory zoning and land category (Land Category).

---

<a name="ru-litigation-advocacy"></a>
# 📦 SKILL: ru-litigation-advocacy
*Domain:* **Russian Litigation**

---
name: ru-litigation-advocacy
description: >-
  Russian litigation and judicial practice: commercial arbitration courts (APK RF, mandatory 30-day pre-trial claims, interim measures), civil courts (GPK RF, consumer protection), administrative justice (KAS RF), criminal defense in white-collar economic crimes (UPK RF, Art. 159, 199 UK RF, Art. 108 Part 1.1 detention ban), Federal Bar Act (63-FZ, attorney privilege, warrants, inquiries), and debt enforcement (229-FZ, FSSP, bank account attachments).
---
# Russian Litigation, Advocacy & Enforcement Practice 

An exhaustive, high-level tactical and procedural reference for trial attorneys (advocates), litigation partners, corporate counsel, and forensic specialists litigating before the commercial and general jurisdiction courts of the Russian Federation.

---

## 1. Russian Judicial Hierarchy & Court Architecture

The judicial system of the Russian Federation operates under two primary court branches unified under the **Supreme Court of the Russian Federation (Supreme Court of the Russian Federation)**:

```
                       [ Supreme Court of the Russian Federation ]
                                    |
      +-----------------------------+-----------------------------+
      |                                                           |
[ Commercial Courts (Arbitrazh - Business) ]       [ Courts of General Jurisdiction (Civil/Criminal) ]
  - Cassation (10 District Courts + IP Court SIP)  - Cassation Courts of General Jurisdiction (District Cassation Courts)
  - Appeals (21 Commercial Appellate Courts)      - Appellate Courts of General Jurisdiction (Appellate Courts)
  - First Instance (Regional Commercial Courts)    - Regional / Provincial / Supreme Republic / City Courts
                                                  - District / City Courts
                                                  - Magistrate Judges
```

---

## 2. Commercial Arbitration Proceedings (Commercial Procedure Code - APK RF)

Arbitration courts resolve disputes arising from entrepreneurial and economic activities between legal entities, individual entrepreneurs, and public authorities.

### A. Pre-trial Claim Procedure (Mandatory Pre-Trial Claim Procedure - Art. 4 Part 5 APK RF):
- **Statutory Rule**: Civil law disputes concerning monetary claims arising from contracts and unjust enrichment can be submitted to arbitration **only after 30 calendar days** from the date of sending a formal written pre-trial claim (pre-trial claim) to the counterparty, unless other terms or procedures are established by federal statute or contract.
- **Evidence of Dispatch**: Registered mail with declared value and postal inventory list (registered letter with inventory list) and postal tracking receipt. Premature filing or lack of proper evidence of dispatch results in the statement of claim being left without consideration (claim left without consideration - Art. 148 APK RF).

### B. Interim Protective Measures (Interim Protective Measures - Articles 90–100 APK RF):
- **Statutory Criteria**: Imposed if failure to grant measures could make execution of the judicial act impossible or difficult, or to prevent substantial damage to the applicant.
- **Types**: Attachment of bank accounts (attachment of bank accounts within claim amount), prohibition from performing certain actions (e.g., prohibition to state registers against registering real estate transfer or corporate share alienation), transfer of disputed asset to storage.
- **Counter-securing (Counter-Securing Deposit - Art. 94 APK RF)**: Depositing monetary funds onto the court's deposit account in the amount of the requested claim dramatically increases the probability of granting interim measures.

### C. Burden of Proof & Evidence Rules (Articles 64–75, 82 APK RF):
- **Burden of Proof (Art. 65 APK RF)**: Each party must prove the circumstances upon which it bases its claims or objections.
- **Electronic Evidence**: Printouts of emails, WhatsApp/Telegram messenger correspondence, electronic document management systems (EDO) are admissible when verified by notarial protocol or when the underlying contract establishes electronic communications as legally binding.
- **Forensic Expertise (Court-Appointed Forensic Expertise - Art. 82 APK RF)**:
  - Appointed upon party motion or court initiative (construction, financial-economic, forensic handwriting examination, computer-technical).
  - Crucial tactics: Drafting precise questions, selecting licensed expert organizations with immaculate reputation, depositing expert fees onto court deposit account prior to motion.

### D. Appellate, Cassation & Supreme Court Appeals:
1. **First Instance**: Examination of facts, witnesses, documents, expert testimonies.
2. **Court of Appeals (Court of Appeals - Articles 257–272 APK RF)**:
   - Deadline: **1 month** from the date of manufacturing the full text of the decision.
   - De novo review of facts and law; new evidence admitted only upon proving impossibility of earlier submission for valid reasons.
3. **First Cassation (District Cassation Court - Articles 273–291 APK RF)**:
   - Deadline: **2 months** from entry of appellate judgment into legal force.
   - Examines only legality and application of substantive/procedural law; cannot re-evaluate factual evidence.
4. **Second Cassation (Supreme Court Economic Panel - Articles 291.1–291.15 APK RF)**:
   - Deadline: **2 months**; initial filtration by single judge of Supreme Court; hearing granted only upon substantial systemic legal errors.

---

## 3. Civil Courts of General Jurisdiction (Civil Procedure Code GPK RF) & Administrative Justice (KAS RF)

### A. Civil Procedure Code (GPK RF):
- Resolves disputes with physical persons (consumers, labor, family, inheritance, property damage).
- **Consumer Protection Law (Law on Protection of Consumer Rights No. 2300-1)**:
  - Unprecedented leverage for consumer-plaintiffs: exemption from state duty, choice of alternative jurisdiction (residence of consumer), statutory forfeit of **1% per day** for delayed goods replacement or **3% per day** for delayed services.
  - **Mandatory 50% Judicial Fine**: Under Art. 13 Part 6, the court awards a mandatory fine of 50% of the entire awarded amount in favor of the consumer for failure of the business to satisfy demands voluntarily in pre-trial order.

### B. Code of Administrative Judicial Procedure (KAS RF):
- Used to contest illegal decisions, actions, or omissions of government bodies:
  - Challenging unlawful tax decisions and asset blocks by the Federal Tax Service (FNS).
  - Challenging actions and unlawful inaction of bailiffs (FSSP).
  - Challenging denials of cadastral registration and registration of rights by Rosreestr.
  - Strict limitation periods: Generally **3 months** from the day the applicant learned of the violation of rights.

---

## 4. White-Collar Criminal Defense & Economic Crimes (Criminal Code UK RF & Criminal Procedure Code UPK RF)

Defense of business executives, owners, and chief accountants against corporate criminal prosecution:

### A. Key Economic Crime Articles of the Criminal Code (UK RF):
- **Article 159 (Fraud)**:
  - Parts 5–7 specifically penalize intentional non-fulfillment of contractual obligations in entrepreneurial activities resulting in significant or large-scale damage.
  - Defense strategy: Proving civil law nature of dispute (civil-law dispute nature), lack of prior fraudulent intent, economic impossibility of fulfillment due to market collapse or force majeure.
- **Article 160 (Embezzlement / Misappropriation)**: Accusations against directors for bonus payouts, corporate property transfers, or affiliate transactions.
- **Articles 198, 199, 199.1, 199.2 (Tax Evasion)**:
  - Full payment of tax arrears, penalties, and fines prior to court hearing grants mandatory statutory exemption from criminal liability for first-time offenders (Art. 76.1 UK RF).

### B. Entrepreneurial Detention Ban (Prohibition of Pre-Trial Detention for Entrepreneurs - Art. 108 Part 1.1 UPK RF):
- Direct statutory prohibition on remanding into custody (pre-trial detention) suspects accused of economic crimes (Articles 159 parts 5–7, 160, 199 UK RF) committed by individual entrepreneurs or members of commercial management bodies in connection with their entrepreneurial activity.
- Defense tactics: Submitting corporate charters, orders of appointment, commercial contracts, and tax filings to establish the undisputed entrepreneurial status of the transaction.

### C. Tactical Guidelines during Search, Seizure & Interrogation:
- **Searches and Seizures (Searches and Seizures - Articles 182, 183 UPK RF)**:
  - Right to presence of defense attorney.
  - Verification of judicial warrant (or investigator's decree in urgent cases).
  - Prohibition of unnecessary damage to property; mandatory inclusion of all seized documents, servers, flash drives, and tokens into the search protocol with specific serialized markings.
- **Interrogation (Interrogation - Articles 187–190 UPK RF)**:
  - Absolute constitutional right to remain silent under **Article 51 of the Constitution of the Russian Federation**.
  - Right to private consultation with attorney prior to first interrogation.

---

## 5. The Bar & Legal Status of Advocates (Federal Law No. 63-FZ)

The legal status of a licensed attorney (Licensed Advocate) provides statutory legal protections under **Federal Law No. 63-FZ "On Advocacy and the Bar in the Russian Federation"**:

1. **Advocate's Privilege / Attorney-Client Privilege (Attorney-Client Privilege - Art. 8 63-FZ)**:
   - Encompasses any information connected with the rendering of legal assistance to a client.
   - An advocate cannot be summoned, subpoenaed, or interrogated as a witness regarding circumstances that became known to him in connection with rendering legal aid.
   - Conducting searches, inspections, or seizures in an advocate's office or home requires a **special judicial warrant** and can be carried out only in the presence of an authorized representative of the regional Bar Chamber (Art. 450.1 UPK RF).
2. **Advocate's Inquiry (Advocate Official Inquiry - Art. 6.1 63-FZ)**:
   - Mandatory statutory inquiry sent to state authorities, municipal bodies, and public organizations to collect documents and certificates.
   - Failure to respond within 30 days entails administrative liability under **Article 5.39 of the Administrative Offenses Code (Administrative Code KoAP RF)**.
3. **Representation Instruments**:
   - Criminal defense: Attorney warrant (Advocate Warrant - Order) issued by the legal entity of the bar (Bureau, College, Consultation).
   - Civil and arbitration proceedings: Power of attorney (Power of Attorney) with explicit procedural powers (signing of statement of claim, changing claim subject, conclusion of amicable settlement).

---

## 6. Debt Enforcement & Bailiff Operations (Federal Law No. 229-FZ)

Obtaining a court judgment is only the first stage; recovery of funds is governed by **Federal Law No. 229-FZ "On Enforcement Proceedings"**:

### A. Direct Execution via Commercial Banks (Art. 8 229-FZ):
- **Fast-Track Recovery**: If the creditor knows the debtor's bank accounts, the original Executive Writ (Writ of Execution / Enforcement Order) along with an application can be delivered directly to the debtor's commercial bank.
- The bank is statutorily mandated to freeze funds and execute write-off within **3 banking days**, entirely bypassing bailiff delays.
- Creditors have the legal right under Art. 69 part 8 of Law 229-FZ to submit the court writ to any branch of the Federal Tax Service (FNS) to obtain a list of all active bank accounts opened in the debtor's name across all credit institutions.

### B. Bailiff Operations (Federal Bailiff Service FSSP):
- If accounts are empty or assets unknown, enforcement is initiated via the Federal Bailiff Service:
  - Imposition of ban on registration actions for vehicles and real estate (ban on registration actions in vehicle and land registries).
  - Seizure and sale of corporate property and warehouse inventories at public auction.
  - Imposition of temporary restriction on international travel (temporary international travel ban) on individual debtors and managing directors.
  - Foreclosure on accounts receivable (foreclosure on accounts receivable - Art. 76 229-FZ).
  - Challenging unlawful inaction of the bailiff via administrative complaints to higher bailiffs or through the court under Chapter 22 KAS RF.

---

<a name="secure-software-engineering"></a>
# 📦 SKILL: secure-software-engineering
*Domain:* **DevOps & Bulletproof Software Engineering**

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

---

<a name="server-hardening-zerotrust"></a>
# 📦 SKILL: server-hardening-zerotrust
*Domain:* **Server Hardening**

---
name: server-hardening-zerotrust
description: >-
  Enterprise infrastructure hardening for Linux & Windows, SSH ed25519/2FA, UFW/Nftables firewalls, Fail2ban, CrowdSec, Web Application Firewalls (WAF), Zero Trust architecture (mTLS, bastion hosts), and PCI DSS v4.0 compliance standards.
---
# Server Hardening, Security Baselines & Zero Trust Architecture

A comprehensive operational security framework for hardening servers, endpoints, cloud nodes, and network perimeters against advanced persistent threats (APTs) and automated exploitation.

---

## 1. Linux Server Hardening Baseline (CIS Benchmarks)

### A. SSH Daemon Hardening (`/etc/ssh/sshd_config`):
```ini
# Port and Protocol
Port 22222                          # Move from default port 22
Protocol 2
AddressFamily inet                  # IPv4 only if IPv6 is unused

# Authentication
PermitRootLogin no                  # Never allow direct root login
PasswordAuthentication no           # Pure key-based authentication
PubkeyAuthentication yes
AuthenticationMethods publickey     # Enforce publickey (or publickey,keyboard-interactive for 2FA)
MaxAuthTries 3                      # Disconnect quickly on failed attempts
LoginGraceTime 20                   # Short window to authenticate
PermitEmptyPasswords no
HostbasedAuthentication no
IgnoreRhosts yes

# Cryptographic Primitives (Modern Only)
KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group16-sha512
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com
MACs hmac-sha2-512-etm@openssh.com

# Session Restrictions
X11Forwarding no
AllowTcpForwarding no               # Disable unless explicitly required for tunneling
ClientAliveInterval 300
ClientAliveCountMax 2
```

### B. Firewall & Intrusion Prevention:
- **Nftables / UFW**:
  - Default policy: **DROP** all incoming, **DROP** all forwarded, **ACCEPT** all outgoing.
  - Rate limiting new incoming connections to prevent brute force and port scans.
- **Fail2ban vs. CrowdSec**:
  - **CrowdSec**: Modern collaborative IPS parsing journald/logs, utilizing a global consensus threat intelligence network, and blocking attackers at the firewall/bouncing level.
  - **Fail2ban**: Local jail rules targeting SSH, Nginx auth, and WordPress brute force.

### C. Kernel Self-Protection & Auditing:
- Enforce AppArmor / SELinux in `enforcing` mode.
- System call auditing via `auditd`: Track modifications to `/etc/passwd`, `/etc/shadow`, `/etc/sudoers`, and execution of SUID binaries.
- Restrict kernel pointers and dmesg: `kernel.dmesg_restrict = 1`, `kernel.kptr_restrict = 2`.

---

## 2. Web Application & Reverse Proxy Hardening

### Secure HTTP Response Headers (Nginx / Cloudflare):
```nginx
# Prevent MIME-sniffing
add_header X-Content-Type-Options "nosniff" always;

# Prevent clickjacking
add_header X-Frame-Options "SAMEORIGIN" always;

# Restrict browser capabilities
add_header Permissions-Policy "geolocation=(), camera=(), microphone=(), payment=()" always;

# Strict Content Security Policy (CSP)
add_header Content-Security-Policy "default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self';" always;

# Strict-Transport-Security (HSTS - 2 years + preload)
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

# Referrer Policy
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
```

### Web Application Firewall (WAF) & Rate Limiting:
- Deploy **Cloudflare WAF** or **ModSecurity with OWASP Core Rule Set (CRS)** to block SQL injection (SQLi), Cross-Site Scripting (XSS), Local File Inclusion (LFI), and Remote Code Execution (RCE).
- Nginx connection & request limiting:
  ```nginx
  limit_req_zone $binary_remote_addr zone=req_limit_per_ip:10m rate=10r/s;
  limit_conn_zone $binary_remote_addr zone=conn_limit_per_ip:10m;

  location /api/ {
      limit_req zone=req_limit_per_ip burst=20 nodelay;
      limit_conn conn_limit_per_ip 10;
  }
  ```

---

## 3. Windows Server & Workstation Hardening

### Attack Surface Reduction (ASR) & Credential Protection:
- **Enable Windows Defender Credential Guard**: Isolates LSA secrets (LSASS) in a virtualization-based security (VBS) container, neutralizing Mimikatz Pass-the-Hash attacks.
- **Disable Legacy Protocols via Group Policy or Registry**:
  - Disable **SMBv1** entirely.
  - Disable **LLMNR** (*Link-Local Multicast Name Resolution*) and **NetBIOS over TCP/IP** to prevent Responder/poisoning attacks.
  - Enforce SMB Signing and SMB Encryption.
- **PowerShell Hardening**:
  - Enforce **Constrained Language Mode** for standard users via AppLocker / WDAC.
  - Enable Script Block Logging (Event ID 4104) and Module Logging.
- **BitLocker with TPM + PIN**: Full disk encryption protecting data at rest on laptops and desktops against physical theft or offline recovery attacks.

---

## 4. Zero Trust Architecture (ZTA)

### Core Tenets of Zero Trust (NIST SP 800-207):
1. **Never Trust, Always Verify**: Location within the local network perimeter grants zero trust.
2. **Least Privilege Access**: Access is granted strictly on a per-session, need-to-know basis.
3. **Assume Breach**: Segment networks and operate under the premise that an adversary is already inside.

### Implementation Checklist:
- **Bastion / Jump Hosts**: Production servers must never expose SSH/RDP directly to the public internet. Access exclusively via an authenticated Bastion host or an encrypted WireGuard/Tailscale mesh with multi-factor authentication (MFA).
- **Mutual TLS (mTLS)**: Inter-service communication across microservices or internal APIs requires cryptographic client and server certificates.
- **Ephemeral Secrets & Vault**: Store zero secrets in code, Dockerfiles, or unencrypted text. Inject via HashiCorp Vault, AWS Secrets Manager, or encrypted SOPS repositories.

---

## 5. PCI DSS v4.0 Compliance Standards

For systems processing, transmitting, or storing cardholder or sensitive financial data:
- **Requirement 1 & 2**: Strict firewall network segmentation isolating the Cardholder Data Environment (CDE) from out-of-scope systems.
- **Requirement 3 & 4**: Strong cryptography (AES-256) for data at rest and TLS 1.3 for data in transit; complete prohibition of storing card verification codes (CVV/CVC) after authorization.
- **Requirement 10**: Log all user access to system components; synchronize clocks via secure NTP; retain audit trail history for at least 12 months (with 3 months immediately available).
- **Requirement 11.5**: Deploy **File Integrity Monitoring (FIM)** (e.g. AIDE, OSSEC, Wazuh) to monitor system binaries and critical configuration files against unauthorized modifications.

---

<a name="sysadmin-network-engineering"></a>
# 📦 SKILL: sysadmin-network-engineering
*Domain:* **SysAdmin & Networking**

---
name: sysadmin-network-engineering
description: >-
  Advanced system administration for Linux & Windows Server, computer networking (routing, DNS, reverse proxies), VPN tunneling & protocol obfuscation (Xray, 3X-UI, Reality, WireGuard), 3-2-1 backup strategies (Borg, Rclone), and storage management.
---
# Senior System Administration & Network Engineering

A master operational manual for systems administration across Linux and Windows Server environments, enterprise network routing, modern obfuscated VPN architectures, and disaster recovery.

---

## 1. Dual-Stack System Administration (Linux & Windows)

### Enterprise Linux (Debian, Ubuntu, AlmaLinux):
- **Service Lifecycle Management**: `systemd` units, override drops (`/etc/systemd/system/<unit>.d/override.conf`), sandboxing directives (`ProtectSystem=strict`, `PrivateTmp=yes`, `NoNewPrivileges=true`).
- **Resource Limits**: PAM limits (`/etc/security/limits.conf`), `cgroups v2` resource budgeting.
- **Package Management**: Automated security patching via `unattended-upgrades` with blacklisting of kernel reboot packages on production nodes.

### Windows Server & Workstation Administration:
- **PowerShell 7+ Automation**: Script blocks, advanced parameters, pipeline chaining, structured error handling with `$ErrorActionPreference = 'Stop'`.
- **Windows Services & Scheduled Tasks**: Automated creation, service account delegation (`gMSA` - Group Managed Service Accounts), non-interactive background scheduling.
- **Sysinternals Diagnostics**:
  - `Process Explorer` (identifying process handles, DLL injection, CPU spikes).
  - `Process Monitor` (ProcMon - real-time file system, registry, and network activity tracing).
  - `Autoruns` (comprehensive audit of startup hooks, WMI persistence, scheduled tasks).

---

## 2. Enterprise Network Architecture & Routing

### Routing & Subnetting:
- **Linux Network Stack**: `iproute2` suite (`ip addr`, `ip route`, `ip rule`), policy-based routing (PBR), multiple routing tables (`/etc/iproute2/rt_tables`), network namespaces (`ip netns`).
- **Windows Network Stack**: `Get-NetIPAddress`, `Get-NetRoute`, `New-NetRoute`, `Test-NetConnection`.
- **MTU & MSS Clamping**: Preventing packet fragmentation in VPN tunnels:
  ```bash
  # Clamping TCP MSS to PMTU in iptables
  iptables -t mangle -A FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
  ```

### DNS Infrastructure & Split-Horizon DNS:
- **DNS Resolution**: Unbound, CoreDNS, systemd-resolved, and `dnsmasq`.
- **Encrypted DNS**: DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) preventing ISP spoofing and inspection.
- **Split-Horizon Architecture**: Internal queries resolve to private IPs (`10.0.0.0/8`, `192.168.0.0/16`), while external public queries resolve to WAN IPs.

---

## 3. Reverse Proxies, Load Balancing & SSL/TLS Automation

### Nginx High-Performance Reverse Proxy:
- HTTP/2 & HTTP/3 (QUIC) support, upstream connection pooling (`keepalive 64`), buffer tuning.
- **Automated SSL/TLS via Certbot / ACME**:
  ```bash
  # Issue wildcard certificate via Cloudflare DNS plugin
  certbot certonly --dns-cloudflare --dns-cloudflare-credentials ~/.secrets/cloudflare.ini \
    -d example.com -d "*.example.com" --agree-tos -m admin@example.com --non-interactive
  ```

### Modern Reverse Proxies (Traefik & Caddy):
- **Caddy**: Automatic zero-config TLS via Let's Encrypt / ZeroSSL with reverse proxying and on-demand certificates.
- **Traefik**: Dynamic configuration discovery via Docker labels.

---

## 4. Advanced VPN, Protocol Obfuscation & Tunneling

Operational management of secure tunnels capable of bypassing deep packet inspection (DPI) and active network probing:

### Modern Obfuscation (Xray-Core, 3X-UI & Reality Protocol):
- **VLESS with Reality**:
  - Eliminates the need for a real domain certificate on the server.
  - **SNI Camouflage (Stealth)**: Borrows the TLS certificate and SNI of a legitimate third-party website (e.g. `gateway.icloud.com`, `dl.google.com`, `microsoft.com`).
  - Active probing resistance: When an unauthorized scanner connects without the client private key, the server transparently proxies the connection to the camouflage target.
- **Management via 3X-UI**:
  - Inbound management (VLESS, VMess, Trojan, Shadowsocks).
  - Multi-user bandwidth accounting and automatic credential expiry.

### WireGuard High-Speed Kernel Mesh:
- Modern Cryptography: Curve25519, ChaCha20, Poly1305, BLAKE2s.
- Instant connection handover for roaming mobile clients.
- Configuration template:
  ```ini
  [Interface]
  PrivateKey = <SERVER_PRIVATE_KEY>
  Address = 10.100.0.1/24
  ListenPort = 51820
  PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
  PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

  [Peer]
  PublicKey = <CLIENT_PUBLIC_KEY>
  AllowedIPs = 10.100.0.2/32
  ```

### SSH Advanced Tunneling:
- **Local Port Forward**: `ssh -L 8080:127.0.0.1:80 user@remote-server` (Access remote service locally).
- **Remote / Reverse Tunnel**: `ssh -R 9000:127.0.0.1:3000 user@remote-server` (Expose local port to public internet).
- **Dynamic SOCKS5 Proxy**: `ssh -D 1080 -q -C -N user@remote-server` (Route all local browser traffic through remote host).

---

## 5. Storage Architecture, Backups & Disaster Recovery

### The 3-2-1-1-0 Backup Architecture:
- **3** copies of critical data.
- **2** different storage media types (Local SSD/NVMe + NAS or Cloud).
- **1** copy stored offsite (geographically separated remote datacenter).
- **1** copy offline / immutable / air-gapped (WORM or cold storage with Object Lock).
- **0** errors on backup recovery verification.

### Enterprise Backup Tooling:
- **BorgBackup**:
  - Deduplicated, authenticated, and encrypted client-side backups.
  - Efficient pruning (`borg prune --keep-daily=7 --keep-weekly=4 --keep-monthly=12`).
- **Rclone**:
  - Syncing encrypted directory trees to 40+ cloud backends (Mega, S3, OCI, Google Drive, SFTP, WebDAV).
- **Automated Recovery Testing**: A backup that hasn't been tested for restoration is legally and operationally deemed nonexistent. Automated weekly restoration tests into an isolated test container.

---

<a name="systematic-debugging"></a>
# 📦 SKILL: systematic-debugging
*Domain:* **Software Engineering**

---
name: systematic-debugging
description: >-
  Use this skill when encountering errors or unexpected behavior in Bash (Linux) or PowerShell/CMD (Windows) scripts. It enforces a strict, methodical troubleshooting process.
---
# Systematic Debugging Protocol

When asked to debug a script or system issue, follow this strict protocol:

1. **Replicate & Understand**: Never guess the error. Ask the user for the exact error output, or use tools to run the script and capture the error.
2. **Check Environment**: 
   - Windows: Verify PowerShell version, Execution Policy, and Administrator privileges.
   - Linux: Verify bash version, user permissions, `$PATH`, and file execution bits (`chmod +x`).
3. **Isolate the Fault**: Do not rewrite the entire script. Add verbose logging (`set -x` in Bash, `Write-Debug` or `Set-PSDebug` in PowerShell) to isolate the exact line failing.
4. **Hypothesize & Test**: Propose one single hypothesis at a time. Do not make multiple unrelated changes.
5. **Verify**: Once a fix is applied, verify it solves the specific error without introducing new ones.

---

<a name="writing-plans"></a>
# 📦 SKILL: writing-plans
*Domain:* **Software Engineering**

---
name: writing-plans
description: >-
  Use this skill when asked to create complex system automation, deployment scripts, or cross-platform tasks. It forces the creation of a step-by-step plan before coding.
---
# Script Planning Protocol

Before writing any complex Bash or PowerShell script, you MUST create a plan and present it to the user.

1. **Requirements Gathering**: Identify the target OS (Linux, Windows 10/11, Windows Server), required permissions, and dependencies.
2. **Step-by-step logic**: Write a numbered list of what the script will do sequentially.
3. **Error Handling Strategy**: Explicitly state how errors will be handled (e.g., `set -e` in bash, `Try/Catch` or `ErrorAction Stop` in PowerShell).
4. **Rollback Strategy**: If the script modifies system state, describe how to revert changes if it fails halfway.
5. **Wait for Approval**: Do not write the full code until the user approves the plan.

---
