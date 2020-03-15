---
layout: post
title: transform todoist integration to serverless
date: 2020-03-15 10:00 +0100
---
## WHY

## WHAT

## HOW

### Transform the app into a serverless workload
The services has been running for a couple of months and there has been some pain points to adress.

* Todoist deprecated the API-Version I was using for my integration. So my poor mans CI/CD and smart contained app made the upcoming changes a real nightmare to deploy, test and run.
* The service was running all the time for exactly one occurence in 5 of 7 days in the week. Coming to the office early. This was the only moment of a real necessity to have the service running.




* AWS has a Free Tier
* Todoist API is capable of sending onEvent Webhooks (e.g. Task completed)
* Build a serverless Lambda Endpoint capable of consuming the event and acting

* Serverless Framework
* Github Repository https://github.com/BenMatheja/todoist-serverless-lambda
* AWS Region US-West-1

## Next
* Extend the handling of other events (e.g. tracking a streak)
* Improve Security by scoping