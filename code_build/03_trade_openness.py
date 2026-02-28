"""
03_trade_openness.py
Extracts the world trade openness time series (one value per year).
Source: globalization_data.dta, variable 'tradew'
"""
import json
import os
import pyreadstat

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'replication_data', 'globalization_data.dta')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'site', 'data', 'trade_openness.json')

print("Reading tradew and year columns...")
df, meta = pyreadstat.read_dta(
    DATA_PATH,
    usecols=['year', 'tradeworld']
)
print(f"  Loaded {len(df):,} rows")

# tradeworld is constant within year — take first value per year
df = df[df['year'] >= 1989]
trade_by_year = df.groupby('year')['tradeworld'].first().reset_index()
trade_by_year.columns = ['year', 'trade_openness']
trade_by_year['year'] = trade_by_year['year'].astype(int)
trade_by_year['trade_openness'] = trade_by_year['trade_openness'].round(4)
trade_by_year = trade_by_year.sort_values('year')

records = trade_by_year.to_dict(orient='records')

with open(OUT_PATH, 'w') as f:
    json.dump(records, f, indent=2)

print(f"Wrote {len(records)} years of trade data to {OUT_PATH}")
for r in records:
    print(f"  {r['year']}: {r['trade_openness']}")
