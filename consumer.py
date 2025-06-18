from kafka import KafkaConsumer
import psycopg2
import json

# Connect to Kafka
consumer = KafkaConsumer(
    'taxi_zones',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer started and listening to 'taxi_zones'...")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="nyc_taxi",
    user="postgres",
    password="yourpassword",  # ✅ Matches docker-compose.yml
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS taxi_zones (
        LocationID INT PRIMARY KEY,
        Borough TEXT,
        Zone TEXT
    )
''')
conn.commit()

# Consume messages
for message in consumer:
    data = message.value
    print("Inserting:", data)

    cur.execute('''
        INSERT INTO taxi_zones (LocationID, Borough, Zone)
        VALUES (%s, %s, %s)
        ON CONFLICT (LocationID) DO NOTHING
    ''', (data['LocationID'], data['Borough'], data['Zone']))

    conn.commit()
