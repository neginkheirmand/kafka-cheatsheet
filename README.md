# Description
This repository contains a simple Apache Kafka project demonstrating the setup of a Kafka cluster using Docker Compose, along with Python scripts for a Kafka producer and consumer.

## Contents
- docker-compose.yml: Docker Compose configuration to set up a Kafka cluster with multiple brokers and ZooKeeper instances.
- producer.py: A Python script implementing a Kafka producer that sends messages to a specified Kafka topic.
- consumer.py: A Python script implementing a Kafka consumer that reads messages from a specified Kafka topic.
## Features
- Kafka Cluster Setup: Easily spin up a Kafka cluster using Docker Compose.
- Python Producer: Script to produce messages to Kafka topics.
- Python Consumer: Script to consume messages from Kafka topics.
## How to Use
#### 1- Start the Kafka Cluster:

```
docker-compose up -d
```
#### 1.5- create a topic with a preferred number of partitions:
```
docker exec -it <kafka_container_id> bash
kafka-topics --create --topic mytopic --partitions <n> --replication-factor 2 --bootstrap-server localhost:9092
```
<n> is the number of partitions you want to be created for the topic "mytopic".
<kafka_container_id> is the container_id of any of the 2 brokers. You can get this value by using the command:
```
docker ps -a
```
This step can be skipped since the Kafka Python library already creates a topic of the mentioned name with 1 partition by default when such a topic doesn't exist, still, if you want a specific number of partitions, you can use the previous command.

#### 2- Run the Producer:

```
python producer.py
```
Run the Consumer:
```
python consumer.py
```

### Prerequisites:
- Docker and Docker Compose installed.
- Python and the kafka library installed.
