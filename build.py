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
    "ministry-groups.html",
    "events.html",
    "contact.html"
]

for page in pages:
    template = env.get_template(page)

    html = template.render()

    output_file = output_dir / page
    output_file.write_text(html, encoding="utf-8")

    print(f"Built {output_file}")


# ---------------------------------------------------------------------------
# Sermons: add a new dict here for each new sermon.
# "slug" becomes the filename.
# NOTE: Sermon slugs must not match an existing page name (index, about, listen,
# ministry-groups, events, contact), or the sermon will overwrite that page.
# Newest first, so the related-sermons sidebar shows recent messages.
# Leave a field as "" (or delete it) and that part of the page is hidden.
# ---------------------------------------------------------------------------

SERMONS = [
    {
        "title": "Salt and Light",
        "slug": "salt-and-light",
        "date": "2026-01-25",
        "date_display": "January 25, 2026",
        "author": "GLCF",
        "category": "Topical",
        "image": "https://glcfellowship.ca/wp-content/uploads/2025/02/58-open-sermon-event-campaign-placeholder.webp",
        "audio_url": "",
        "video_url": "",
        "scripture": "",
        "summary": "",
        "body": "",
    },
    {
        "title": "The Believers Walk",
        "slug": "the-believers-walk",
        "date": "2025-02-21",
        "date_display": "February 21, 2025",
        "author": "GLCF",
        "category": "",
        "image": "https://glcfellowship.ca/wp-content/uploads/2025/02/Screenshot-2025-04-10-at-6.25.00%20PM-768x430.png",
        "audio_url": "",
        "video_url": "",
        "scripture": "",
        "summary": "",
        "body": "",
    },
    {
        "title": "Confidence In GOD",
        "slug": "welcome-to-the-family-of-god",
        "date": "2025-02-20",
        "date_display": "February 20, 2025",
        "author": "GLCF",
        "category": "",
        "image": "https://glcfellowship.ca/wp-content/uploads/2025/02/Screenshot-2025-04-10-at-6.27.10%20PM-768x428.png",
        "audio_url": "",
        "video_url": "",
        "scripture": "",
        "summary": "",
        "body": "",
    },
]

sermon_template = env.get_template("base-sermon.html")

for sermon in SERMONS:
    html = sermon_template.render(sermon=sermon, related_sermons=SERMONS)

    output_file = output_dir / f"{sermon['slug']}.html"
    output_file.write_text(html, encoding="utf-8")
    print(f"Built {output_file}")
