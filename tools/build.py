"""Build the installable PWA (docs/, served by GitHub Pages) from src/app.html. Run: python3 tools/build.py"""
import json, pathlib, shutil
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "src" / "app.html").read_text(encoding="utf-8")
dist = root / "docs"
dist.mkdir(exist_ok=True)

pwa = """<script>
if ('serviceWorker' in navigator && !window.claude) {
  addEventListener('load', () => navigator.serviceWorker.register('./sw.js').catch(() => {}));
}
</script>"""
head = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1d6f55">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="明智選擇">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-180.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
</head>
<body>
"""
html = head + src.replace("<!--PWA-HEAD-->", pwa) + "\n</body>\n</html>\n"
(dist / "index.html").write_text(html, encoding="utf-8")

manifest = {
    "name": "明智選擇", "short_name": "明智選擇", "lang": "zh-Hant",
    "description": "根據你的處境與公開資料，排出最值得實踐的行動。",
    "start_url": "./", "scope": "./", "display": "standalone",
    "background_color": "#f4f6f2", "theme_color": "#1d6f55",
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}
(dist / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
shutil.copy(root / "src" / "sw.js", dist / "sw.js")
shutil.copy(root / "src" / "icon.svg", dist / "icon.svg")
for f in (root / "src").glob("icon-*.png"):
    shutil.copy(f, dist / f.name)
print("built", dist)
