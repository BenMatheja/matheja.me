---
layout: post
title: Getting Started with Minikube on WSL2
date: 2020-03-22 09:46 +0100
---
I wanted to get started with Kubernets and the underlying concepts on a free sunday morning.
This was my starting point
* Windows 10 with WSL 2 enabled
* Docker Desktop installed on Windows and exposed via 2375 without TSL

I tried to apply the guide from https://medium.com/@joaoh82/setting-up-kubernetes-on-wsl-to-work-with-minikube-on-windows-10-90dac3c72fa1

<!--more-->
At that point, i created the minikube alias for using the windows installation and was able to run minikube(.exe) start
```
ben@ben-desktop  ~  which minikube
/home/ben/minikube/minikube
 ben@ben-desktop  ~  minikube start
😄  minikube v1.8.2 on Microsoft Windows 10 Pro N 10.0.19041 Build 19041
✨  Automatically selected the docker driver
💾  Downloading preloaded images tarball for k8s v1.17.3 ...
    > preloaded-images-k8s-v1-v1.17.3-docker-overlay2.tar.lz4: 499.26 MiB / 499
🔥  Creating Kubernetes in docker container with (CPUs=2) (2 available), Memory=6100MB (7964MB available) ...
🐳  Preparing Kubernetes v1.17.3 on Docker 19.03.2 ...
    ▪ kubeadm.pod-network-cidr=10.244.0.0/16
🚀  Launching Kubernetes ... 
🌟  Enabling addons: default-storageclass, storage-provisioner
⌛  Waiting for cluster to come online ...
🏄  Done! kubectl is now configured to use "minikube"
```

Run on from my WSL Ubuntu Distribution fails. The Kubernetes Cluster cannot be reached.
```
 minikube kubectl get all
    > kubectl.exe.sha256: 65 B / 65 B [----------------------] 100.00% ? p/s 0s
    > kubectl.exe: 41.95 MiB / 41.95 MiB [------------] 100.00% 5.48 MiB p/s 8s
Unable to connect to the server: dial tcp 127.0.0.1:32768: connectex: No connection could be made because the target machine actively refused it.
```
Confirmed that indeed the cluster seemed to be faulty by running on Windows via Terminal
```
PS C:\Users\ben> kubectl get all
Unable to connect to the server: dial tcp 127.0.0.1:32768: connectex: No connection could be made because the target mac
hine actively refused it.
PS C:\Users\ben>
```
Recreate minikube cluster with minikube delete and minikube start from Ubuntu distribution
```
 ben@ben-desktop  ~  minikube start 
😄  minikube v1.8.2 on Microsoft Windows 10 Pro N 10.0.19041 Build 19041
✨  Automatically selected the docker driver
🔥  Creating Kubernetes in docker container with (CPUs=2) (4 available), Memory=6100MB (9968MB available) ...
🐳  Preparing Kubernetes v1.17.3 on Docker 19.03.2 ...
    ▪ kubeadm.pod-network-cidr=10.244.0.0/16
🚀  Launching Kubernetes ... 
🌟  Enabling addons: default-storageclass, storage-provisioner
⌛  Waiting for cluster to come online ...
🏄  Done! kubectl is now configured to use "minikube"
 ben@ben-desktop  ~  minikube kubectl get all
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   22s
```
Problem: kubectl from Ubuntu Distribution is not able to access minikube deployment.
Connection to localhost fails (127.0.0.1:32768)

Tried to inject kubectl configuration as in
```
pavel@MSI:~$ kubectl --kubeconfig /mnt/c/Users/Pavel/.kube/config cluster-info
```
Not working
```
✘ ben@ben-desktop  ~  minikube kubectl cluster-info
Kubernetes master is running at https://127.0.0.1:32771
KubeDNS is running at https://127.0.0.1:32771/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
 ben@ben-desktop  ~  kubectl cluster-info

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
The connection to the server 127.0.0.1:32771 was refused - did you specify the right host or port?
```
### Things done changed
Apparently since converting to my Ubuntu Distrubition to WSL 2 things done changed.
https://github.com/microsoft/WSL/issues/4321

Don't believe it and keep researching.
Deleted all previous Docker installations on Ubuntu WSL Distribution.

Did run the following steps with good output
https://docs.docker.com/docker-for-windows/wsl-tech-preview/

```
PS C:\Users\ben> wsl -l -v
  NAME                   STATE           VERSION
* Ubuntu                 Running         2
  docker-desktop-data    Running         2
  docker-desktop         Running         2
```
Reinstalled sudo apt-get install docker-ce-cli.
Docker cannot connect to /var/run/docker.sock. How is this shit supposed to work?
How can the Ubuntu distribution "just access" the same docker engine as the one on powershell without configuration?
Looked on https://www.hanselman.com/blog/DockerDesktopForWSL2IntegratesWindows10AndLinuxEvenCloser.aspx.
Should all work out of the box just fine.

Doubt it, still try if if a reinstall of docker desktop works
https://github.com/docker/for-win/issues/5268

Enabled the 'Virtual Machine Platform' optional component and make sure WSL is enabled before.
https://docs.microsoft.com/en-us/windows/wsl/wsl2-install

Did a reboot - ERMAHGERD IT WERKS

Ubuntu WSL2 Distribution
```
ben@ben-desktop  docker images
REPOSITORY                                          TAG                 IMAGE ID            CREATED             SIZE
docker.elastic.co/logstash/logstash-oss             7.6.0               50251e88900f        6 weeks ago         804MB
ea_logstash                                         latest              50251e88900f        6 weeks ago         804MB
ea_kibana                                           latest              3ad6636ee22e        6 weeks ago         646MB
docker.elastic.co/kibana/kibana-oss                 7.6.0               3ad6636ee22e        6 weeks ago         646MB
ea_elasticsearch                                    latest              1d8bbe9f233d        6 weeks ago         690MB
docker.elastic.co/elasticsearch/elasticsearch-oss   7.6.0               1d8bbe9f233d        6 weeks ago         690MB
hello-world                                         latest              fce289e99eb9        14 months ago       1.84kB
```
Windows Terminal
```
PS C:\Users\ben> docker images
REPOSITORY                                          TAG                 IMAGE ID            CREATED             SIZE
docker.elastic.co/logstash/logstash-oss             7.6.0               50251e88900f        6 weeks ago         804MB
ea_logstash                                         latest              50251e88900f        6 weeks ago         804MB
ea_kibana                                           latest              3ad6636ee22e        6 weeks ago         646MB
docker.elastic.co/kibana/kibana-oss                 7.6.0               3ad6636ee22e        6 weeks ago         646MB
docker.elastic.co/elasticsearch/elasticsearch-oss   7.6.0               1d8bbe9f233d        6 weeks ago         690MB
ea_elasticsearch                                    latest              1d8bbe9f233d        6 weeks ago         690MB
hello-world                                         latest              fce289e99eb9        14 months ago       1.84kB
PS C:\Users\ben>
```

