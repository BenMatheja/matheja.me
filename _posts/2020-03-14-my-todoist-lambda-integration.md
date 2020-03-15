---
layout: post
title: Showcase and Storytime - My own Todoist Integration
date: 2020-03-14 09:52 +0100
---
# Why
When I started working at my current employer, there was a unconvenience every day.

Keep track when I arrived at and then calculate when I shall leave the office latest to not get in trouble for beeing present too long. 
The "trouble" actually protects employees, which is quite an asset in Germany. 

But reminding yourself on such stuff seems like unnecessary load for your brain. In the "Getting Things Done" methodology, you should try to put anything that you "have to take care of" into a trusted system.
So in theory, your brain gets clear on the task and you will not feel overburden by the amount of open things to do.

# What
Beeing a heavy Todoist user, I started looking for ways how my "trusted system" would do the "grunt work" of counting hours and reminding me.
Todoist should recognize whenever a Task named "Clock in" has been completed to create another one for this day to clock out at a specific time. The time should be the latest possible clock out to not get into trouble.

I started looking for ways and found the following simple truths. There are few integration platforms which offers a variety of use cases.

## Zapier
[Zapier](https://zapier.com/apps/todoist/integrations) featured a lot of integrations out of the box.
But it wasn't an option as the free plan featured a 15 minute update time. 
I wasn't able to find out, if the update time will exactly be 15 minutes. So waiting 15 minutes until the event has been processed by [Zapier](https://zapier.com/apps/todoist/integrations) seemed like a show stopper. In fact the event entering the office had to be computed in near real-time to produce accurate results.

## IFTT
I looked on [IFTT](https://ifttt.com/todoist) and it immediately looked promising.
The platform has been build on "if XY happened in Todoist, then do YZ". I looked through available integrations but the use case I was longing for was missing. Back in the days the pricing has been different, so a premium plan was necessary to have the integration running.
Every time someone asks you to pay something, you get creative in how to avoid those costs.

## Run your Own
Still i was having a reserved instance running linux at netcup, which was hardly doing any intensive work.
So any integration could run on my own machine. While looking for todoist integrations, I found out that the app itself already offers [Webhooks](https://developer.todoist.com/sync/v8/#webhooks) based on events you can tailor e.g event:created. Shouldn't be that hard to build it on your own.

# How

## Build Python Flask-App and run it on own machine
In that time I was working on a Python [Flask](https://github.com/pallets/flask) backend to receive performance events via a REST API. If you never tried [Flask](https://github.com/pallets/flask) give it a try. It is amazing how concise and easy you can create APIs.

I started building my own integration [todoist-flask](https://github.com/BenMatheja/todoist-flask). A small service, running on my own machine.

![Todoist Flask Overview](/assets/todoist-flask-overview.jpg "Todoist Flask Overview]")

### Learning: Find a smart way to contain your application
In retrospective I probably spent two thirds of the time not on business logic.
Rather I spent a lot of time to build a poor mans CI/CD i.e. how to deploy a version of the app to my instance.

Even more of a hassle seemed to have the app running and being able to see what is happening right now. I developed the app on my machine and ran it with built-in Python HTTP-Server.
Worked like a charm and I could even verify the webhook integration was working using [ngrok](https://ngrok.com/). 
The service creates a tunnel to proxy requests from the web to your local machine. 

Bringing the app to their target environment was the the hardest part.
I planned to use gunicorn instead of the buit-in Python HTTP-Server. Gunicorn would expect a different entry point into the app. As Gunicorn now was running the app, the log output changed. In fact I lost complete visibility on how calls are handled within the application. Some research and configuration afterwards fixed that issue.

I don't want to say it's not possible to have it running smoothly with the aformentioned setup. My (limited) experience with python in general and gunicorn made it a real hassle. 
Learning here: Find a way to package your application to have the same platform and concepts applied already during local development. Nowadays I would probably go for a docker container, package everything and then excessively make sure that the container works as expected.

## Transform the app into a serverless workload
The services has been running for a couple of months and there has been some pain points to adress.

* Todoist deprecated the API-Version I was using for my integration. So my poor mans CI/CD and smart contained app made the upcoming changes a real nightmare to deploy, test and run.
* The service was running all the time for exactly one occurence in 5 of 7 days in the week. Coming to the office early. This was the only moment of a real necessity to have the service running.




* AWS has a Free Tier
* Todoist API is capable of sending onEvent Webhooks (e.g. Task completed)
* Build a serverless Lambda Endpoint capable of consuming the event and acting

* Serverless Framework
* Github Repository https://github.com/BenMatheja/todoist-serverless-lambda
* AWS Region US-West-1

# Next
* Extend the handling of other events (e.g. tracking a streak)
* Improve Security by scoping