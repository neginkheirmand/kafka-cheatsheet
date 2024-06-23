from kafka import KafkaProducer
import json

# Create a Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092', 'localhost:39092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Produce some messages
for i in range(10):
    message = {'key': str(i), 'value': 'my_message_{}'.format(i)}
    producer.send('mytopic', value=message)
    producer.flush()

print("Messages sent!")
