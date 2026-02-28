"""
01_extract_chokepoints.py
Generates chokepoints.json from known geographic coordinates.
Source: Gallea & Rohner (2021), SKILL.md verified coordinates.
"""
import json
import os

chokepoints = [
    {"name": "Strait of Hormuz", "lat": 26.57, "lng": 56.25, "context": "Oil route, Iran tensions"},
    {"name": "Strait of Malacca", "lat": 2.50, "lng": 101.50, "context": "Asia-Europe trade, busiest strait"},
    {"name": "Suez Canal", "lat": 30.46, "lng": 32.35, "context": "Mediterranean-Red Sea link"},
    {"name": "Panama Canal", "lat": 9.08, "lng": -79.68, "context": "Atlantic-Pacific shortcut"},
    {"name": "Strait of Gibraltar", "lat": 35.97, "lng": -5.50, "context": "Mediterranean entry"},
    {"name": "Bab el-Mandeb", "lat": 12.58, "lng": 43.33, "context": "Red Sea entry, Yemen conflict"},
    {"name": "Strait of Taiwan", "lat": 24.00, "lng": 119.50, "context": "US-China flashpoint"},
    {"name": "Cape of Good Hope", "lat": -34.36, "lng": 18.47, "context": "Alternative to Suez"},
    {"name": "Strait of Dover", "lat": 51.05, "lng": 1.45, "context": "English Channel narrows"},
    {"name": "Turkish Straits", "lat": 41.12, "lng": 29.05, "context": "Bosphorus, Black Sea access"},
    {"name": "Strait of Kerch", "lat": 45.30, "lng": 36.60, "context": "Russia-Ukraine, 2018 incident"},
    {"name": "Lombok Strait", "lat": -8.47, "lng": 115.72, "context": "Alternative to Malacca"},
]

out_path = os.path.join(os.path.dirname(__file__), '..', 'site', 'data', 'chokepoints.json')
with open(out_path, 'w') as f:
    json.dump(chokepoints, f, indent=2)

print(f"Wrote {len(chokepoints)} choke points to {out_path}")
