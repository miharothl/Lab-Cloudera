# 
## Basic Cloudera Installation

## Delte Nodes

host:
`
vagrant halt
rm -r .vagrant
rm -r ~/VirtualBox\ VMs/vc1
`

## Cloudera Manager

`
cd 2_nodes
vagrant up
`

vc1:
`
curl -O https://archive.cloudera.com/cm5/installer/latest/cloudera-manager-installer.bin
chmod 777 cloudera-manager-installer.bin
sudo ./cloudera-manager-installer.bin
`

Cloudera Manager
http://192.168.56.101:7180/

username/pwd: admin/admin


### Explore services

Navigate to Cloudera Manager -> Clusters -> Cluster 1; Explore services, Check
Web UI.

* HDFS http://vc1:50070/
* Hive http://vc1:10002/
* Hue http://vc1:8889/hue
* Oozie http://vc1:11000/
* Spark http://vc1:18088/
* YARN http://vc1:8088/cluster http://vc1:19888/jobhistory 
* ZooKeeper 

### Add file to hdfs

node: 
`
hdfs dfs -put some-file.txt /tmp'
hdfs dfs -ls /tmp
`

### Start spark

read:
http://community.cloudera.com/t5/Storage-Random-Access-HDFS/Where-does-the-super-user-group-need-to-be-created/td-p/57207


node: 
`
pyspark
AccessControlException: Permission denied: user=vagrant, access=WRITE, inode="/user":hdfs:supergroup:drwxr-xr-x
`

Create supergroup and add vagrant to the group:
`
sudo groupadd supergroup
sudo usermod -a -G supergroup vagrant
groups vagrant

vagrant : vagrant supergroup
`

https://community.cloudera.com/t5/Advanced-Analytics-Apache-Spark/spark-shell-stuck/m-p/57603A

https://community.cloudera.com/t5/Advanced-Analytics-Apache-Spark/Endless-INFO-Client-Application-report-for-application-xx-state/td-p/31460

https://stackoverflow.com/questions/30828879/application-report-for-application-state-accepted-never-ends-for-spark-submi

http://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-2/

yarn.scheduler.maximum-allocation-mb  1180 Mib -> 2180 Mib
yarn.nodemanager.resource.memory-mb 1180 Mib -> 2180 Mib

`
pyspark

spark-shell
`

get pi.py from 1.6 spark on on github

spark-submit --num-executors 2 --executor-cores 2 --executor-memory 500m pi.py

## Uninstall Cloudera from the node

Read: https://www.cloudera.com/documentation/enterprise/latest/topics/cm_ig_uninstall_cm.html


