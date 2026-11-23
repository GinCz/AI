import re

path = "/AI/GitHub/Secret_Privat/Windows/Ultarix-Monitor/dashboard.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CANONICAL_MAP, defaultProfiles, and storeData at top of script
top_script_target = """        // Track open state for each computer so user's manual expand/collapse is never overwritten
        const pcOpenState = {
            "ULTARIX-07": true,
            "U-09": false,
            "PC-09": false,
            "PC-02": false
        };

        // Saved custom names for employees in localStorage
        const customNames = JSON.parse(localStorage.getItem("ultarix_custom_names") || "{}");

        // Canonical mapping of office computers
        const defaultProfiles = {
            "ULTARIX-07": { name: "Галина", role: "Бухгалтерия 07", icon: "💼" },
            "Ulta_007":   { name: "Галина", role: "Бухгалтерия 07", icon: "💼" },
            "U-09":       { name: "Татьяна / Любовь", role: "Бухгалтерия / Склад (Ёжик)", icon: "📦" },
            "PC-09":      { name: "Татьяна / Любовь", role: "Бухгалтерия / Склад (Ёжик)", icon: "📦" },
            "ULTARIX-09": { name: "Любовь", role: "Бухгалтерия 09", icon: "📦" },
            "PC-02":      { name: "Ульяна", role: "Главный бухгалтер / Директор", icon: "👑" },
            "Ulka-02":    { name: "Ульяна", role: "Главный бухгалтер / Директор", icon: "👑" },
            "ULTARIX-03": { name: "Лилия", role: "Бухгалтерия 03", icon: "📊" },
            "ULTARIX-04": { name: "Оксана", role: "Бухгалтерия 04", icon: "📑" },
            "ULTARIX-05": { name: "Анна", role: "Бухгалтерия 05", icon: "🖨️" },
            "ULTARIX-06": { name: "Бухгалтер 06", role: "Бухгалтерия 06", icon: "📂" },
            "ULTARIX-08": { name: "Светлана", role: "Бухгалтерия 08", icon: "📈" },
            "ULTARIX-010":{ name: "Наталья", role: "Бухгалтерия 10", icon: "🗂️" },
            "ULPS1":      { name: "Сервер", role: "Главный сервер ULPS1", icon: "🖥️" }
        };"""

top_script_replacement = """        // Canonical mapping for all ULTARIX office and remote workstations
        const CANONICAL_MAP = {
            "pc-02": "U-002", "ulka-02": "U-002", "ultarix-02": "U-002", "u-02": "U-002", "u-002": "U-002",
            "pc-03": "U-003", "ultarix-03": "U-003", "u-03": "U-003", "u-003": "U-003",
            "pc-04": "U-004", "ultarix-04": "U-004", "u-04": "U-004", "u-004": "U-004",
            "pc-05": "U-005", "ultarix-05": "U-005", "u-05": "U-005", "u-05": "U-005",
            "pc-06": "U-006", "ultarix-06": "U-006", "u-06": "U-006", "u-06": "U-006",
            "007": "U-007", "pc-07": "U-007", "u-07": "U-007", "ulta_007": "U-007", "ultarix-07": "U-007", "u-007": "U-007",
            "pc-08": "U-008", "ultarix-08": "U-008", "u-08": "U-008", "u-08": "U-008",
            "pc-09": "U-009", "ultarix-09": "U-009", "u-09": "U-009", "u-09": "U-009",
            "pc-010": "U-010", "ultarix-010": "U-010", "u-010": "U-010", "u-10": "U-010", "pc-10": "U-010",
            "u-507": "U-507", "u-510": "U-510", "u-511": "U-511", "u-512": "U-512",
            "ulps1": "ULPS1"
        };
        function normalizeHost(h) {
            if (!h) return "";
            const clean = h.trim().toLowerCase();
            return CANONICAL_MAP[clean] || h.trim().toUpperCase();
        }

        // Track open state for each computer so user's manual expand/collapse is never overwritten
        const pcOpenState = {
            "U-007": true,
            "U-009": true,
            "U-002": false,
            "ULPS1": false
        };

        // Saved custom names for employees in localStorage
        const customNames = JSON.parse(localStorage.getItem("ultarix_custom_names") || "{}");

        // Canonical mapping of office computers (No duplicates, U-XXX format)
        const defaultProfiles = {
            "ULPS1":      { name: "Сервер", role: "Главный сервер ULPS1", icon: "🖥️" },
            "U-002":      { name: "Ульяна", role: "Главный бухгалтер / Директор", icon: "👑" },
            "U-003":      { name: "Лилия", role: "Бухгалтерия 03", icon: "📊" },
            "U-004":      { name: "Оксана", role: "Бухгалтерия 04", icon: "📑" },
            "U-005":      { name: "Анна", role: "Бухгалтерия 05", icon: "🖨️" },
            "U-006":      { name: "Бухгалтер 06", role: "Бухгалтерия 06", icon: "📂" },
            "U-007":      { name: "Галина", role: "Бухгалтерия 07", icon: "💼" },
            "U-008":      { name: "Светлана", role: "Бухгалтерия 08", icon: "📈" },
            "U-009":      { name: "Татьяна / Любовь", role: "Бухгалтерия / Склад (Ёжик)", icon: "📦" },
            "U-010":      { name: "Наталья", role: "Бухгалтерия 10", icon: "🗂️" },
            "U-507":      { name: "Галина (Дом)", role: "Бухгалтерия (Удаленно)", icon: "💼" }
        };"""

