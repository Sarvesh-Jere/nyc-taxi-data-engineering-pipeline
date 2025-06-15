# kafka-producer/producer.py

import csv
import time
from kafka import KafkaProducer

# Configs
KAFKA_BROKER = 'localhost:9092'
TOPIC_NAME = 'taxi_trips'
DATA_FILE = 'data/nyc_taxi_sample.csv'  # You can change this path as needed

# Kafka setup
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: str(v).encode('utf-8')
)

# Send data to Kafka
def stream_csv():
    with open(DATA_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            producer.send(TOPIC_NAME, value=row)
            print(f"Produced to {TOPIC_NAME}: {row}")
            time.sleep(0.5)  # Simulate real-time stream

    producer.flush()

if __name__ == "__main__":
    print("Starting Kafka producer...")
    stream_csv()
    print("All records sent.")
