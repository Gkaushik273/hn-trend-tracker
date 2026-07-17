import csv
import os
from datetime import datetime, timezone

def save_snapshot(stories, filepath="data/hn_snapshots.csv"):
    file_exists = os.path.isfile(filepath)
    scraped_at = datetime.now(timezone.utc).isoformat()

    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["story_id", "title", "link", "points", "comments", "scraped_at"])
        if not file_exists:
            writer.writeheader()

        for story in stories:
            row = story.copy()
            row["scraped_at"] = scraped_at
            writer.writerow(row)

    print(f"Saved {len(stories)} stories to {filepath} at {scraped_at}")