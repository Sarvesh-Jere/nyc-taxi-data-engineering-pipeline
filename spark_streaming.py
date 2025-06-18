from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, IntegerType, StringType

# Define the schema for the incoming Kafka messages
schema = StructType() \
    .add("LocationID", IntegerType()) \
    .add("Borough", StringType()) \
    .add("Zone", StringType()) \
    .add("service_zone", StringType())

# Create Spark session with Kafka support
spark = SparkSession.builder \
    .appName("NYC Taxi Zones Stream") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1,org.postgresql:postgresql:42.5.4") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Read stream from Kafka topic
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "taxi_zones") \
    .option("startingOffsets", "earliest") \
    .load()

# Convert value from bytes to string
df_json = df_raw.selectExpr("CAST(value AS STRING)")

# Parse JSON and extract fields
df_parsed = df_json.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Write to PostgreSQL in micro-batches
df_parsed.writeStream \
    .foreachBatch(lambda batch_df, epoch_id: batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://postgres:5432/nyc_taxi") \
        .option("dbtable", "taxi_zones") \
        .option("user", "postgres") \
        .option("password", "postgres") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()) \
    .outputMode("update") \
    .start() \
    .awaitTermination()
