from scraper.fetch import get_front_page_html

html = get_front_page_html()
print(html[:300])
print(f"\nTotal length: {len(html)} characters")

from scraper.fetch import get_front_page_html
from scraper.parse import parse_front_page

html = get_front_page_html()
stories = parse_front_page(html)

print(f"Found {len(stories)} stories\n")
for s in stories[:5]:
    print(s["title"], "->", s["link"])

for s in stories[:5]:
    print(s["title"], "| points:", s["points"], "| comments:", s["comments"])

#///////////////#

from scraper.fetch import get_front_page_html
from scraper.parse import parse_front_page
from scraper.storage import save_snapshot

html = get_front_page_html()
stories = parse_front_page(html)
save_snapshot(stories)