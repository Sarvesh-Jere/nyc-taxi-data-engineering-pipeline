from kafka import KafkaConsumer
import json

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'rides',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='ride-consumers',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started...\n")

# Consume messages
for message in consumer:
    print("Received:", message.value)
