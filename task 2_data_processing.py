import pandas as pd
import os
file_path = "data/trends_20240115.json"
df = pd.read_json(file_path)
print(f"Loaded {len(df)} stories from {file_path}")
df = df.drop_duplicates(subset="post_id")
df = df.dropna(subset=["post_id", "title", "score"])
df["title"] = df["title"].str.strip()
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].fillna(0).astype(int)
df = df[df["score"] >= 5]
print(f"After cleaning, {len(df)} stories remain")
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)
print(f"Saved cleaned data to {output_file} with {len(df)} rows")
print("\nStories per category:")
print(df["category"].value_counts())