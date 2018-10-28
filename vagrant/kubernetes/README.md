# Goal

To set up kubernetes sandbox using 3 centos virtual machines managed by vagrant

## Environment

192.168.2.140 kube0 # master
192.168.2.141 kube1 # node
192.168.2.142 kube2 # node

`
vagrant up
vagrant ssh kube0
vagrant ssh kube1
vagrant ssh kube2

su -
`

## Install Kubernetes

### /etc/hosts

Comment out the fire line and append kube0, kube1, kube3.

`
#127.0.0.1	kube0	kube0
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.2.140 kube0
192.168.2.141 kube1
192.168.2.142 kube2
`

### Disable SELinux and swap

`
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
`

`
swapoff -a
`

Edit `etc/fstab` and comment out:

`
#/dev/mapper/VolGroup00-LogVol01 swap                    swap    defaults        0 0
`

### Enable br_netfilter

`
modprobe br_netfilter
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
`

### Install Docker

`
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce
`

### Install Kubernetes

Edit `/etc/yum.repos.d/kubernetes.repo` and add:

`
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
        https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
`

`
yum install -y kubelet kubeadm kubectl
`

### Cgroup

`
docker info | grep -i cgroup
sed -i 's/cgroup-driver=systemd/cgroup-driver=cgroupfs/g' /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
`

`
systemctl restart docker  && systemctl enable docker  && systemctl  status docker
systemctl restart kubelet  && systemctl enable kubelet  && systemctl  status kubelet
`

### On master initialize the cluster

`
kubeadm init --apiserver-advertise-address=192.168.2.140 --pod-network-cidr=192.168.2.0/16
`

Deploy the network:

`
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
`

To start using your cluster, you need to run the following as a regular user:

`
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
`

### On node join the cluster

`
kubeadm join 192.168.2.140:6443 --token rhig2q.bighms65p2cvgx8m --discovery-token-ca-cert-hash sha256:6c91ee2ff012dec6e37bdb976296ee4d9e1116ffef626f3707efed089918708f
`

### On master get nodes

`
kubectl get nodes
`

## Resources

https://www.techrepublic.com/article/how-to-install-a-kubernetes-cluster-on-centos-7/
https://www.linuxtechi.com/install-kubernetes-1-7-centos7-rhel7/


