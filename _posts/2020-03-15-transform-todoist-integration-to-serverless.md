---
layout: post
title: Journey to Serverless - Transform the Todoist Integration to Lambda
date: 2020-03-15 10:00 +0100
---
## WHY
My current approach had a lot of shortcomings.

Firstly the way I was developing the app and how it ran in production was not reproducible.
There was no real CI/CD process and the packaging of the app itself really differed from dev to production. This caused issues, whenever changes were brought to production.

The simple function consisted of too many moving parts which also introduced more complexity to the overall system.
I used an self-configured Nginx as reverse proxy. There was the infamous Gunicorn with it's own configuration files and last but not least the Python App itself.

The durability of the app was not convincing. From a user's perspective the performance got worse the longer the application has been running. This resulted in dropped clock-in events and made the service not usable.
I remember someone talking about self-driving cars and he said "if it doesn't work in all circumstances - there is no use for it". To be honest, the complexity of the todoist integration is trivial compared to the challenges of writing software for self-driving cars, but still the argument holds.

The handling of credentials was far from easy and optimal. With the current app, they were just inserted to an settings.py file on the machine. T


## WHAT

* Use a Framework for Serverless (Zappa, Serverless)
* Used both, Serverless seemed more mature to me - both work

* Use Serverless Functions
* Only looked upon Lambda


## HOW

* AWS has a Free Tier
* Deploy App to Lambda from local
* Configure Todoist API to send events to Lambda Endpoint
* Choose an Endpoint which is closest possible to Todoist (service is in US-WEST)

* Github Repository https://github.com/BenMatheja/todoist-serverless-lambda
* AWS Region US-West-1

## Next
* Extend the handling of other events (e.g. tracking a streak)
* Improve Security by scoping