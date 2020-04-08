---
layout: post
title: Getting Started with Minikube on WSL2
date: 2020-04-08 09:46 +0100
---
One nice Sunday morning, I wanted to get started with Kubernetes to learn the underlying concepts. I wanted to run it on my local machine to play a bit around similar to what i'm already doing with docker-compose.
<!--more-->

This was my starting point
* Windows 10 with WSL 2 enabled
* Docker Desktop installed on Windows 10, exposed via 2375 without TSL

I tried following the guide below
[Setting up Kubernetes on WSL to work with Minikube on Windows 10](https://medium.com/@joaoh82/setting-up-kubernetes-on-wsl-to-work-with-minikube-on-windows-10-90dac3c72fa1)

At that point, i created the minikube alias for using the windows installation and was able to run minikube(.exe) start

    ben@ben-desktop  ~  which minikube
    /home/ben/minikube/minikube
    ben@ben-desktop  ~  minikube start
    😄 minikube v1.8.2 on Microsoft Windows 10 Pro N 10.0.19041 Build 19041
    ✨ Automatically selected the docker driver
    💾 Downloading preloaded images tarball for k8s v1.17.3 ...
    > preloaded-images-k8s-v1-v1.17.3-docker-overlay2.tar.lz4: 499.26 MiB / 499
    🔥 Creating Kubernetes in docker container with (CPUs=2) (2 available), Memory=6100MB (7964MB available) ...
    🐳 Preparing Kubernetes v1.17.3 on Docker 19.03.2 ...
    ▪ kubeadm.pod-network-cidr=10.244.0.0/16
    🚀 Launching Kubernetes ...
    🌟 Enabling addons: default-storageclass, storage-provisioner
    ⌛ Waiting for cluster to come online ...
    🏄 Done! kubectl is now configured to use "minikube"

### Cannot reach Kubernetes Cluster from WSL

Run from my WSL Ubuntu Distribution fails. The Kubernetes Cluster cannot be reached.

    minikube kubectl get all
    > kubectl.exe.sha256: 65 B / 65 B [----------------------] 100.00% ? p/s 0s
    > kubectl.exe: 41.95 MiB / 41.95 MiB [------------] 100.00% 5.48 MiB p/s 8s
    Unable to connect to the server: dial tcp 127.0.0.1:32768: connectex: No connection could be made because the target machine actively refused it.

Confirmed that indeed the cluster seemed to be faulty by running on Windows via Terminal

    PS C:\Users\ben> kubectl get all
    Unable to connect to the server: dial tcp 127.0.0.1:32768: connectex: No connection could be made because the target mac
    hine actively refused it.
    PS C:\Users\ben>

Recreate minikube cluster with minikube delete and minikube start from Ubuntu distribution

    ben@ben-desktop  ~  minikube start
    😄 minikube v1.8.2 on Microsoft Windows 10 Pro N 10.0.19041 Build 19041
    ✨ Automatically selected the docker driver
    🔥 Creating Kubernetes in docker container with (CPUs=2) (4 available), Memory=6100MB (9968MB available) ...
    🐳 Preparing Kubernetes v1.17.3 on Docker 19.03.2 ...
    ▪ kubeadm.pod-network-cidr=10.244.0.0/16
    🚀 Launching Kubernetes ...
    🌟 Enabling addons: default-storageclass, storage-provisioner
    ⌛ Waiting for cluster to come online ...
    🏄 Done! kubectl is now configured to use "minikube"
    ben@ben-desktop  ~  minikube kubectl get all
    NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE
    service/kubernetes ClusterIP 10.96.0.1 <none> 443/TCP 22s

Problem: kubectl from Ubuntu Distribution is not able to access minikube deployment.

Connection to localhost fails (127.0.0.1:32768)

Tried to inject kubectl configuration as in

    pavel@MSI:~$ kubectl --kubeconfig /mnt/c/Users/Pavel/.kube/config cluster-info

Not working

    ✘ ben@ben-desktop  ~  minikube kubectl cluster-info
    Kubernetes master is running at https://127.0.0.1:32771
    KubeDNS is running at https://127.0.0.1:32771/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
    To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
    ben@ben-desktop  ~  kubectl cluster-info
    To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
    The connection to the server 127.0.0.1:32771 was refused - did you specify the right host or port?

### Things done changed

Apparently since converting to my Ubuntu Distrubition to WSL 2 things done changed.

[WSL 2 docker client cannot reach Docker Desktop via tcp://0.0.0.0:2375 · Issue #4321 · microsoft/WSL](https://github.com/microsoft/WSL/issues/4321#issuecomment-573351391)

Don't believe it and keep researching. Then deleted all previous Docker installations on Ubuntu WSL Distribution. Did run the following steps with good output

[Docker Desktop WSL 2 backend](https://docs.docker.com/docker-for-windows/wsl-tech-preview/)

    PS C:\Users\ben> wsl -l -v
    NAME STATE VERSION
    * Ubuntu Running 2
    docker-desktop-data Running 2
    docker-desktop Running 2

Reinstalled  

    sudo apt-get install docker-ce-cli.

Docker cannot connect to /var/run/docker.sock. How is this shit supposed to work?

How can the Ubuntu distribution "just access" the same docker engine as the one on powershell without configuration?

Looked on 

[Docker Desktop for WSL 2 integrates Windows 10 and Linux even closer](https://www.hanselman.com/blog/DockerDesktopForWSL2IntegratesWindows10AndLinuxEvenCloser.aspx)

Should all work out of the box just fine.

Doubt it, still try if if a reinstall of docker desktop works

[[WSL2] docker CLI cannot connect to running docker engine · Issue #5268 · docker/for-win](https://github.com/docker/for-win/issues/5268)

Enabled the 'Virtual Machine Platform' optional component and make sure WSL is enabled before.

[Install WSL 2](https://docs.microsoft.com/en-us/windows/wsl/wsl2-install)

### Did a reboot - ERMAHGERD IT WERKS

*View from Ubuntu WSL2 Distribution*

    ben@ben-desktop  docker images
    REPOSITORY TAG IMAGE ID CREATED SIZE
    docker.elastic.co/logstash/logstash-oss 7.6.0 50251e88900f 6 weeks ago 804MB
    ea_logstash latest 50251e88900f 6 weeks ago 804MB
    ea_kibana latest 3ad6636ee22e 6 weeks ago 646MB
    docker.elastic.co/kibana/kibana-oss 7.6.0 3ad6636ee22e 6 weeks ago 646MB
    ea_elasticsearch latest 1d8bbe9f233d 6 weeks ago 690MB
    docker.elastic.co/elasticsearch/elasticsearch-oss 7.6.0 1d8bbe9f233d 6 weeks ago 690MB
    hello-world latest fce289e99eb9 14 months ago 1.84kB

*View from Windows Terminal*

    PS C:\Users\ben> docker images
    REPOSITORY TAG IMAGE ID CREATED SIZE
    docker.elastic.co/logstash/logstash-oss 7.6.0 50251e88900f 6 weeks ago 804MB
    ea_logstash latest 50251e88900f 6 weeks ago 804MB
    ea_kibana latest 3ad6636ee22e 6 weeks ago 646MB
    docker.elastic.co/kibana/kibana-oss 7.6.0 3ad636ee22e 6 weeks ago 646MB
    docker.elastic.co/elasticsearch/elasticsearch-oss 7.6.0 1d8bbe9f233d 6 weeks ago 690MB
    ea_elasticsearch latest 1d8bbe9f233d 6 weeks ago 690MB
    hello-world latest fce289e99eb9 14 months ago 1.84kB
    PS C:\Users\ben>

# Back to the initial plan

Do a small tutorial of kubernets 

[Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/)

    minikube start

fails

    minikube delete & minikube start

works

mother of god kubectl is also giving me the cluster-info

    ben@ben-desktop  ~  kubectl cluster-info
    Kubernetes master is running at https://127.0.0.1:32771
    KubeDNS is running at https://127.0.0.1:32771/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
    To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

Cannot access the service via IP, suspect minikube.exe installation is causing issue

    ben@ben-desktop  ~  minikube service hello-node
    |-----------|------------|-------------|-------------------------|
    | NAMESPACE | NAME | TARGET PORT | URL |
    |-----------|------------|-------------|-------------------------|
    | default | hello-node | | http://172.17.0.2:30926 |
    |-----------|------------|-------------|-------------------------|
    🎉 Opening service default/hello-node in default browser...
    "\\wsl$\Ubuntu\home\ben"
    CMD.EXE wurde mit dem oben angegebenen Pfad als aktuellem Verzeichnis gestartet.
    UNC-Pfade werden nicht unterstützt.
    Stattdessen wird das Windows-Verzeichnis als aktuelles Verzeichnis gesetzt.

Removed Minikube proxy and installed it within the WSL Distro using 

[Installation von Minikube](https://kubernetes.io/de/docs/tasks/tools/install-minikube/)

Minikube is really the only thing which really heals itself when errors occur.

    ben@ben-desktop  ~  minikube start
    😄 minikube v1.8.2 on Ubuntu 18.04
    ✨ Automatically selected the docker driver
    💾 Downloading preloaded images tarball for k8s v1.17.3 ...
    > preloaded-images-k8s-v1-v1.17.3-docker-overlay2.tar.lz4: 499.26 MiB / 499
    🔥 Creating Kubernetes in docker container with (CPUs=2) (4 available), Memory=4700MB (19124MB available) ...
    🐳 Preparing Kubernetes v1.17.3 on Docker 19.03.2 ...
    ▪ kubeadm.pod-network-cidr=10.244.0.0/16
    🚀 Launching Kubernetes ...
    💣 Error starting cluster: running cmd: /bin/bash -c "sudo env PATH=/var/lib/minikube/binaries/v1.17.3:$PATH kubeadm init phase certs all --config
    /var/tmp/minikube/kubeadm.yaml": /bin/bash -c "sudo env PATH=/var/lib/minikube/binaries/v1.17.3:$PATH kubeadm init phase certs all --config /var/tmp/minikube/kubeadm.yaml": exit status 1
    stdout:
    [certs] Using certificateDir folder "/var/lib/minikube/certs"
    [certs] Using existing ca certificate authority[certs] Using existing apiserver certificate and key on disk
    stderr:
    W0322 11:26:27.055133 1180 validation.go:28] Cannot validate kube-proxy config - no validator is available
    W0322 11:26:27.055179 1180 validation.go:28] Cannot validate kubelet config - no validator is available
    error execution phase certs/apiserver-kubelet-client: [certs] certificate apiserver-kubelet-client not signed by CA certificate ca: crypto/rsa: verification error
    To see the stack trace of this error execute with --v=5 or higher
    😿 minikube is exiting due to an error. If the above message is not useful, open an issue:
    👉 https://github.com/kubernetes/minikube/issues/new/choose
    ✘ ben@ben-desktop  ~  minikube delete
    ❗ Unable to get the status of the minikube cluster.
    🔥 Removing /home/ben/.minikube/machines/minikube ...
    💀 Removed all traces of the "minikube" cluster.
    ben@ben-desktop  ~  minikube start
    😄 minikube v1.8.2 on Ubuntu 18.04
    ✨ Automatically selected the docker driver
    🔥 Creating Kubernetes in docker container with (CPUs=2) (4 available), Memory=4700MB (19124MB available) ...
    🐳 Preparing Kubernetes v1.17.3 on Docker 19.03.2 ...
    ▪ kubeadm.pod-network-cidr=10.244.0.0/16
    🚀 Launching Kubernetes ...
    🌟 Enabling addons: default-storageclass, storage-provisioner
    ⌛ Waiting for cluster to come online ...
    🏄 Done! kubectl is now configured to use "minikube"

Trying to expose a service works but the service cannot be accessed (timeout)

    ben@ben-desktop  ~  minikube service hello-node
    |-----------|------------|-------------|-------------------------|
    | NAMESPACE | NAME | TARGET PORT | URL |
    |-----------|------------|-------------|-------------------------|
    | default | hello-node | | http://172.17.0.2:32663 |
    |-----------|------------|-------------|-------------------------|
    🎉 Opening service default/hello-node in default browser...
    💣 open url failed: http://172.17.0.2:32663: exec: "xdg-open": executable file not found in $PATH
    😿 minikube is exiting due to an error. If the above message is not useful, open an issue:
    👉 https://github.com/kubernetes/minikube/issues/new/choose
    ✘ ben@ben-desktop  ~  curl http://172.17.0.2:32663/ -v
    * Trying 172.17.0.2...
    * TCP_NODELAY set
    * connect to 172.17.0.2 port 32663 failed: Connection timed out
    * Failed to connect to 172.17.0.2 port 32663: Connection timed out
    * Closing connection 0
    curl: (7) Failed to connect to 172.17.0.2 port 32663: Connection timed out
    ✘ ben@ben-desktop  ~ 

Seemingly without minikube tunnel one cannot expose a deployment. Tunnel seems not to be build up correctly means i cannot finish the tutorial.

    Status:
    machine: minikube
    pid: 6483
    route: 10.96.0.0/12 -> 172.17.0.2
    minikube: Running
    services: []
    errors:
    minikube: no errors
    router: error adding Route: Error: Nexthop has invalid gateway.
    , 2
    loadbalancer emulator: no errors

Stopped it at this point. Even though there are some nice things to do e.g. set up deployments via kubectl and see how they are applied on our minikube cluster I cannot expose services which is a main thing of having Kubernetes running.
I'll be back :).