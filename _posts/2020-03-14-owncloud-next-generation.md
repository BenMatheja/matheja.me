---
layout: post
title: Owncloud Next Generation
date: 2020-03-14 13:08 +0100
---
# Why
* Filesystem Storage on VPS is expensive (netcup storage - 1,5TB 15€ per month)
* Dont feed the big monsters

# What
* Owncloud in a container
* Using Backblaze B2 as cheap object storage Backend (encrypted)

# How
* Owncloud seemingly does not offer a native Backblaze B2 Integration
* Use https://github.com/minio/minio/blob/master/docs/gateway/b2.md as a local Gateway to b2 storage
* Could possibly load-balance the container
* OC -> minio1 -> Backblaze B2
* OC -> minio2 -> Backblaze B2