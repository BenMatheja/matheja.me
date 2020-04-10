---
layout: post
title: Secure your Services with Traefik and Google oAuth
date: 2020-04-10 11:19 +0200
---
Hobby projects tend to grow.

As things grew bigger, the need to have proper authentification in place constantly rises.

With the use of Containers and Orchestration Tools such as `docker-compose` you can bring up an entire ELK stack within seconds. Still the setup will feature non-protected Kibana installation. This argument holds for Grafana and other Web-applications as well. Luckily there is a solution for Traefik. I want to show some of the key parts to get it working.
<!--more-->

## Setup

The setup is quite easy. Imagine you want to have a couple of services running at your domain.

In this example it will be *farsity.de*. 

I'm using Traefik 2.2 in the examples below. Be careful if you came by tutorials written for Traefik v1. The stuff will just not work because traefik changed their internal modules (bye bye frontend, hello routers)

The layout is quite simple, below [farsity.de](http://farsity.de) we will find a

- Sample whoami service which I want to protect at https://api.farsity.de
- Authentication Container which redirects to Google for oAuth at https://auth.farsity.de

After applying the configuration, the sample whoami service should no longer be reachable without a proper authorization.

You will find the complete examples at [BenMatheja/traefik-sandbox](https://github.com/BenMatheja/traefik-sandbox)

# How does it look like from user perspective?

GET at  [https://api.farsity.de](https://api.farsity.de) will check if the user is already authenticated.

if not, the request is forwarded to our authentication proxy which builds up an redirection to receive a token. The user does not recognise anything of the internal logic. Either he will just access the Service or will see a login at Google and then access the Service.
```bash
> GET / HTTP/2
> Host: api.farsity.de
> User-Agent: curl/7.64.1
> Accept: */*
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 250)!
< HTTP/2 307
< content-type: text/html; charset=utf-8
< date: Fri, 10 Apr 2020 09:04:02 GMT
< location: https://accounts.google.com/o/oauth2/auth?client_id=dtl2sgbj48q8it.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fapi.farsity.de%2F_oauth&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&state=24490f27856b1515a121ec763550347e%3Agoogle%3Ahttps%3A%2F%2Fapi.farsity.de%2F
< set-cookie: _forward_auth_csrf=24490fe; Path=/; Domain=api.farsity.de; Expires=Fri, 10 Apr 2020 21:04:02 GMT; HttpOnly; Secure
< content-length: 450
<
<a href="https://accounts.google.com/o/oauth2/auth?client_id=dtl2sgbj48q8it.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fapi.farsity.de%2F_oauth&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&state=24490f27856b1515a121ec763550347e%3Agoogle%3Ahttps%3A%2F%2Fapi.farsity.de%2F">Temporary Redirect</a>.
```
## Register your application with Google

- Create a new Project at [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials?project=my-traefik-oauth-proxy-273717)
- Create new oAuth 2.0-Client-IDs
- Make sure to add all authorised redirect domains (in this case [https://api.farsity.de/_oauth](https://api.farsity.de/_oauth))

## Configuration of the authentication proxy

Below is the configuration for the traefik-forward-auth container.

[thomseddon/traefik-forward-auth](https://github.com/thomseddon/traefik-forward-auth)

The configuration happens within the environment. 
```yaml
traefikforward:
image: thomseddon/traefik-forward-auth
container_name: traefikforward
environment:
    # These Variables are injected via environment file
    #- PROVIDERS_GOOGLE_CLIENT_ID=${GOOGLE_CLIENT_ID}
    #- PROVIDERS_GOOGLE_CLIENT_SECRET=GOOGLE_CLIENT_SECRET
    #- SECRET=${SECRET}
    #- INSECURE_COOKIE=true # Example assumes no https, do not use in production
    #- WHITELIST=${WHITELIST}
    - DOMAIN=farsity.de
    - AUTH_HOST=auth.farsity.de
    - LOG_LEVEL=debug
env_file: 
    - ./traefik-auth.env
labels:
    - "traefik.enable=true"
    - "traefik.http.services.traefikforward.loadbalancer.server.port=4181"
    - "traefik.http.routers.traefikforward.entrypoints=websecure"
    - "traefik.http.routers.traefikforward.tls.certresolver=myresolver"
    - "traefik.http.routers.traefikforward.rule=Host(`auth.farsity.de`)"
```
Security critical values are handled in a separate .env file

To generate the secret use `openssl rand -hex 16` . It is used to sign the cookie.

    PROVIDERS_GOOGLE_CLIENT_ID=123.apps.googleusercontent.com
    PROVIDERS_GOOGLE_CLIENT_SECRET=456
    SECRET=something-random
    WHITELIST=me@farsity.de,you@farsity.de

## Configuration of a to-be-secured service

Below is the configuration of sample service which shall be secured by the aforementioned auth proxy.

What has been done here is quite generic i.e. it will also just work for Kibana, Grafana or other Web-based applications.
```yaml
whoamisecure:
image: containous/whoami
labels:
    - "traefik.enable=true"
#     Route which handles HTTPS Traffic
    - "traefik.http.routers.whoamisecure.rule=Host(`api.farsity.de`)"
    - "traefik.http.routers.whoamisecure.entrypoints=websecure"
    - "traefik.http.routers.whoamisecure.tls.certresolver=myresolver"
#     Apply Forward Auth to the Service 
    - "traefik.http.routers.whoamisecure.middlewares=whoamisecure"
    - "traefik.http.middlewares.whoamisecure.forwardauth.address=http://traefikforward:4181"
    - "traefik.http.middlewares.whoamisecure.forwardauth.authResponseHeaders=X-Forwarded-User"
    - "traefik.http.middlewares.whoamisecure.forwardauth.authResponseHeaders=X-Auth-User, X-Secret"
    - "traefik.http.middlewares.whoamisecure.forwardauth.trustForwardHeader=true"
```
## Read on
- Excellent walk-through how to obtain the Google Credentials. But be careful with the configurations as they are written for Traefik v1.7 
([https://www.smarthomebeginner.com/google-oauth-with-traefik-docker/](https://www.smarthomebeginner.com/google-oauth-with-traefik-docker/)).
- Worth to read as well, features the same limitations as the article above ([https://sysadmins.co.za/integrating-google-oauth-with-traefik/](https://sysadmins.co.za/integrating-google-oauth-with-traefik/))