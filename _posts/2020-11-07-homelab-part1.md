---
layout: post
title: "Homelab - Part 1: Overview"
date: 2020-11-07 09:31 +0100
tags: development traefik container docker unix homelab route53 letsencrypt
---
Due to Covid-19 I took on the task to build something new and exciting.
It was time to rebuild and extend services i'm hosting in my local network.
As a quick premise: Everything i'm running locally is only exposed to clients within the same network.
<!--more-->

## Status Quo

Having the need to run at least the Unifi-Controller within my network to control my Unifi devices I used an old Raspberry Pi 2 before.
The RPI 2 used my Synology NAS as NFS as I was aware of file system issues using only the internal SD cards.
Still the setup was painfully slow and not extendable. 

## Overview

With the use of Containers and Orchestration Tools such as `docker-compose` you can bring up entire stacks within seconds and manage them in a painless way.
I procured a used [Fujitsu TX-120 S3](https://sp.ts.fujitsu.com/dmsp/Publications/public/ds-py-tx120-s3.pdf) with a single Xeon E3-1220 3,1GHz 8GB Ram and 300GB SAS Drives for below 200€.
Then I installed Ubuntu 18.04 on it to use it as my primary docker-compose host.

Sidenote: The TX-120 is placed in the hall of our flat and I'm a bit annoyed by the continous noisy write on the Disks.
So i'll opt to switch the SAS Drives towards 2,5" SSDs in the Future.
But still i'm really amazed by the size of the case. You'll find a spot for a server that big. And as a bonus tt features 2 usable Network Interfaces out of the box.

Here is an overview of the current setup.

```asci
                          +--------------------------------------+
                          |                       TX120 S3 (io)  |
                          |                       docker-compose |
                          |                                      |
+-----------+             | +-----------+        +-------------+ |
|           |             | |           |        |             | |
| Quaysi.de +--------------->  Traefik  +-------->  Services   | |
|           |             | |           |        |             | |
+-----------+             | +-----------+        +-------------+ |
                          |                                      |
                          +--------------------------------------+

```

Everything is accessible and exposed via HTTPS below the quaysi.de domain.
Each services has its own subdomain e.g. unifi.quaysi.de.

### Traefik, Domain and Certificates

[Traefik](https://traefik.io/) is configured as the central edge router handling incoming requests and forwarding them to the services.
If you ever set up local services I assume you encountered the issues regarding non-trusted certificates.
With the help of [Amazon Route 53](https://aws.amazon.com/route53/), [Traefik](https://traefik.io/) and the LetsEncrypt Resolver its possible to bypass that.

* Set public Records in a Hosted Zone within Route 53 for your internal services e.g. quaysi.de points to 192.168.1.9, 192.168.1.10 and 192.168.1.11
* Configure Traefik to use the [DNS-Challenge](https://doc.traefik.io/traefik/user-guides/docker-compose/acme-dns/) and provision AWS Credentials

The effect is: all your internal services receive a trusted LetsEncrypt certificate and you can just work around those annoying "untrusted connection" issues, as everything is provisioned.

This was the first part of the series about my homelab. As always love to hear your feedback about.
