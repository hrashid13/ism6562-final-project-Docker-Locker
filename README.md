# AgriFlow Farming — Big Data Pipeline
**ISM 6562: Big Data for Business Applications | Team: Docker Locker**

## Team Members
- Freeman Ulrich Talla Wouoto (FTalla18)
- Gustavo Wengerkiewicz Storck
- Hesham Rashid (hrashid13)
- Savannah Day
- Zachary Zambrana

## Project Scenario
**AgriFlow Farming** is a precision-agriculture company managing operations
across thousands of acres on multiple farms. The company needs a unified big
data pipeline to answer two core questions:

1. **Crop yield prediction** — Which combination of soil conditions, weather
   patterns, and irrigation schedules produces the highest yield per acre?
2. **Irrigation optimization** — Where and when is water being wasted?

We act as data engineers designing and building a complete four-layer pipeline:
Store → Transform → Stream → Orchestrate.

## Architecture Overview

```
Raw Sources (CSV.gz / JSON.gz)
        │
        ▼
┌─────────────────────────────────────┐
│  HDFS Data Lake  (Stage 1)          │
│  /agriflow/landing/   ← raw files   │
│  /agriflow/curated/   ← Parquet     │
│  /agriflow/analytics/ ← aggregated  │
└─────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────┐
│  Spark Batch Transforms  (Stage 2)  │
│  Clean → Join → Aggregate → Parquet │
└─────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────┐
│  Kafka + Structured Streaming (S3)  │
│  Real-time sensor alerts            │
└─────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────┐
│  Airflow Orchestration  (Stage 4)   │
│  Scheduled DAGs + quality gates     │
└─────────────────────────────────────┘
```

See `report/architecture-diagram.png` for the full diagram.

## Repository Structure

```
ism6562-final-project-Docker-Locker/
├── README.md                          # this file
├── docker-compose.yml                 # full stack: HDFS + Spark + Kafka + Airflow
├── docker/
│   └── Dockerfile.spark               # uid-aligned Spark image (jovyan user)
├── data/
│   └── README.md                      # how to download AgriFlow data
├── notebooks/
│   ├── 01-data-lake-setup.ipynb       # Stage 1: HDFS data lake
│   ├── 02-spark-transforms.ipynb      # Stage 2: PySpark batch pipeline
│   ├── 03-streaming-pipeline.ipynb    # Stage 3: Kafka + Structured Streaming
│   └── 04-exploration.ipynb           # Ad-hoc analysis and visualizations
├── dags/
│   ├── batch_pipeline.py              # Stage 4: batch orchestration DAG
│   └── streaming_monitor.py           # Stage 4: streaming health DAG
├── producers/
│   └── event_producer.py              # Stage 3: Kafka sensor event producer
├── report/
│   ├── final-report.pdf
│   └── architecture-diagram.png
├── presentation/
│   └── slides.pdf
└── .gitignore
```

## Quick Start

### Prerequisites
- Docker Desktop (Mac) with at least 8 GB memory allocated
- ~6 GB free disk space for Docker volumes

### 1. Start the stack

```bash
git clone https://github.com/hrashid13/ism6562-final-project-Docker-Locker.git
cd ism6562-final-project-Docker-Locker
docker compose up -d
```

On first run, Docker builds the custom Spark image (`ism6562/spark-jovyan:3.5.0`).
This takes ~2 minutes. Subsequent starts are fast.

### 2. Wait for services to be healthy

```bash
docker compose ps
```

All services should show `Up (healthy)` within ~90 seconds.

### 3. Open the interfaces

| Service | URL |
|---------|-----|
| Jupyter (notebooks) | http://localhost:8888?token=agriflow |
| HDFS NameNode UI | http://localhost:9870 |
| Spark Master UI | http://localhost:8080 |
| DataNode 1 UI | http://localhost:9864 |
| DataNode 2 UI | http://localhost:9865 |

### 4. Download the AgriFlow data

See `data/README.md` for data download instructions.

### 5. Run Stage 1

In Jupyter, open `notebooks/01-data-lake-setup.ipynb` and run all cells.

### Lightweight mode (8 GB machines)

If you have ≤ 8 GB RAM, stop the second worker and reduce Spark memory:

```bash
docker compose stop agriflow-spark-worker-1
# Edit docker-compose.yml: change SPARK_WORKER_MEMORY to 1g
docker compose up -d agriflow-spark-worker-1
```

### Teardown

```bash
docker compose down        # stop and remove containers
docker compose down -v     # also delete volumes (wipes HDFS data)
```

## Data Sources

All datasets are provided by the course. See `data/README.md`.

| Source | Format | Description |
|--------|--------|-------------|
| farm_sensors | CSV.gz | IoT soil/temperature/humidity readings |
| crop_records | CSV.gz | Planting dates, crop types, harvest data |
| weather_data | CSV.gz | Daily weather by farm location |
| irrigation_logs | CSV.gz | Irrigation events and water volumes |
| soil_samples | CSV.gz | Soil composition lab results |

## Key Findings

*(To be completed at project conclusion)*

## Contributors

See GitHub commit history and pull requests for contribution breakdown.
