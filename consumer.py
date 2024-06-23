from kafka import KafkaConsumer
import json

# Create a Kafka consumer instance
consumer = KafkaConsumer(
    'mytopic',
    bootstrap_servers=['localhost:29092', 'localhost:39092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='mygroup',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Poll for new messages from Kafka and print them
for message in consumer:
    print(f"Received message: key={message.key} value={message.value}")

consumer.close()
