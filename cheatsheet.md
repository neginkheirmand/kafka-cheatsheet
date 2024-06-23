## Basic Kafka Commands
### Create a Topic:
```
kafka-topics --create --topic <topic_name> --partitions <num_partitions> --replication-factor <replication_factor> --bootstrap-server <broker_list>
```
Example:
```
kafka-topics --create --topic test-topic --partitions 3 --replication-factor 2 --bootstrap-server localhost:9092
```
### List Topics:
```
kafka-topics --list --bootstrap-server <broker_list>
```
Example:
```
kafka-topics --list --bootstrap-server localhost:9092
```
### Describe a Topic:
```
kafka-topics --describe --topic <topic_name> --bootstrap-server <broker_list>
```
Example:
```
kafka-topics --describe --topic test-topic --bootstrap-server localhost:9092
```