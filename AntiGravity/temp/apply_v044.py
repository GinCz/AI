import re
import os

cs_path = "/AI/GitHub/Windows/GIN-Desktop/src/GIN-Desktop.cs"
with open(cs_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update version v043 -> v044
code = re.sub(r'\[assembly: AssemblyTitle\("GIN-Desktop_v043"\)\]', '[assembly: AssemblyTitle("GIN-Desktop_v044")]', code)
code = re.sub(r'\[assembly: AssemblyDescription\("GIN-Desktop_v043"\)\]', '[assembly: AssemblyDescription("GIN-Desktop_v044")]', code)
code = re.sub(r'\[assembly: AssemblyProduct\("GIN-Desktop_v043"\)\]', '[assembly: AssemblyProduct("GIN-Desktop_v044")]', code)
code = re.sub(r'\[assembly: AssemblyVersion\("0\.43\.0\.0"\)\]', '[assembly: AssemblyVersion("0.44.0.0")]', code)
code = re.sub(r'\[assembly: AssemblyFileVersion\("0\.43\.0\.0"\)\]', '[assembly: AssemblyFileVersion("0.44.0.0")]', code)
code = code.replace('GIN-Desktop/v043', 'GIN-Desktop/v044')
code = code.replace('⚡ GIN Dock Wallpaper v043', '⚡ GIN Dock Wallpaper v044')
code = code.replace('GIN Dock Wallpaper v043', 'GIN Dock Wallpaper v044')
code = code.replace('CURRENT_VERSION = "v043";', 'CURRENT_VERSION = "v044";')
code = code.replace('Text = "v043"', 'Text = "v044"')

# 2. WeatherService replacement
old_ws_pattern = r'    // ==========================================\s+// WEATHER SERVICE \(Open-Meteo & wttr\.in\)\s+// ==========================================\s+public static class WeatherService \{[\s\S]*?return I18n\.CurrentLanguage == "ru" \? "Гроза" : \(I18n\.CurrentLanguage == "cs" \? "Bouřka" : "Storm"\);\s+\}\s+\}'

new_ws = '''    // ==========================================
    // WEATHER SERVICE (Open-Meteo & wttr.in)
    // ==========================================
    public static class WeatherService {
        private static string _cachedWeather = null;
        private static string _cachedLanguage = null;
        private static string _cachedSource = null;
        private static string _cachedCity = null;
        private static DateTime _lastFetch = DateTime.MinValue;

        public static void InvalidateCache() {
            _cachedWeather = null;
            _cachedLanguage = null;
            _cachedSource = null;
            _cachedCity = null;
            _lastFetch = DateTime.MinValue;
        }

        public static string GetCurrentWeather(string source, string city) {
            string curLang = (I18n.CurrentLanguage ?? "ru").ToLowerInvariant();
            if (_cachedWeather != null &&
                string.Equals(_cachedLanguage, curLang, StringComparison.OrdinalIgnoreCase) &&
                string.Equals(_cachedSource, source, StringComparison.OrdinalIgnoreCase) &&
                string.Equals(_cachedCity, city, StringComparison.OrdinalIgnoreCase) &&
                (DateTime.Now - _lastFetch).TotalMinutes < 30) {
                return _cachedWeather;
            }

            try {
                using (WebClient wc = new WebClient()) {
                    wc.Headers.Add("User-Agent", "GIN-Desktop/v044 (Windows; WinAPI)");
                    wc.Encoding = Encoding.UTF8;

                    if (string.Equals(source, "wttr.in", StringComparison.OrdinalIgnoreCase)) {
                        string loc = (string.IsNullOrEmpty(city) || city.Equals("Auto", StringComparison.OrdinalIgnoreCase)) ? "" : Uri.EscapeDataString(city);
                        string langParam = (curLang == "ru") ? "ru" : ((curLang == "cs") ? "cs" : "en");
                        string url = "https://wttr.in/" + loc + "?format=%c+%t+(%C)&m&lang=" + langParam;
                        string res = wc.DownloadString(url).Trim();
                        if (!string.IsNullOrEmpty(res) && !res.Contains("<html")) {
                            res = SanitizeWeatherString(res);
                            _cachedWeather = res;
                            _cachedLanguage = curLang;
                            _cachedSource = source;
                            _cachedCity = city;
                            _lastFetch = DateTime.Now;
                            return _cachedWeather;
                        }
                    }

                    // Open-Meteo default
                    string targetCity = (string.IsNullOrEmpty(city) || city.Equals("Auto", StringComparison.OrdinalIgnoreCase)) ? "Prague" : city;
                    double lat = 50.08, lon = 14.43;
                    try {
                        string geoUrl = "https://geocoding-api.open-meteo.com/v1/search?name=" + Uri.EscapeDataString(targetCity) + "&count=1&language=en&format=json";
                        string geoJson = wc.DownloadString(geoUrl);
                        int latIdx = geoJson.IndexOf("\\\"latitude\\\":");
                        if (latIdx != -1) {
                            latIdx += 11;
                            int latEnd = geoJson.IndexOfAny(new char[] { ',', '}' }, latIdx);
                            double.TryParse(geoJson.Substring(latIdx, latEnd - latIdx).Trim(), NumberStyles.Any, CultureInfo.InvariantCulture, out lat);
                        }
                        int lonIdx = geoJson.IndexOf("\\\"longitude\\\":");
                        if (lonIdx != -1) {
                            lonIdx += 12;
                            int lonEnd = geoJson.IndexOfAny(new char[] { ',', '}' }, lonIdx);
                            double.TryParse(geoJson.Substring(lonIdx, lonEnd - lonIdx).Trim(), NumberStyles.Any, CultureInfo.InvariantCulture, out lon);
                        }
                    } catch { }

                    string weatherUrl = string.Format(CultureInfo.InvariantCulture,
                        "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&current=temperature_2m,weather_code",
                        lat, lon);
                    string wJson = wc.DownloadString(weatherUrl);

                    double temp = 0;
                    int tempIdx = wJson.IndexOf("\\\"temperature_2m\\\":");
                    if (tempIdx != -1) {
                        tempIdx += 17;
                        int tempEnd = wJson.IndexOfAny(new char[] { ',', '}' }, tempIdx);
                        double.TryParse(wJson.Substring(tempIdx, tempEnd - tempIdx).Trim(), NumberStyles.Any, CultureInfo.InvariantCulture, out temp);
                    }

                    int code = 0;
                    int codeIdx = wJson.IndexOf("\\\"weather_code\\\":");
                    if (codeIdx != -1) {
                        codeIdx += 15;
                        int codeEnd = wJson.IndexOfAny(new char[] { ',', '}' }, codeIdx);
                        int.TryParse(wJson.Substring(codeIdx, codeEnd - codeIdx).Trim(), out code);
                    }

                    string icon = GetWeatherIcon(code);
                    string desc = GetWeatherDescription(code);
                    string sign = temp > 0 ? "+" : "";
                    string formatted = string.Format("{0} {1}{2:0}°C · {3}", icon, sign, temp, desc);
                    formatted = SanitizeWeatherString(formatted);

                    _cachedWeather = formatted;
                    _cachedLanguage = curLang;
                    _cachedSource = source;
                    _cachedCity = city;
                    _lastFetch = DateTime.Now;
                    return _cachedWeather;
                }
            } catch { }

            string fallbackDesc = curLang == "ru" ? "Ясно" : (curLang == "cs" ? "Jasno" : "Clear");
            return _cachedWeather ?? ("☀ +18°C · " + fallbackDesc);
        }

        private static string SanitizeWeatherString(string input) {
            if (string.IsNullOrEmpty(input)) return "";
            return input
                .Replace("\\uFE0F", "")
                .Replace("\\uFE0E", "")
                .Replace("\\u200D", "")
                .Replace("\\uFFFD", "")
                .Trim();
        }

        private static string GetWeatherIcon(int code) {
            if (code == 0) return "☀";      // U+2600 Clean sun (NO \\uFE0F)
            if (code <= 3) return "⛅";     // U+26C5 Sun behind cloud (NO \\uFE0F)
            if (code <= 48) return "☁";     // U+2601 Cloud / Fog (NO \\uFE0F)
            if (code <= 67) return "🌧";     // U+1F327 Rain
            if (code <= 77) return "❄";     // U+2744 Snowflake (NO \\uFE0F)
            if (code <= 82) return "🌦";     // U+1F326 Sun behind rain
            return "⚡";                     // U+26A1 Lightning / Storm (NO \\uFE0F)
        }

        private static string GetWeatherDescription(int code) {
            string lang = (I18n.CurrentLanguage ?? "ru").ToLowerInvariant();
            if (code == 0) return lang == "ru" ? "Ясно" : (lang == "cs" ? "Jasno" : "Clear");
            if (code <= 3) return lang == "ru" ? "Переменная облачность" : (lang == "cs" ? "Polojasno" : "Partly Cloudy");
            if (code <= 48) return lang == "ru" ? "Туман" : (lang == "cs" ? "Mlha" : "Fog");
            if (code <= 67) return lang == "ru" ? "Дождь" : (lang == "cs" ? "Déšť" : "Rain");
            if (code <= 77) return lang == "ru" ? "Снег" : (lang == "cs" ? "Sníh" : "Snow");
            return lang == "ru" ? "Гроза" : (lang == "cs" ? "Bouřka" : "Storm");
        }
    }'''

code = re.sub(old_ws_pattern, lambda m: new_ws, code)

# 3. Update I18n dictionary for Interval & hours
# EN:
code = code.replace(
    '                { "WallInterval", "Auto-Change Interval:" },\n                { "WallpaperInterval", "Wallpaper Change Interval:" },',
    '                { "WallInterval", "Interval:" },\n                { "WallpaperInterval", "Interval:" },\n                { "Int1h", "1 hour" },\n                { "Int3h", "3 hours" },\n                { "Int6h", "6 hours" },\n                { "Int12h", "12 hours" },\n                { "Int24h", "24 hours" },'
)
# RU:
code = code.replace(
    '                { "WallInterval", "Интервал смены обоев:" },\n                { "WallpaperInterval", "Интервал смены обоев:" },',
    '                { "WallInterval", "Интервал:" },\n                { "WallpaperInterval", "Интервал:" },\n                { "Int1h", "1 час" },\n                { "Int3h", "3 часа" },\n                { "Int6h", "6 часов" },\n                { "Int12h", "12 часов" },\n                { "Int24h", "24 часа" },'
)
# CS:
code = code.replace(
    '                { "WallInterval", "Interval výměny tapety:" },\n                { "WallpaperInterval", "Interval výměny tapety:" },',
    '                { "WallInterval", "Interval:" },\n                { "WallpaperInterval", "Interval:" },\n                { "Int1h", "1 hodina" },\n                { "Int3h", "3 hodiny" },\n                { "Int6h", "6 hodin" },\n                { "Int12h", "12 hodin" },\n                { "Int24h", "24 hodin" },'
)

# 4. Localize Calendar Month & Day names + Weather font in WallpaperEngine
old_cal_render = '''                string fontName = _config.CalendarFontFamily ?? "Segoe UI";
                string monthTitle = now.ToString("MMMM yyyy", CultureInfo.CurrentCulture).ToUpperInvariant();
                float titleFontSize = Math.Max(10f, cardW * 0.052f);

                using (Font titleFont = new Font(fontName, titleFontSize, FontStyle.Bold))
                using (SolidBrush textBrush = new SolidBrush(theme.TextPrimary))
                using (SolidBrush accentBrush = new SolidBrush(theme.Accent)) {
                    g.DrawString(monthTitle, titleFont, accentBrush, cardX + 16, cardY + 12);

                    string[] days = new string[] { "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su" };'''

new_cal_render = '''                string fontName = _config.CalendarFontFamily ?? "Segoe UI";

                CultureInfo cult;
                string[] days;
                string curLang = (I18n.CurrentLanguage ?? "ru").ToLowerInvariant();
                if (curLang == "ru") {
                    cult = new CultureInfo("ru-RU");
                    days = new string[] { "Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс" };
                } else if (curLang == "cs") {
                    cult = new CultureInfo("cs-CZ");
                    days = new string[] { "Po", "Út", "St", "Čt", "Pá", "So", "Ne" };
                } else {
                    cult = new CultureInfo("en-US");
                    days = new string[] { "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su" };
                }
                string monthTitle = now.ToString("MMMM yyyy", cult).ToUpperInvariant();
                float titleFontSize = Math.Max(10f, cardW * 0.052f);

                using (Font titleFont = new Font(fontName, titleFontSize, FontStyle.Bold))
                using (SolidBrush textBrush = new SolidBrush(theme.TextPrimary))
                using (SolidBrush accentBrush = new SolidBrush(theme.Accent)) {
                    g.DrawString(monthTitle, titleFont, accentBrush, cardX + 16, cardY + 12);'''

code = code.replace(old_cal_render, new_cal_render)

# Weather HUD font: use Segoe UI so emojis and symbols never tofu
old_wfont = 'using (Font wFont = new Font(fontName, Math.Max(8.5f, cardW * 0.040f), FontStyle.Bold))'
new_wfont = 'using (Font wFont = new Font("Segoe UI", Math.Max(9.0f, cardW * 0.042f), FontStyle.Bold))'
code = code.replace(old_wfont, new_wfont)

# 5. SettingsForm field declarations
old_fields = '''        private Label _lblIntervalTitle;
        private Button _btnInt1h;
        private Button _btnInt3h;
        private Button _btnInt6h;
        private Button _btnInt24h;'''

new_fields = '''        private Label _lblIntervalTitle;
        private Button _btnInt1h;
        private Button _btnInt3h;
        private Button _btnInt6h;
        private Button _btnInt12h;
        private Button _btnInt24h;
        private List<Panel> _separatorLines = new List<Panel>();'''

code = code.replace(old_fields, new_fields)

# 6. Form Size and Tabs size
code = code.replace('this.ClientSize = new Size(760, 656);', 'this.ClientSize = new Size(760, 780);')
code = code.replace('_tabs = new TabControl { Location = new Point(12, 42), Size = new Size(736, 565) };', '_tabs = new TabControl { Location = new Point(12, 42), Size = new Size(736, 680) };')
code = code.replace('_bottomBar = new Panel { Location = new Point(12, 612), Size = new Size(736, 38), BackColor = Color.Transparent };', '_bottomBar = new Panel { Location = new Point(12, 730), Size = new Size(736, 38), BackColor = Color.Transparent };')

# 7. Language buttons in SettingsForm: invalidate cache and trigger re-render
old_lang_clicks = '''            _btnLangEN.Click += (s, e) => { _config.Language = "en"; I18n.SetLanguage("en"); ApplyLocalization(); ApplyThemeColors(); PlayClickSound(); };
            _btnLangRU.Click += (s, e) => { _config.Language = "ru"; I18n.SetLanguage("ru"); ApplyLocalization(); ApplyThemeColors(); PlayClickSound(); };
            _btnLangCS.Click += (s, e) => { _config.Language = "cs"; I18n.SetLanguage("cs"); ApplyLocalization(); ApplyThemeColors(); PlayClickSound(); };'''

new_lang_clicks = '''            Action<string> changeLanguage = (lang) => {
                _config.Language = lang;
                I18n.SetLanguage(lang);
                WeatherService.InvalidateCache();
                ApplyLocalization();
                ApplyThemeColors();
                if (_wallpaperEngine != null) {
                    _wallpaperEngine.TriggerNextWallpaperAsync();
                }
                if (_onConfigChanged != null) _onConfigChanged();
                PlayClickSound();
            };
            _btnLangEN.Click += (s, e) => changeLanguage("en");
            _btnLangRU.Click += (s, e) => changeLanguage("ru");
            _btnLangCS.Click += (s, e) => changeLanguage("cs");'''

code = code.replace(old_lang_clicks, new_lang_clicks)

# 8. TAB 2: WALLPAPER & CALENDAR controls layout
old_tab_wall = '''            // =====================================
            // TAB 2: WALLPAPER & CALENDAR
            // =====================================
            _tabWall = new TabPage { Text = I18n.T("TabWallpaper") };

            _lblWallThemesTitle = new Label { Location = new Point(20, 6), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            _tabWall.Controls.Add(_lblWallThemesTitle);

            _chkCatAll = new CheckBox { Text = "🎲 " + I18n.T("CatAll"), Location = new Point(25, 24), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            _chkCatAll.CheckedChanged += ChkCatAll_CheckedChanged;
            _tabWall.Controls.Add(_chkCatAll);

            string[] catKeys = new string[] {
                "3d", "nature", "flowers", "animals", "ocean", "cars", "space", "trucks", "girls", "city",
                "cyberpunk", "minimalism", "anime", "darkhorse", "macro", "architecture", "aircraft", "retrowave", "fantasy", "underwater"
            };
            string[] catNames = new string[] {
                "Cat3D", "CatNature", "CatFlowers", "CatAnimals", "CatOcean", "CatCars", "CatSpace", "CatTrucks", "CatGirls", "CatCity",
                "CatCyberpunk", "CatMinimalism", "CatAnime", "CatDarkHorse", "CatMacro", "CatArchitecture", "CatAircraft", "CatRetrowave", "CatFantasy", "CatUnderwater"
            };

            string activeCats = (_config.WallpaperCategories ?? "all").ToLowerInvariant();
            // Two wide columns (Width = 330 each, avoiding all text cutoffs!)
            for (int i = 0; i < catKeys.Length; i++) {
                string key = catKeys[i];
                int col = i / 10;
                int row = i % 10;
                int xPos = (col == 0) ? 25 : 370;
                int yPos = 42 + row * 18;
                CheckBox cb = new CheckBox {
                    Text = I18n.T(catNames[i]),
                    Tag = key,
                    Location = new Point(xPos, yPos),
                    Size = new Size(330, 18),
                    AutoSize = false,
                    Font = new Font("Segoe UI", 9f)
                };
                cb.Checked = (activeCats.Contains("all") || activeCats.Contains(key));
                cb.CheckedChanged += ChildCategory_CheckedChanged;
                _catCheckBoxes[key] = cb;
                _tabWall.Controls.Add(cb);
            }
            SyncMasterCheckboxState();

            // Interval Buttons
            _lblIntervalTitle = new Label { Location = new Point(20, 226), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            _btnInt1h = new Button { Text = "1 " + I18n.T("Hour"), Tag = 60, Size = new Size(125, 25), Location = new Point(25, 246), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand };
            _btnInt3h = new Button { Text = "3 " + I18n.T("Hours"), Tag = 180, Size = new Size(125, 25), Location = new Point(160, 246), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand };
            _btnInt6h = new Button { Text = "6 " + I18n.T("Hours"), Tag = 360, Size = new Size(125, 25), Location = new Point(295, 246), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand };
            _btnInt24h = new Button { Text = "24 " + I18n.T("Hours"), Tag = 1440, Size = new Size(125, 25), Location = new Point(430, 246), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand };

            EventHandler intClick = (s, e) => {
                _config.WallpaperIntervalMinutes = (int)((Button)s).Tag;
                UpdateIntervalButtonStyles();
                PlayClickSound();
            };
            _btnInt1h.Click += intClick;
            _btnInt3h.Click += intClick;
            _btnInt6h.Click += intClick;
            _btnInt24h.Click += intClick;

            _tabWall.Controls.AddRange(new Control[] { _lblIntervalTitle, _btnInt1h, _btnInt3h, _btnInt6h, _btnInt24h });

            // Calendar Section (Clean "Календарь:" + 5 Full-Width Buttons)
            _lblCalTitle = new Label { Text = "📅 " + I18n.T("Calendar") + ":", Location = new Point(25, 280), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };

            _btnScaleNone = new Button { Text = I18n.T("CalScaleNone"), Tag = 0.0f, Size = new Size(108, 25), Location = new Point(135, 276), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnScaleSmall = new Button { Text = I18n.T("CalScaleSmall"), Tag = 0.75f, Size = new Size(108, 25), Location = new Point(250, 276), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnScaleMed = new Button { Text = I18n.T("CalScaleMedium"), Tag = 1.0f, Size = new Size(108, 25), Location = new Point(365, 276), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnScaleLarge = new Button { Text = I18n.T("CalScaleLarge"), Tag = 1.3f, Size = new Size(108, 25), Location = new Point(480, 276), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnScaleHuge = new Button { Text = I18n.T("CalScaleHuge"), Tag = 1.6f, Size = new Size(108, 25), Location = new Point(595, 276), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };

            _btnScaleNone.Click += (s, e) => {
                _config.ShowCalendar = false;
                _config.Save();
                UpdateCalScaleButtonStyles();
                PlayClickSound();
                if (_wallpaperEngine != null) {
                    _wallpaperEngine.TriggerNextWallpaperAsync();
                }
            };

            EventHandler scaleClick = (s, e) => {
                float sc = (float)((Button)s).Tag;
                _config.CalendarScale = sc;
                _config.ShowCalendar = true;
                _config.Save();
                UpdateCalScaleButtonStyles();
                PlayClickSound();
                if (_wallpaperEngine != null) {
                    _wallpaperEngine.TriggerNextWallpaperAsync();
                }
            };
            _btnScaleSmall.Click += scaleClick;
            _btnScaleMed.Click += scaleClick;
            _btnScaleLarge.Click += scaleClick;
            _btnScaleHuge.Click += scaleClick;

            _tabWall.Controls.AddRange(new Control[] { _lblCalTitle, _btnScaleNone, _btnScaleSmall, _btnScaleMed, _btnScaleLarge, _btnScaleHuge });

            // 24 Curated Artistic & Graphic Font Buttons
            _lblFontsHeader = new Label { Location = new Point(20, 307), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            _tabWall.Controls.Add(_lblFontsHeader);

            string[] curatedFonts = new string[] {
                "Segoe UI", "Tahoma", "Arial", "Verdana",
                "Georgia", "Corbel", "Consolas", "Trebuchet MS",
                "Cambria", "Century Gothic", "Candara", "Calibri",
                "Gabriola", "Ink Free", "Impact", "Comic Sans MS",
                "Sitka Banner", "Palatino Linotype", "Garamond", "Franklin Gothic Medium",
                "Constantia", "Lucida Console", "Bookman Old Style", "Sylfaen"
            };

            for (int i = 0; i < curatedFonts.Length; i++) {
                int col = i % 4;
                int row = i / 4;
                string fontName = curatedFonts[i];
                Button bFont = new Button {
                    Text = fontName,
                    Tag = fontName,
                    Size = new Size(160, 23),
                    Location = new Point(25 + col * 170, 326 + row * 25),
                    FlatStyle = FlatStyle.Flat,
                    Cursor = Cursors.Hand
                };
                try {
                    bFont.Font = new Font(fontName, 9.5f, FontStyle.Regular);
                } catch {
                    bFont.Font = new Font("Segoe UI", 9.5f, FontStyle.Regular);
                }

                bFont.Click += (s, e) => {
                    string chosen = (string)((Button)s).Tag;
                    _config.CalendarFontFamily = chosen;
                    _config.ShowCalendar = true;
                    _config.Save();
                    UpdateFontButtonStyles();
                    UpdateCalScaleButtonStyles();
                    PlayClickSound();
                    if (_wallpaperEngine != null) {
                        _wallpaperEngine.TriggerNextWallpaperAsync();
                    }
                };
                _fontButtons.Add(bFont);
                _tabWall.Controls.Add(bFont);
            }

            _btnNextWall = new Button {
                Text = "🖼️ " + I18n.T("NextWallpaper"),
                Location = new Point(25, 480),
                Width = 325,
                Height = 28,
                FlatStyle = FlatStyle.Flat,
                Cursor = Cursors.Hand,
                Font = new Font("Segoe UI", 9.5f, FontStyle.Bold)
            };
            _btnNextWall.Click += (s, e) => {
                if (_wallpaperEngine != null) {
                    _wallpaperEngine.TriggerNextWallpaperAsync();
                    PlayClickSound();
                }
            };

            _btnSavePic = new Button {
                Text = "💾 " + I18n.T("BtnSaveWall"),
                Location = new Point(355, 480),
                Width = 350,
                Height = 28,
                FlatStyle = FlatStyle.Flat,
                Cursor = Cursors.Hand,
                Font = new Font("Segoe UI", 9.5f)
            };
            _btnSavePic.Click += (s, e) => {
                if (_wallpaperEngine != null) {
                    _wallpaperEngine.SaveActiveWallpaperToPictures();
                    PlayClickSound();
                }
            };

            _tabWall.Controls.AddRange(new Control[] { _btnNextWall, _btnSavePic });

            // Weather HUD section
            Label lblWeatherTitle = new Label { Text = "🌤️ " + (I18n.CurrentLanguage == "ru" ? "Погода под календарем:" : (I18n.CurrentLanguage == "cs" ? "Počasí:" : "Weather HUD:")), Location = new Point(25, 514), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            CheckBox chkShowWeather = new CheckBox { Text = (I18n.CurrentLanguage == "ru" ? "Включить погоду" : (I18n.CurrentLanguage == "cs" ? "Povolit počasí" : "Enable Weather")), Checked = _config.ShowWeather, Location = new Point(230, 513), AutoSize = true, Font = new Font("Segoe UI", 9f) };
            chkShowWeather.CheckedChanged += (s, e) => {
                _config.ShowWeather = chkShowWeather.Checked;
                _config.Save();
                if (_wallpaperEngine != null) _wallpaperEngine.TriggerNextWallpaperAsync();
            };

            ComboBox cmbWeatherSrc = new ComboBox { Location = new Point(370, 511), Width = 150, DropDownStyle = ComboBoxStyle.DropDownList, Font = new Font("Segoe UI", 9f) };
            cmbWeatherSrc.Items.AddRange(new string[] { "Open-Meteo", "wttr.in" });
            cmbWeatherSrc.SelectedItem = _config.WeatherSource;
            cmbWeatherSrc.SelectedIndexChanged += (s, e) => {
                _config.WeatherSource = cmbWeatherSrc.SelectedItem.ToString();
                _config.Save();
                if (_wallpaperEngine != null) _wallpaperEngine.TriggerNextWallpaperAsync();
            };

            TextBox txtWeatherCity = new TextBox { Location = new Point(535, 511), Width = 170, Text = _config.WeatherCity, Font = new Font("Segoe UI", 9f) };
            txtWeatherCity.TextChanged += (s, e) => {
                _config.WeatherCity = txtWeatherCity.Text.Trim();
                _config.Save();
            };

            _tabWall.Controls.AddRange(new Control[] { lblWeatherTitle, chkShowWeather, cmbWeatherSrc, txtWeatherCity });
            _tabs.TabPages.Add(_tabWall);'''

new_tab_wall = '''            // =====================================
            // TAB 2: WALLPAPER & CALENDAR
            // =====================================
            _tabWall = new TabPage { Text = I18n.T("TabWallpaper") };

            _lblWallThemesTitle = new Label { Location = new Point(20, 8), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            _tabWall.Controls.Add(_lblWallThemesTitle);

            _chkCatAll = new CheckBox { Text = "🎲 " + I18n.T("CatAll"), Location = new Point(25, 26), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            _chkCatAll.CheckedChanged += ChkCatAll_CheckedChanged;
            _tabWall.Controls.Add(_chkCatAll);

            string[] catKeys = new string[] {
                "3d", "nature", "flowers", "animals", "ocean", "cars", "space", "trucks", "girls", "city",
                "cyberpunk", "minimalism", "anime", "darkhorse", "macro", "architecture", "aircraft", "retrowave", "fantasy", "underwater"
            };
            string[] catNames = new string[] {
                "Cat3D", "CatNature", "CatFlowers", "CatAnimals", "CatOcean", "CatCars", "CatSpace", "CatTrucks", "CatGirls", "CatCity",
                "CatCyberpunk", "CatMinimalism", "CatAnime", "CatDarkHorse", "CatMacro", "CatArchitecture", "CatAircraft", "CatRetrowave", "CatFantasy", "CatUnderwater"
            };

            string activeCats = (_config.WallpaperCategories ?? "all").ToLowerInvariant();
            for (int i = 0; i < catKeys.Length; i++) {
                string key = catKeys[i];
                int col = i / 10;
                int row = i % 10;
                int xPos = (col == 0) ? 25 : 370;
                int yPos = 44 + row * 18;
                CheckBox cb = new CheckBox {
                    Text = I18n.T(catNames[i]),
                    Tag = key,
                    Location = new Point(xPos, yPos),
                    Size = new Size(330, 18),
                    AutoSize = false,
                    Font = new Font("Segoe UI", 9f)
                };
                cb.Checked = (activeCats.Contains("all") || activeCats.Contains(key));
                cb.CheckedChanged += ChildCategory_CheckedChanged;
                _catCheckBoxes[key] = cb;
                _tabWall.Controls.Add(cb);
            }
            SyncMasterCheckboxState();

            // Separator 1: Between Categories and Interval
            Panel sep1 = new Panel { Location = new Point(25, 230), Size = new Size(678, 1), BackColor = theme.Separator };
            _separatorLines.Add(sep1);
            _tabWall.Controls.Add(sep1);

            // Interval Section: Clean single row (Label + 5 Buttons: 1h, 3h, 6h, 12h, 24h)
            _lblIntervalTitle = new Label { Location = new Point(25, 243), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            _btnInt1h = new Button { Text = I18n.T("Int1h"), Tag = 60, Size = new Size(108, 26), Location = new Point(135, 240), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnInt3h = new Button { Text = I18n.T("Int3h"), Tag = 180, Size = new Size(108, 26), Location = new Point(250, 240), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnInt6h = new Button { Text = I18n.T("Int6h"), Tag = 360, Size = new Size(108, 26), Location = new Point(365, 240), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnInt12h = new Button { Text = I18n.T("Int12h"), Tag = 720, Size = new Size(108, 26), Location = new Point(480, 240), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnInt24h = new Button { Text = I18n.T("Int24h"), Tag = 1440, Size = new Size(108, 26), Location = new Point(595, 240), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };

            EventHandler intClick = (s, e) => {
                _config.WallpaperIntervalMinutes = (int)((Button)s).Tag;
                UpdateIntervalButtonStyles();
                PlayClickSound();
            };
            _btnInt1h.Click += intClick;
            _btnInt3h.Click += intClick;
            _btnInt6h.Click += intClick;
            _btnInt12h.Click += intClick;
            _btnInt24h.Click += intClick;

            _tabWall.Controls.AddRange(new Control[] { _lblIntervalTitle, _btnInt1h, _btnInt3h, _btnInt6h, _btnInt12h, _btnInt24h });

            // Separator 2: Between Interval and Calendar
            Panel sep2 = new Panel { Location = new Point(25, 274), Size = new Size(678, 1), BackColor = theme.Separator };
            _separatorLines.Add(sep2);
            _tabWall.Controls.Add(sep2);

            // Calendar Section: Clean single row (Label + 5 Buttons)
            _lblCalTitle = new Label { Text = "📅 " + I18n.T("Calendar") + ":", Location = new Point(25, 287), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };

            _btnScaleNone = new Button { Text = I18n.T("CalScaleNone"), Tag = 0.0f, Size = new Size(108, 26), Location = new Point(135, 284), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnScaleSmall = new Button { Text = I18n.T("CalScaleSmall"), Tag = 0.75f, Size = new Size(108, 26), Location = new Point(250, 284), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnScaleMed = new Button { Text = I18n.T("CalScaleMedium"), Tag = 1.0f, Size = new Size(108, 26), Location = new Point(365, 284), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnScaleLarge = new Button { Text = I18n.T("CalScaleLarge"), Tag = 1.3f, Size = new Size(108, 26), Location = new Point(480, 284), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };
            _btnScaleHuge = new Button { Text = I18n.T("CalScaleHuge"), Tag = 1.6f, Size = new Size(108, 26), Location = new Point(595, 284), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand, Font = new Font("Segoe UI", 9f) };

            _btnScaleNone.Click += (s, e) => {
                _config.ShowCalendar = false;
                _config.Save();
                UpdateCalScaleButtonStyles();
                PlayClickSound();
                if (_wallpaperEngine != null) {
                    _wallpaperEngine.TriggerNextWallpaperAsync();
                }
            };

            EventHandler scaleClick = (s, e) => {
                float sc = (float)((Button)s).Tag;
                _config.CalendarScale = sc;
                _config.ShowCalendar = true;
                _config.Save();
                UpdateCalScaleButtonStyles();
                PlayClickSound();
                if (_wallpaperEngine != null) {
                    _wallpaperEngine.TriggerNextWallpaperAsync();
                }
            };
            _btnScaleSmall.Click += scaleClick;
            _btnScaleMed.Click += scaleClick;
            _btnScaleLarge.Click += scaleClick;
            _btnScaleHuge.Click += scaleClick;

            _tabWall.Controls.AddRange(new Control[] { _lblCalTitle, _btnScaleNone, _btnScaleSmall, _btnScaleMed, _btnScaleLarge, _btnScaleHuge });

            // Separator 3: Between Calendar and Font Grid
            Panel sep3 = new Panel { Location = new Point(25, 318), Size = new Size(678, 1), BackColor = theme.Separator };
            _separatorLines.Add(sep3);
            _tabWall.Controls.Add(sep3);

            // 24 Curated Font Buttons with ample breathing room (4 cols x 6 rows, H=29)
            _lblFontsHeader = new Label { Location = new Point(25, 326), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            _tabWall.Controls.Add(_lblFontsHeader);

            string[] curatedFonts = new string[] {
                "Segoe UI", "Tahoma", "Arial", "Verdana",
                "Georgia", "Corbel", "Consolas", "Trebuchet MS",
                "Cambria", "Century Gothic", "Candara", "Calibri",
                "Gabriola", "Ink Free", "Impact", "Comic Sans MS",
                "Sitka Banner", "Palatino Linotype", "Garamond", "Franklin Gothic Medium",
                "Constantia", "Lucida Console", "Bookman Old Style", "Sylfaen"
            };

            for (int i = 0; i < curatedFonts.Length; i++) {
                int col = i % 4;
                int row = i / 4;
                string fontName = curatedFonts[i];
                int x = 25 + col * 171;
                int y = 348 + row * 33;
                Button bFont = new Button {
                    Text = fontName,
                    Tag = fontName,
                    Size = new Size(165, 29),
                    Location = new Point(x, y),
                    FlatStyle = FlatStyle.Flat,
                    Cursor = Cursors.Hand,
                    TextAlign = ContentAlignment.MiddleCenter,
                    Padding = Padding.Empty
                };
                float fontSize = 9.0f;
                if (fontName == "Gabriola") fontSize = 8.0f;
                else if (fontName == "Impact" || fontName == "Sitka Banner" || fontName == "Palatino Linotype") fontSize = 8.5f;

                try {
                    bFont.Font = new Font(fontName, fontSize, FontStyle.Regular);
                } catch {
                    bFont.Font = new Font("Segoe UI", fontSize, FontStyle.Regular);
                }

                bFont.Click += (s, e) => {
                    string chosen = (string)((Button)s).Tag;
                    _config.CalendarFontFamily = chosen;
                    _config.ShowCalendar = true;
                    _config.Save();
                    UpdateFontButtonStyles();
                    UpdateCalScaleButtonStyles();
                    PlayClickSound();
                    if (_wallpaperEngine != null) {
                        _wallpaperEngine.TriggerNextWallpaperAsync();
                    }
                };
                _fontButtons.Add(bFont);
                _tabWall.Controls.Add(bFont);
            }

            // Separator 4: Between Font Grid and Action Buttons
            Panel sep4 = new Panel { Location = new Point(25, 550), Size = new Size(678, 1), BackColor = theme.Separator };
            _separatorLines.Add(sep4);
            _tabWall.Controls.Add(sep4);

            _btnNextWall = new Button {
                Text = "🖼️ " + I18n.T("NextWallpaper"),
                Location = new Point(25, 558),
                Width = 330,
                Height = 32,
                FlatStyle = FlatStyle.Flat,
                Cursor = Cursors.Hand,
                Font = new Font("Segoe UI", 9.5f, FontStyle.Bold)
            };
            _btnNextWall.Click += (s, e) => {
                if (_wallpaperEngine != null) {
                    _wallpaperEngine.TriggerNextWallpaperAsync();
                    PlayClickSound();
                }
            };

            _btnSavePic = new Button {
                Text = "💾 " + I18n.T("BtnSaveWall"),
                Location = new Point(367, 558),
                Width = 336,
                Height = 32,
                FlatStyle = FlatStyle.Flat,
                Cursor = Cursors.Hand,
                Font = new Font("Segoe UI", 9.5f)
            };
            _btnSavePic.Click += (s, e) => {
                if (_wallpaperEngine != null) {
                    _wallpaperEngine.SaveActiveWallpaperToPictures();
                    PlayClickSound();
                }
            };

            _tabWall.Controls.AddRange(new Control[] { _btnNextWall, _btnSavePic });

            // Separator 5: Between Action Buttons and Weather HUD
            Panel sep5 = new Panel { Location = new Point(25, 598), Size = new Size(678, 1), BackColor = theme.Separator };
            _separatorLines.Add(sep5);
            _tabWall.Controls.Add(sep5);

            // Weather HUD section (Beautiful spacing & margins!)
            Label lblWeatherTitle = new Label { Text = "🌤️ " + (I18n.CurrentLanguage == "ru" ? "Погода:" : (I18n.CurrentLanguage == "cs" ? "Počasí:" : "Weather HUD:")), Location = new Point(25, 611), AutoSize = true, Font = new Font("Segoe UI", 9.5f, FontStyle.Bold) };
            CheckBox chkShowWeather = new CheckBox { Text = (I18n.CurrentLanguage == "ru" ? "Включить погоду" : (I18n.CurrentLanguage == "cs" ? "Povolit počasí" : "Enable Weather")), Checked = _config.ShowWeather, Location = new Point(215, 610), AutoSize = true, Font = new Font("Segoe UI", 9f) };
            chkShowWeather.CheckedChanged += (s, e) => {
                _config.ShowWeather = chkShowWeather.Checked;
                _config.Save();
                WeatherService.InvalidateCache();
                if (_wallpaperEngine != null) _wallpaperEngine.TriggerNextWallpaperAsync();
            };

            ComboBox cmbWeatherSrc = new ComboBox { Location = new Point(367, 608), Width = 145, Height = 28, DropDownStyle = ComboBoxStyle.DropDownList, Font = new Font("Segoe UI", 9f) };
            cmbWeatherSrc.Items.AddRange(new string[] { "Open-Meteo", "wttr.in" });
            cmbWeatherSrc.SelectedItem = _config.WeatherSource;
            cmbWeatherSrc.SelectedIndexChanged += (s, e) => {
                _config.WeatherSource = cmbWeatherSrc.SelectedItem.ToString();
                _config.Save();
                WeatherService.InvalidateCache();
                if (_wallpaperEngine != null) _wallpaperEngine.TriggerNextWallpaperAsync();
            };

            TextBox txtWeatherCity = new TextBox { Location = new Point(522, 608), Width = 181, Height = 28, Text = _config.WeatherCity, Font = new Font("Segoe UI", 9f) };
            txtWeatherCity.TextChanged += (s, e) => {
                _config.WeatherCity = txtWeatherCity.Text.Trim();
                _config.Save();
                WeatherService.InvalidateCache();
            };

            _tabWall.Controls.AddRange(new Control[] { lblWeatherTitle, chkShowWeather, cmbWeatherSrc, txtWeatherCity });
            _tabs.TabPages.Add(_tabWall);'''

code = code.replace(old_tab_wall, new_tab_wall)

# 9. ApplyThemeColors: style separators
old_sep_style = '''            // Force repaint of tab headers
            _tabs.Invalidate();'''

new_sep_style = '''            // Style Separator lines
            foreach (Panel sep in _separatorLines) {
                sep.BackColor = theme.Separator;
            }

            // Force repaint of tab headers
            _tabs.Invalidate();'''

code = code.replace(old_sep_style, new_sep_style)

# 10. UpdateIntervalButtonStyles: support _btnInt12h
old_int_styles = '''        private void UpdateIntervalButtonStyles() {
            ColorTheme theme = ThemeManager.GetTheme(_config.ThemeName, _config.DayEveningNightMode);
            int cur = _config.WallpaperIntervalMinutes;
            StyleToggleButton(_btnInt1h, cur <= 60, theme);
            StyleToggleButton(_btnInt3h, cur == 180, theme);
            StyleToggleButton(_btnInt6h, cur == 360, theme);
            StyleToggleButton(_btnInt24h, cur >= 1440, theme);
        }'''

new_int_styles = '''        private void UpdateIntervalButtonStyles() {
            ColorTheme theme = ThemeManager.GetTheme(_config.ThemeName, _config.DayEveningNightMode);
            int cur = _config.WallpaperIntervalMinutes;
            if (_btnInt1h != null) StyleToggleButton(_btnInt1h, cur <= 60, theme);
            if (_btnInt3h != null) StyleToggleButton(_btnInt3h, cur == 180, theme);
            if (_btnInt6h != null) StyleToggleButton(_btnInt6h, cur == 360, theme);
            if (_btnInt12h != null) StyleToggleButton(_btnInt12h, cur == 720, theme);
            if (_btnInt24h != null) StyleToggleButton(_btnInt24h, cur >= 1440, theme);
        }'''

code = code.replace(old_int_styles, new_int_styles)

# 11. ApplyLocalization: update Interval buttons
old_loc_int = '''            _lblIntervalTitle.Text = "⏱️ " + I18n.T("WallpaperInterval");
            _btnInt1h.Text = "1 " + I18n.T("Hour");
            _btnInt3h.Text = "3 " + I18n.T("Hours");
            _btnInt6h.Text = "6 " + I18n.T("Hours");
            _btnInt24h.Text = "24 " + I18n.T("Hours");'''

new_loc_int = '''            _lblIntervalTitle.Text = "⏱️ " + I18n.T("WallpaperInterval");
            if (_btnInt1h != null) _btnInt1h.Text = I18n.T("Int1h");
            if (_btnInt3h != null) _btnInt3h.Text = I18n.T("Int3h");
            if (_btnInt6h != null) _btnInt6h.Text = I18n.T("Int6h");
            if (_btnInt12h != null) _btnInt12h.Text = I18n.T("Int12h");
            if (_btnInt24h != null) _btnInt24h.Text = I18n.T("Int24h");'''

code = code.replace(old_loc_int, new_loc_int)

with open(cs_path, "w", encoding="utf-8") as f:
    f.write(code)

print("✅ GIN-Desktop.cs successfully updated!")
