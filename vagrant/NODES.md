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

