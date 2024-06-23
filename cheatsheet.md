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


![](https://github.com/neginkheirmand/kafka-getting-started/blob/master/images/img2.png?raw=true)

### Consume Messages from a Topic:
```
kafka-console-consumer.sh --topic <topic_name> --bootstrap-server <broker_list> --from-beginning
```
Example:
```
kafka-console-consumer.sh --topic testTopic --bootstrap-server localhost:9092 --from-beginning
```
## Kafka Consumer Group Commands