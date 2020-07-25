---
layout: post
title: "How I'm using Todoist"
author: "Ben Matheja"
categories: journal
tags: [productivity, todoist]
---
My journey with [Todoist](https://todoist.com) began in 2014 during my placement at [Zweitag](https://zweitag.de). 
During a meeting with my former manager Julian, I did a short glance on his screen spotting the infamous red icon. Knowing that Julian was really passionate on efficient working approaches I had to do research of the unknown app.
<!--more-->

Later the underlying concept, the [Getting Things Done methodology](https://gettingthingsdone.com/)  tremendeously helped me to stay focussed during the completion of my Masters studies. If you haven't already read the [Book](https://gettingthingsdone.com/getting-things-done-the-art-of-stress-free-productivity/) i do recommend it. Don't read it by heart, but get inspired by the concepts discussed.

I've compiled some "hacks" on this page which I use to make Todoist productivity tool of choice.

## Use Shared Projects

I'm using a shared project as a shopping list with my spouse. It's dead simple and works with her free plan.

## Use not Ending Tasks with bold typeface
To get a better overview within Projects, you can define tasks which are not completeable serving as kind of sections.

Both convetions lead to a non completeable task with a bold typeface

```
* **Gelbe Säcke** 🗑
```


```
* !!Work!! 👔
```

## Using Unicode Emojis

Todoist supports [unicode Emojis](https://unicode.org/emoji/charts/full-emoji-list.html) within Tasks, Projects and Labels.


## Use Webhook Integration for Custom Workflows

I'm using [Todoist Webhooks](https://developer.todoist.com/sync/v7/#webhooks) to feed completed Tasks into AWS Lambda which inspects the completed task and triggers custom actions such as creating a new task.
The integration is pretty similar to that what [Zapier](https://zapier.com) within premium does, besides it costs me 0€ as it runs within the AWS free tier.

Currently using that to remind me before reaching the 10-hours working time limit in Germany.

The function is based [on a previous project](https://github.com/BenMatheja/todoist-flask) which did the same as a standalone Python [Flask](http://flask.pocoo.org/) application.

## Use Inbox for ideas

* [Use your Inbox to store Ideas](https://www.youtube.com/watch?v=CKjIJYCfBJA&feature=youtu.be)

## See Also
* [Todoist Help on Text Formatting](https://get.todoist.help/hc/en-us/articles/205195102-Text-Formatting-)
* [Usage of Templates in Todoist](https://hairofthedogblog.com/2018/07/using-todoist-photography-workflow/)
* [Essentials of a Productivity System](https://blog.todoist.com/user-stories/systemist-personal-workflow/)
* [Related Concept: Inbox Zero](http://www.43folders.com/izero)

