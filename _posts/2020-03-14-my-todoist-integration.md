---
layout: post
title: Showcase - Build your own Todoist Integration
date: 2020-03-14 09:52 +0100
tags: todoist productivity python development
---
When I started working at my current employer, I noticed an unconvenience every day.
Keeping track of the time of arrival and calculate when I should leave the office latest possible to not get into trouble for beeing present too long. This "trouble" actually protects employees, which is quite an asset in Germany. 
<!--more-->

But reminding yourself on such stuff seems like unnecessary load for your brain. In the "Getting Things Done" methodology, you should try to put anything that you "have to take care of" into a trusted system.
So in theory, your brain gets clear on the task and you will not feel overburden by the amount of open things to do.

## What
Beeing a heavy Todoist user, I started looking for ways how my "trusted system" would do the "grunt work" of counting hours and reminding me.
Todoist should recognize whenever a Task named "Clock in" has been completed to create another one for this day to clock out at a specific time. The time should be the latest possible clock out to not get into trouble.

I started looking for ways and found the following simple truths. There are few integration platforms which offers a variety of use cases.

### Zapier
[Zapier](https://zapier.com/apps/todoist/integrations) featured a lot of integrations out of the box.
But it wasn't an option as the free plan featured a 15 minute update time. 

I wasn't able to find out, if the update time will exactly be 15 minutes. So waiting 15 minutes until the event has been processed by [Zapier](https://zapier.com/apps/todoist/integrations) seemed like a show stopper. In fact the event entering the office had to be computed in near real-time to produce accurate results.

### IFTT
I looked on [IFTT](https://ifttt.com/todoist) and it immediately seemed promising.
The platform has been build on "if XY happened in Todoist, then do YZ". 

I looked through available integrations but the use case I was longing for was missing. Back in the days the pricing has been different, so a premium plan was necessary to have the integration running.
Every time someone asks you to pay something, you get creative in how to avoid those costs.

### Run your Own
Still i was having a reserved instance running linux at netcup, which was hardly doing any intensive work.
So any integration could run on my own machine. While looking for todoist integrations, I found out that the app itself already offers [Webhooks](https://developer.todoist.com/sync/v8/#webhooks) based on events you can tailor e.g event:created. Shouldn't be that hard to build it on your own.

## How

### Python Flask-App running on your own machine
In that time I was working on a Python [Flask](https://github.com/pallets/flask) backend to receive performance events via a REST API. If you never tried [Flask](https://github.com/pallets/flask) give it a try. It is amazing how concise and easy you can create APIs.

````python
@app.route('/todoist/events/v1/items', methods=['POST'])
def handle_event():
    begin_time = datetime.datetime.now()
    event_id = request.headers.get('X-Todoist-Delivery-ID')
    # Check if user-agent matches to todoist webhooks
    if request.headers.get('USER-AGENT') == 'Todoist-Webhooks':
````


I started building my own integration [todoist-flask](https://github.com/BenMatheja/todoist-flask). A small service, running on my own machine.

![Todoist Flask Overview](/assets/todoist-flask-overview.jpg "Todoist Flask Overview]")

#### Learning: Find a smart way to contain your application
In retrospective I probably spent two thirds of the time not on business logic.
Rather I spent a lot of time to build a poor mans CI/CD i.e. how to deploy a version of the app to my instance.

Even more of a hassle seemed to have the app running and being able to see what is happening right now. I developed the app on my machine and ran it with built-in Python HTTP-Server.
Worked like a charm and I could even verify the webhook integration was working using [ngrok](https://ngrok.com/). 
The service creates a tunnel to proxy requests from the web to your local machine. 

Bringing the app to their target environment was the the hardest part.
I planned to use [Gunicorn](https://gunicorn.org/) instead of the buit-in Python HTTP-Server. [Gunicorn](https://gunicorn.org/) would expect a different entry point into the app. As [Gunicorn](https://gunicorn.org/) now was running the app, the log output changed. In fact I lost complete visibility on how calls are handled within the application. Some research and configuration afterwards fixed that issue.

I don't want to say it's not possible to have it running smoothly with the aformentioned setup. My (limited) experience with python in general and [Gunicorn](https://gunicorn.org/) made it a real hassle. 
Learning here: Find a way to package your application to have the same platform and concepts applied already during local development. Nowadays I would probably go for a docker container, package everything and then excessively make sure that the container works as expected.

## Next
The service has been running for a couple of months and there are pain points to adress.

* Todoist deprecated the version of the sync API I was using for my integration. So my poor mans CI/CD and smart contained app made the upcoming changes a real nightmare to deploy, test and run.
* The service was running all the time for exactly one occurence within the work days. Coming to the office early. This was the only moment of a real necessity to have the service running.
* After running some time, the service seemed to get unresponsive. Clock-in events were handled (if they were) after minutes, resulting in unreliable clock-out tasks.

![SERVERLESS All the Things](/assets/serverless-all-the-things.jpg "Serverless")

The integration is the perfect use-case for a serverless workload.
* The function to create the clock-out task is really small 
* The footprint of the python app with regards to startup-time and memory consumption is small (no heavy JVM / Springboot startup)
* The function is only used occasionally.