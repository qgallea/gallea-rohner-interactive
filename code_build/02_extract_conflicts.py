"""
02_extract_conflicts.py
Extracts conflict events aggregated to grid cells, split by high/low trade.
Mirrors replication.do lines 66-105 (Figure 2 data preparation).
Source: globalization_data.dta
"""
import json
import os
import pyreadstat
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'replication_data', 'globalization_data.dta')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'site', 'data', 'conflict_events.json')

print("Reading globalization_data.dta (subset of columns)...")
df, meta = pyreadstat.read_dta(
    DATA_PATH,
    usecols=['gid', 'xcoord', 'ycoord', 'year', 'conflict', 'best', 'tradeworld', 'col', 'row']
)
print(f"  Loaded {len(df):,} rows x {len(df.columns)} columns")

# Filter to sample period
df = df[df['year'] >= 1989]

# Compute median trade openness
trade_median = df['tradeworld'].median()
print(f"  Trade openness median: {trade_median:.4f}")

# Split into high/low trade
df['high_trade'] = df['tradeworld'] >= trade_median

# Aggregate by grid cell and trade period
agg = df.groupby(['gid', 'high_trade']).agg(
    lat=('ycoord', 'first'),
    lng=('xcoord', 'first'),
    events=('conflict', 'sum'),
    deaths=('best', 'sum'),
).reset_index()

# Keep only cells with at least 1 conflict event
agg = agg[agg['events'] > 0]

# Round coordinates for smaller file
agg['lat'] = agg['lat'].round(2)
agg['lng'] = agg['lng'].round(2)
agg['deaths'] = agg['deaths'].astype(int)
agg['events'] = agg['events'].astype(int)

# Convert to list of dicts
records = agg[['lat', 'lng', 'events', 'deaths', 'high_trade']].to_dict(orient='records')

with open(OUT_PATH, 'w') as f:
    json.dump(records, f)

size_kb = os.path.getsize(OUT_PATH) / 1024
print(f"Wrote {len(records)} conflict records ({size_kb:.0f} KB) to {OUT_PATH}")
