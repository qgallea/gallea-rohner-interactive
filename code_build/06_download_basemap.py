"""
06_download_basemap.py
Downloads Natural Earth 110m TopoJSON for the D3 world map.
"""
import os
import urllib.request

URL = "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json"
out_path = os.path.join(os.path.dirname(__file__), '..', 'site', 'data', 'world-110m.json')

print(f"Downloading world basemap from {URL}...")
urllib.request.urlretrieve(URL, out_path)

size_kb = os.path.getsize(out_path) / 1024
print(f"Wrote world-110m.json ({size_kb:.0f} KB) to {out_path}")
