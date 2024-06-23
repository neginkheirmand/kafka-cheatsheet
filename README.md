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

Run the Producer:

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
