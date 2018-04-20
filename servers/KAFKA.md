## Configuration

https://www.cloudera.com/documentation/kafka/1-2-x/topics/kafka_install.html

Hosts -> Parcels

Kafka Parcel
1. Download
2. Distribure
3. Activate (go back to parcel view)

Home -> Action -> Add Service

### Create a topic

zookeeper is running on vc1
kafka broker is running on vc3

Create a topic:
`
kafka-topics --create --zookeeper vc1:2181 --replication-factor 1 --partitions 1 --topic test
kafka-topics --zookeeper vc1:2181 --list
`

Create console consumer and producer:
`
/usr/bin/kafka-console-producer --broker-list vc3:9092 --topic test  
/usr/bin/kafka-console-consumer --zookeeper vc1:2181 --topic test
`

