---
layout: page
title: Reading List
permalink: /readinglist/
tags: books
---
Below you'll find books i'm currently reading. If you have any recommendation which one(s) to include, please let me know!
## In Progress ▶️
<ul>
{% for book in site.data.books %}
    {% if book.status == 1 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## On Hold ⏸️
<ul>
{% for book in site.data.books %}
    {% if book.status == 3 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## Wishlist 📋
My wishlist features {{ site.data.books | where: "status",0 | size }} books so far.
<ul>
{% for book in site.data.books %}
    {% if book.status == 0 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## Completed ✅ 2021
In 2021 I completed {{ site.data.books | where: "status",2 | where: "target",2021 | size }} books so far.
<ul>
{% for book in site.data.books %}
    {% if book.status == 2 and book.target == 2021 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## Completed ✅ 2020
In 2020 I completed {{ site.data.books | where: "status",2 | where: "target",2020 | size }} books.
<ul>
{% for book in site.data.books %}
    {% if book.status == 2 and book.target == 2020 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## Completed ✅ 2019
In 2019 I completed {{ site.data.books | where: "status",2 | where: "target",2019 | size }} books.
<ul>
{% for book in site.data.books %}
    {% if book.status == 2 and book.target == 2019 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>
