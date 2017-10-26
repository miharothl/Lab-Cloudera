

### Setup new virtual machine

[Get Started](https://www.vagrantup.com/intro/getting-started/)

`mkdir vagrant and cd vagrant`
`vagrant init hasicorp/precise64`
`vagrant up`

`mkdir centos and cd centos`
`vagrant init centos/7`
`vagrant up`
http://192.168.56.101:7180/
### Setup multiple machines

[Multiple vms in one file](http://www.thisprogrammingthing.com/2015/multiple-vagrant-vms-in-one-vagrantfile/)

### How to create a box

https://scotch.io/tutorials/how-to-create-a-vagrant-base-box-from-an-existing-one

sudo yum clean all

cat /dev/null > ~/.bash_history && history -c && exit

vagrant package node1 --output new.box

[on host] vagrant plugin install vagrant-vbguest

### Setup Cloudera

#### ssh

sudo vim /etc/ssh/sshd_config

PubkeyAuthentication yes
PasswordAuthentication yes

sudo service sshd restart

ssh-keygen 
cat ~/.id_rsa.pub >> ~/.ssh/authorized_keys

#### hosts

sudo vim /etc/hosts

192.168.56.101 node1
192.168.56.102 node2
192.168.56.103 node3

sudo vim /etc/selinux/config

SELINUX=disable



#### Cloudera Manager

http://192.168.56.101:7180/







curl -O https://archive.cloudera.com/cm5/installer/latest/cloudera-manager-installer.bin
chmod 777 cloudera-manager-installer.bin
./cloudera-manager-installer.bin