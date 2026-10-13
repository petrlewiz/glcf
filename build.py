from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import shutil

env  = Environment(loader=FileSystemLoader("templates"))

output_dir = Path("docs")
output_dir.mkdir(exist_ok=True)

pages = [
    "index.html",
    "about.html",
    "listen.html",
    "ministry-groups.html"
]

for page in pages:
    template = env.get_template(page)

    html = template.render()

    output_file = output_dir / page
    output_file.write_text(html, encoding="utf-8")

    print(f"Built {output_file}")