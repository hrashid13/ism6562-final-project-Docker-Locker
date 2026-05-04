from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.option("header", True).csv(
    "file:///opt/airflow/data/agriflow-raw/crop-yields.csv.gz"
)

df.write.mode("overwrite").parquet(
    "hdfs://namenode:9000/agriflow/landing/crop"
)