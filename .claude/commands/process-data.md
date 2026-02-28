# /process-data

Transform raw data into web-ready JSON files.

## Usage
```
/process-data [dataset-name]
```

## Datasets
- `chokepoints` — Extract choke point coordinates from replication data
- `conflicts` — Parse UCDP GED conflict events with coordinates
- `trade` — World Bank trade openness time series
- `marginal-effects` — Compute ME curve from Table 2 coefficients
- `regional` — Subset conflict + proximity data for zoom panels
- `all` — Run all of the above in sequence

## Process
1. Read `.claude/agents/data-engineer.md` for conventions
2. Create or update the corresponding notebook in `code_build/`
3. Execute the notebook
4. Validate output: check file size, schema, null values
5. Save to `data/[name].json`
6. Update `.planning/state.md`

## Validation Rules
- All JSON files must be valid (parseable)
- Coordinates: lat ∈ [-90, 90], lng ∈ [-180, 180]
- No null/NaN values in coordinate fields
- File sizes within targets (see data-engineer agent)
- Conflict events: must have year, lat, lng, type, deaths fields
