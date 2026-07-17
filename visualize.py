import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/hn_snapshots.csv", parse_dates=["scraped_at"])

# Clean, same as analyze.py
df = df.dropna(subset=["title", "story_id"])
df["points"] = df["points"].fillna(0).astype(int)
df["comments"] = df["comments"].fillna(0).astype(int)

latest_time = df["scraped_at"].max()
latest = df[df["scraped_at"] == latest_time].sort_values("points", ascending=False).head(10)

# Chart 1: Top 10 stories by points (horizontal bar — easier to read long titles)
plt.figure(figsize=(10, 6))
plt.barh(latest["title"].str.slice(0, 40), latest["points"], color="steelblue")
plt.xlabel("Points")
plt.title("Top 10 Hacker News Stories (Latest Snapshot)")
plt.gca().invert_yaxis()  # highest points at top
plt.tight_layout()
plt.savefig("data/top10_points.png")
plt.show()