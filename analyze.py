import pandas as pd

df = pd.read_csv("data/hn_snapshots.csv", parse_dates=["scraped_at"])

print(f"Total rows: {len(df)}")
print(f"Unique stories seen: {df['story_id'].nunique()}")
print(f"Snapshots taken: {df['scraped_at'].nunique()}\n")

# Basic cleaning
print(f"Rows before cleaning: {len(df)}")

df = df.dropna(subset=["title", "story_id"])          # drop rows missing critical fields
df["points"] = df["points"].fillna(0).astype(int)      # ensure numeric, no NaNs
df["comments"] = df["comments"].fillna(0).astype(int)
df = df.drop_duplicates(subset=["story_id", "scraped_at"])  # exact duplicate snapshot rows only

print(f"Rows after cleaning: {len(df)}")

# Latest snapshot only — current front page ranked by points
latest_time = df["scraped_at"].max()
latest = df[df["scraped_at"] == latest_time].sort_values("points", ascending=False)
print("=== Current top 5 by points ===")
print(latest[["title", "points", "comments"]].head())

# How each story's points changed across snapshots (only meaningful once you have 2+ runs)
growth = df.groupby("story_id").agg(
    title=("title", "first"),
    first_points=("points", "first"),
    latest_points=("points", "last"),
    snapshots_seen=("points", "count"),
)
growth["points_gained"] = growth["latest_points"] - growth["first_points"]
print("\n=== Stories gaining the most points between snapshots ===")
print(growth.sort_values("points_gained", ascending=False).head())