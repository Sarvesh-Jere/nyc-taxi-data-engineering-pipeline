from kafka import KafkaProducer
import json
import time

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Hardcoded ride records
rides = [
    {"LocationID": 1, "Borough": "EWR", "Zone": "Newark Airport"},
    {"LocationID": 2, "Borough": "Queens", "Zone": "Jamaica Bay"},
    {"LocationID": 3, "Borough": "Bronx", "Zone": "Allerton/Pelham Gardens"},
    {"LocationID": 4, "Borough": "Manhattan", "Zone": "Alphabet City"},
    {"LocationID": 5, "Borough": "Staten Island", "Zone": "Arden Heights"},
    {"LocationID": 6, "Borough": "Brooklyn", "Zone": "Arlington"},
    {"LocationID": 7, "Borough": "Staten Island", "Zone": "Arrochar/Fort Wadsworth"},
    {"LocationID": 8, "Borough": "Queens", "Zone": "Astoria"},
    {"LocationID": 9, "Borough": "Queens", "Zone": "Astoria Park"},
    {"LocationID": 10, "Borough": "Queens", "Zone": "Auburndale"},
    {"LocationID": 11, "Borough": "Queens", "Zone": "Baisley Park"},
    {"LocationID": 12, "Borough": "Brooklyn", "Zone": "Bath Beach"},
    {"LocationID": 13, "Borough": "Brooklyn", "Zone": "Battery Park"},
    {"LocationID": 14, "Borough": "Manhattan", "Zone": "Battery Park City"},
    {"LocationID": 15, "Borough": "Manhattan", "Zone": "Bay Ridge"},
    {"LocationID": 16, "Borough": "Brooklyn", "Zone": "Bedford"},
    {"LocationID": 17, "Borough": "Bronx", "Zone": "Bedford Park"},
    {"LocationID": 18, "Borough": "Brooklyn", "Zone": "Bensonhurst East"},
    {"LocationID": 19, "Borough": "Brooklyn", "Zone": "Bensonhurst West"},
    {"LocationID": 20, "Borough": "Brooklyn", "Zone": "Bloomfield"},
    {"LocationID": 21, "Borough": "Brooklyn", "Zone": "Boerum Hill"},
    {"LocationID": 22, "Borough": "Queens", "Zone": "Briarwood/Jamaica Hills"},
    {"LocationID": 23, "Borough": "Bronx", "Zone": "Bronx Park"},
    {"LocationID": 24, "Borough": "Bronx", "Zone": "Bronxdale"},
    {"LocationID": 25, "Borough": "Brooklyn", "Zone": "Brooklyn Heights"},
    {"LocationID": 26, "Borough": "Brooklyn", "Zone": "Brooklyn Navy Yard"},
    {"LocationID": 27, "Borough": "Brooklyn", "Zone": "Brownsville"},
    {"LocationID": 28, "Borough": "Brooklyn", "Zone": "Bushwick North"},
    {"LocationID": 29, "Borough": "Brooklyn", "Zone": "Bushwick South"},
    {"LocationID": 30, "Borough": "Manhattan", "Zone": "Carnegie Hill"},
    {"LocationID": 31, "Borough": "Manhattan", "Zone": "Central Harlem"},
    {"LocationID": 32, "Borough": "Manhattan", "Zone": "Central Park"},
    {"LocationID": 33, "Borough": "Manhattan", "Zone": "Chinatown"},
    {"LocationID": 34, "Borough": "Bronx", "Zone": "City Island"},
    {"LocationID": 35, "Borough": "Bronx", "Zone": "Claremont/Bathgate"},
    {"LocationID": 36, "Borough": "Bronx", "Zone": "Clinton East"},
    {"LocationID": 37, "Borough": "Bronx", "Zone": "Clinton Hill"},
    {"LocationID": 38, "Borough": "Manhattan", "Zone": "Clinton West"},
    {"LocationID": 39, "Borough": "Brooklyn", "Zone": "Cobble Hill"},
    {"LocationID": 40, "Borough": "Brooklyn", "Zone": "Coney Island"},
]

# Send each record to Kafka topic
for ride in rides:
    producer.send('rides', value=ride)
    print(f"Sent: {ride}")
    time.sleep(1)

producer.flush()
