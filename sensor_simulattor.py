from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Replace with your Kafka server address
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    acks='all'  # Wait for acknowledgment from all brokers
)

def generate_sensor_data():
    for _ in range(5):  # Loop will run 5 times
        sensor_data = {
            "temperature": round(random.uniform(20.0, 40.0), 2),
            "humidity": round(random.uniform(30.0, 70.0), 2),
            "pressure": round(random.uniform(900.0, 1100.0), 2),
            "sensorID": "Sensor-001"
        }
        print(f"Sending Data: {sensor_data}")
        future = producer.send('topic-exemple-1', sensor_data)
        try:
            record_metadata = future.get(timeout=10)
            print(f"Message delivered to {record_metadata.topic} "
                  f"partition {record_metadata.partition} "
                  f"offset {record_metadata.offset}")
        except Exception as e:
            print(f"Failed to deliver message: {e}")
        time.sleep(2)  # Wait for 2 seconds before sending the next message
    
    producer.flush()
    producer.close()
    print("Data generation completed.")

generate_sensor_data()
