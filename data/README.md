# AgriFlow Data

All AgriFlow datasets are provided by the course and are **not committed to this
repository** (files are too large and contain the professor's generated data).

## Download Instructions

### Option A — Automatic (recommended)
Run the first two cells of `notebooks/01-data-lake-setup.ipynb`.
The notebook uses the GitHub API to discover available files and downloads
them automatically to `/home/jovyan/data/agriflow-raw/` inside the Jupyter container.

### Option B — Manual download
Files live in the course data repository:

```
https://github.com/prof-tcsmith/6562S26-data/tree/main/final-projects/03-agriflow-farming/
```

Download each file and place it in this `data/` directory on your host machine.
The `docker-compose.yml` mounts `./data` into both the Jupyter and Spark containers
at `/home/jovyan/data`, so files placed here are immediately accessible.

### Option C — Raw URLs (wget / curl)

```bash
BASE="https://raw.githubusercontent.com/prof-tcsmith/6562S26-data/main/final-projects/03-agriflow-farming"

mkdir -p data/agriflow-raw
cd data/agriflow-raw

# Download all files (update filenames if the repo changes)
wget "$BASE/farm_sensors.csv.gz"
wget "$BASE/crop_records.csv.gz"
wget "$BASE/weather_data.csv.gz"
wget "$BASE/irrigation_logs.csv.gz"
wget "$BASE/soil_samples.csv.gz"
```

## Expected Files

| File | Format | Approx. Size | Description |
|------|--------|-------------|-------------|
| `farm_sensors.csv.gz` | CSV (gzip) | ~30–50 MB | IoT sensor readings: soil moisture, temperature, humidity per farm/field/timestamp |
| `crop_records.csv.gz` | CSV (gzip) | ~10–20 MB | Crop planting and harvest records: crop type, field, planting date, expected/actual yield |
| `weather_data.csv.gz` | CSV (gzip) | ~10–20 MB | Daily weather observations: precipitation, temperature, evapotranspiration by location |
| `irrigation_logs.csv.gz` | CSV (gzip) | ~20–30 MB | Irrigation events: field, start/end time, volume applied, system type |
| `soil_samples.csv.gz` | CSV (gzip) | ~5–10 MB | Lab soil composition results: pH, nitrogen, phosphorus, organic matter by field/date |

*Actual filenames and sizes may differ — the notebook auto-discovers them via GitHub API.*

## Notes

- Spark reads `.gz` files natively — no need to decompress before loading
- Do **not** commit these files to Git (they are in `.gitignore`)
- If the GitHub API rate-limits you, wait 60 seconds and retry, or download manually
