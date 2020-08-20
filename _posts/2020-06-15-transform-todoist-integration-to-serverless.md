---
layout: post
title: Journey to Serverless - Migrated my Todoist Integration to Lambda
date: 2020-06-15 10:00 +0100
tags: aws lambda todoist python development
---
I migrated my [Todoist Webhook Integration](https://github.com/BenMatheja/todoist-serverless-lambda) from a self-hosted version towards [AWS Lambda](https://aws.amazon.com/lambda/).

Here is why!

<!--more-->
## Why
My old approach had a lot of shortcomings.

The way I was developing on the app and how it ran in production was not the same.
There was no real CI/CD process involved and the packaging of the app itself really differed from local development. This caused issues, whenever changes had to be done.

The simple function consisted of too many moving parts which also introduced more complexity to the overall system.
I used an *apt-get installed* Nginx as reverse proxy. There was [Gunicorn](https://github.com/benoitc/gunicorn) with it's own configuration files and last but not least the Python App itself.

The durability of the app was not convincing. From a user's perspective the performance got worse the longer the application has been running. This resulted in dropped events and made the service not reliable.
I remember someone talking about self-driving cars and he said "if it doesn't work in all circumstances - there is no use for it". To be honest, the complexity of the [Todoist Webhook Integration](https://github.com/BenMatheja/todoist-serverless-lambda) is trivial compared to the challenges of writing software for self-driving cars, but still the argument holds.

The handling of credentials was far from optimal. With the current app, they were just inserted to an settings.py file on the machine.


## What I did

I used both [Zappa](https://github.com/Miserlou/Zappa) and [Serverless](https://www.serverless.com/) for setting up the AWS Stack and configuring the app to run properly on [AWS Lambda](https://aws.amazon.com/lambda/). Serverless seemed more mature to me which is the reason I'm still using it that way.

The integration runs at free tier with no hassle. I configured [Todoist Webhooks](https://developer.todoist.com/sync/v8/#webhooks) to fire whenever an item on my list is marked as *completed* 

I reduced the moving parts necessary to maintain, it's just packaging the app, making sure that it'll run, deploy it, test it on Lambda and you're done.

I kind of fought with Github Actions to set up a CI/CD but can say that it'll now deploy to AWS whenever something is pushed to master. This is a real relief, knowing that wherever I commit changes to the repository, the app will get deployed in the same (working) way.
So you can say I'm pretty happy with the status quo of the app.

## Future
* Let Github Actions run integration tests after deployment on dev (e.g. is the Endpoint responding as expected using newman or something else). If succesfull stage to prod




