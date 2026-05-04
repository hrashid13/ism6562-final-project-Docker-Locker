from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.getOrCreate()

df = spark.read.parquet(
    "hdfs://namenode:9000/agriflow/landing/crop"
)

df = df.withColumn(
    "yield_double",
    F.col("yield_bushels_per_acre") * 2
)

df.write.mode("overwrite").parquet(
    "hdfs://namenode:9000/agriflow/curated/crop"
)

print("TRANSFORM COMPLETE")