html = html.replace(top_script_target, top_script_replacement)

# 2. Update initial storeData keys (change ULTARIX-07 to U-007, U-09 to U-009)
html = html.replace('"ULTARIX-07": {', '"U-007": {')
html = html.replace('"U-09": {', '"U-009": {')

# 3. Update candidatePcs
cand_target = """        // Live check across all possible computer names
        const candidatePcs = [
            "ULTARIX-07", "Ulta_007", "PC-07",
            "U-09", "PC-09", "ULTARIX-09",
            "PC-02", "Ulka-02", "ULTARIX-02",
            "ULTARIX-03", "ULTARIX-04", "ULTARIX-05", "ULTARIX-06", "ULTARIX-08", "ULTARIX-010", "ULPS1"
        ];"""

cand_replacement = """        // Live check across canonical computer names (U-XXX format)
        const candidatePcs = [
            "ULPS1",
            "U-002", "U-003", "U-004", "U-005", "U-006",
            "U-007", "U-008", "U-009", "U-010",
            "U-507"
        ];"""

html = html.replace(cand_target, cand_replacement)

# 4. Normalize host in callbacks
html = html.replace("window.updateHostStatus = function(pc, data) {", "window.updateHostStatus = function(rawPc, data) {\n            const pc = normalizeHost(rawPc);")
html = html.replace("window.updateDaySummary = function(pc, date, dayData) {", "window.updateDaySummary = function(rawPc, date, dayData) {\n            const pc = normalizeHost(rawPc);")

# 5. Sort entries in renderDashboard()
sort_target = """            let activeCount = 0;
            const entries = Object.entries(storeData);"""

sort_replacement = """            let activeCount = 0;
            const entries = Object.entries(storeData);
            entries.sort((a, b) => {
                if (a[0] === "ULPS1") return -1;
                if (b[0] === "ULPS1") return 1;
                return a[0].localeCompare(b[0], undefined, { numeric: true });
            });"""

html = html.replace(sort_target, sort_replacement)

# 6. Normalize computer when receiving REST API in checkAllComputersLive
rest_pc_target = "const pc = c.computer;"
rest_pc_replacement = "const pc = normalizeHost(c.computer);"
html = html.replace(rest_pc_target, rest_pc_replacement)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated dashboard.html successfully.")
