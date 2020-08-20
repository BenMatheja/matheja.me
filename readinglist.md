---
layout: page
title: Reading List
permalink: /readinglist/
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
<ul>
{% for book in site.data.books %}
    {% if book.status == 0 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## Completed ✅ 2020
<ul>
{% for book in site.data.books %}
    {% if book.status == 2 and book.target == 2020 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## Completed ✅ 2019
<ul>
{% for book in site.data.books %}
    {% if book.status == 2 and book.target == 2019 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>
