from pathlib import Path


# File names
html_file = "index.html"
css_file = "index.css"
js_file = "index.js"
output_file = "main.html"

# Read files
html = Path(html_file).read_text(encoding="utf-8")
css = Path(css_file).read_text(encoding="utf-8")
js = Path(js_file).read_text(encoding="utf-8")

# Replace template placeholders
html = html.replace("{{STYLE}}", f"<style>\n{css}\n</style>")
html = html.replace("{{SCRIPT}}", f"<script>\n{js}\n</script>")

# Write output
Path(output_file).write_text(html, encoding="utf-8")

print(f"Created {output_file}")
