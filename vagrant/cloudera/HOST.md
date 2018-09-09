# Introduction

Nots about how to install vagrant and virtual box on the host (MacOS, Ubuntu)
and setup base CentOS box for Cloudera.

## Update host
`
sudo apt update
sudo apt upgrade
`

## Install vagrant
`
sudo apt-get install virtualbox
sudo apt-get install virtualbox-dkms
sudo apt-get install vagrant
`

### NOTE

If Ubuntu 16.04 freezes on vagrant up, make sure you have:
* vagrant version 2.0.2
 
  Follow:
  * https://askubuntu.com/questions/994926/ubuntu-16-04-freezes-on-vagrant-up

  Download vagrant and install the package sudo dpkg -i vagrant_2.0.2_x86_64.deb

* virtual box version 5.2

  Follow: Method 1
  * https://www.askmetutorials.com/2017/12/install-oracle-virtualbox-524-on-ubuntu.html

## Get Configuration
mkdir -p ~/scm/git/hub && cd ~/scm/git/hub
git clone https://github.com/miharothl/Lab-Cloudera.git
cd Lab-Cloudera

### Basic Check

Start minimal CentOS:
`
cd vagrant/0_minimal
vagrant up
vagrant ssh
`

Check ip address, install vim and net tools
`
ip add
sudo yum install vim
sudo yum install net-tools
`

Follow:
* https://www.unixmen.com/ifconfig-command-found-centos-7-minimal-installation-quick-tip-fix/

### Setup base image

If you have the base image on the other host copy it:

host2:
`
cd ~/Lab-Cloudera/vagrant/1_base_update
scp host:~/Lab-Cloudera/vagrant/1_base_update/base.box .
vagrant box add --force base base.box
vagrant box list
`

Otherwise create it by following next steps:

Update hosts file:

NOTE!!!: hostname and entries in the hosts file should be the same otherwise
you'll get a heartbeat issue

host: `cd vagrant/1_base` and run basic check.
base: `sudo vim /etc/hosts` and add...


127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.1.130 vc0 # base
192.168.1.131 vc1 # manager
192.168.1.132 vc2 # name
192.168.1.133 vc3 # data
192.168.1.134 vc4 #
192.168.1.135 vc5 #
192.168.1.136 vc6 #
192.168.1.137 vc7 #
192.168.1.138 vc8 #
192.168.1.139 vc9 #

host: `sudo vim /etc/hosts` and add...

Configure sshd

base:
`
sudo vim /etc/ssh/sshd_config
PubkeyAuthentication yes
PasswordAuthentication yes

sudo service sshd restart
`

Create ssh keys:

base:
`
ssh-keygen
cat ~/.ssh/id_rsa.pub >>  ~/.ssh/authorized_keys
`

host:
`
ssh-keygen
scp .ssh/id_rsa.pub   vagrant@vc0:~/
`
base:
`
cat ~/id_rsa.pub >>  ~/.ssh/authorized_keys
`

base:
`
sudo vim /etc/selinux/config
`
SELINUX=disabled

#### Create box

Read:
* https://scotch.io/tutorials/how-to-create-a-vagrant-base-box-from-an-existing-one

base:
`
sudo yum clean all
sudo rm -rf /var/cache/yum

cat /dev/null > ~/.bash_history && history -c && exit
`

host:
`
vagrant package vc0 --output base.box
vagrant box add --force base base.box
vagrant box list
`

host:
`
vagrant plugin install vagrant-vbguest
`
