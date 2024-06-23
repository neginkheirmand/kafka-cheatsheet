## Basic Kafka Commands
### Create a Topic:

```
kafka-topics --create --topic <topic_name> --partitions <num_partitions> --replication-factor <replication_factor> --bootstrap-server <broker_list>
```
Example:
```
kafka-topics --create --topic test-topic --partitions 3 --replication-factor 2 --bootstrap-server localhost:9092
```
--replication-factor indicates that for each of the partitions that belong to the topic "test-topic" (ranging from 0 to 2) we  have 2 replicas. 

![img1](https://github.com/neginkheirmand/kafka-getting-started/blob/master/images/img1.png?raw=true)


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

### Delete a Topic:

```
kafka-topics --delete --topic <topic_name> --bootstrap-server <broker_list>
```

Example:

```
kafka-topics --delete --topic test-topic --bootstrap-server localhost:9092
```

## Kafka Producer and Consumer Commands
### Produce Messages to a Topic:
```
kafka-console-producer --topic <topic_name> --bootstrap-server <broker_list>
```
Example:
```
kafka-console-producer --topic testTopic --bootstrap-server localhost:9092
```
After running this command, type your messages and press Enter to send each message:


![img2](https://github.com/neginkheirmand/kafka-getting-started/blob/master/images/img2.png?raw=true)

### Consume Messages from a Topic:
```
kafka-console-consumer --topic <topic_name> --bootstrap-server <broker_list> --from-beginning
```
Example:
```
kafka-console-consumer --topic testTopic --bootstrap-server localhost:9092 --from-beginning
```
![img3](https://github.com/neginkheirmand/kafka-getting-started/blob/master/images/img3.gif?raw=true)

## Kafka Consumer Group Commands

### List Consumer Groups:
```
kafka-consumer-groups --list --bootstrap-server <broker_list>
```
Example:
```
kafka-consumer-groups --list --bootstrap-server localhost:9092
```

### Describe a Consumer Group:
```
kafka-consumer-groups --describe --group <group_id> --bootstrap-server <broker_list>
```
Example:
```
kafka-consumer-groups --describe --group mygroup --bootstrap-server localhost:9092
```
Reset Offsets for a Consumer Group:

```
kafka-consumer-groups --reset-offsets --group <group_id> --topic <topic_name> --to-earliest --bootstrap-server <broker_list>
```
Example:
```
kafka-consumer-groups --reset-offsets --group mygroup --topic mytopic --to-earliest --bootstrap-server localhost:9092 --execute
```
## Kafka Broker and Cluster Commands
### Check Cluster Metadata:

This next command is used for Cluster Diagnostics, Upgrade Planning and Monitoring purposes. 
##### 1. Cluster Diagnostics:
- To verify the versions of Kafka brokers running in the cluster.
- To check supported APIs and versions, which can be crucial when troubleshooting compatibility issues between clients and brokers.
##### 2. Upgrade Planning:
- Before upgrading Kafka brokers, you can use this command to understand the current broker versions and ensure that all brokers in the cluster are compatible with each other and with the client applications.
##### 3. Monitoring:
- To ensure that all brokers are up and running as expected and to get a quick overview of the broker versions and their configurations.
```
kafka-broker-api-versions --bootstrap-server <broker_list>
```
Example:

```
kafka-broker-api-versions --bootstrap-server localhost:9092
```
### Check the Log Segments:
```
kafka-run-class kafka.tools.DumpLogSegments --files <log_segment_file>
```
Example:
```
kafka-run-class kafka.tools.DumpLogSegments --files /path/to/kafka/logs/test-topic-0/00000000000000000000.log
```
### Get Broker Configs:
```
kafka-configs --bootstrap-server <broker_list> --entity-type brokers --entity-name <broker_id> --describe
```
Example:
```
kafka-configs --bootstrap-server localhost:9092 --entity-type brokers --entity-name 1 --describe
```