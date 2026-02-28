"""
05_regional_panels.py
Creates regional subsets for Africa and Central America (reproducing Figure 2).
Regional filters from replication.do lines 83-104.
"""
import json
import os
import pyreadstat
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'replication_data', 'globalization_data.dta')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'site', 'data', 'regional_panels.json')

REGIONS = {
    "africa": {"row_min": 107, "row_max": 200, "col_min": 323, "col_max": 444},
    "central_america": {"row_min": 166, "row_max": 225, "col_min": 117, "col_max": 250},
}

print("Reading globalization_data.dta (subset of columns)...")
df, meta = pyreadstat.read_dta(
    DATA_PATH,
    usecols=['gid', 'xcoord', 'ycoord', 'col', 'row', 'year', 'conflict', 'near_dist', 'tradeworld',
             'near_dist_q1', 'near_dist_q2', 'near_dist_q3', 'near_dist_q4']
)
print(f"  Loaded {len(df):,} rows")

df = df[df['year'] >= 1989]
trade_median = df['tradeworld'].median()
print(f"  Trade median: {trade_median:.4f}")

result = {}

for region_name, bounds in REGIONS.items():
    region = df[
        (df['row'] > bounds['row_min']) & (df['row'] < bounds['row_max']) &
        (df['col'] > bounds['col_min']) & (df['col'] < bounds['col_max'])
    ]

    for label, subset in [("high", region[region['tradeworld'] >= trade_median]),
                          ("low", region[region['tradeworld'] < trade_median])]:
        agg = subset.groupby('gid').agg(
            lat=('ycoord', 'first'),
            lng=('xcoord', 'first'),
            events=('conflict', 'sum'),
            near_dist=('near_dist', 'first'),
            q1=('near_dist_q1', 'first'),
            q2=('near_dist_q2', 'first'),
            q3=('near_dist_q3', 'first'),
            q4=('near_dist_q4', 'first'),
        ).reset_index()

        agg = agg[agg['events'] > 0]

        # Assign quartile label
        agg['quartile'] = 4
        agg.loc[agg['q1'] == 1, 'quartile'] = 1
        agg.loc[agg['q2'] == 1, 'quartile'] = 2
        agg.loc[agg['q3'] == 1, 'quartile'] = 3

        agg['lat'] = agg['lat'].round(2)
        agg['lng'] = agg['lng'].round(2)
        agg['events'] = agg['events'].astype(int)

        key = f"{region_name}_{label}"
        result[key] = agg[['lat', 'lng', 'events', 'quartile']].to_dict(orient='records')
        print(f"  {key}: {len(result[key])} cells with conflict")

with open(OUT_PATH, 'w') as f:
    json.dump(result, f)

size_kb = os.path.getsize(OUT_PATH) / 1024
print(f"Wrote regional panels ({size_kb:.0f} KB) to {OUT_PATH}")
