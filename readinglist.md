---
layout: page
title: Reading List
permalink: /readinglist/
tags: books
---
{% assign sorted_books = site.data.books | sort: "author" %}
Below you'll find books i'm currently reading. If you have any recommendation which one(s) to include, please let me know as i'll always try to keep it updated. Ty!

## ⏯ Currently Reading

<ul>
{% for book in sorted_books %}
    {% if book.status == 1 %}
     <li>
        <a href="{{ book.link}}"> 
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### ⏸️ On Hold

<ul>
{% for book in sorted_books %}
    {% if book.status == 3 %}
     <li>
        <a href="{{ book.link}}">
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## 🌠 Wishlist

My wishlist currently features {{ site.data.books | where: "status",0 | size }} books.

### :1st_place_medal: Gold Tier 

<ul>
{% for book in sorted_books %}
    {% if book.status == 0 and book.tier == 1 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### :2nd_place_medal: Silver Tier

<ul>
{% for book in sorted_books %}
    {% if book.status == 0 and book.tier == 2 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### :3rd_place_medal: Bronze Tier

<ul>
{% for book in sorted_books %}
    {% if book.status == 0 and book.tier == 3 %}
     <li>
        <a href="{{ book.link}}">{{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## ✅ Completed

### 2022

In this year I was able to complete {{ site.data.books | where: "status",2 | where: "target",2022 | size }} books so far.
<ul>
{% for book in sorted_books %}
    {% if book.status == 2 and book.target == 2022 %}
     <li>
        <a href="{{ book.link}}">        
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### 2021

In this year I was able to complete these {{ site.data.books | where: "status",2 | where: "target",2021 | size }} books.
<ul>
{% for book in sorted_books %}
    {% if book.status == 2 and book.target == 2021 %}
     <li>
        <a href="{{ book.link}}">        
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### 2020

In this year I was able to complete these {{ site.data.books | where: "status",2 | where: "target",2020 | size }} books.
<ul>
{% for book in sorted_books  %}
    {% if book.status == 2 and book.target == 2020 %}
     <li>
        <a href="{{ book.link}}">
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### 2019

In this year I was able to complete these {{ site.data.books | where: "status",2 | where: "target",2019 | size }} books.
<ul>
{% for book in sorted_books  %}
    {% if book.status == 2 and book.target == 2019 %}
     <li>
        <a href="{{ book.link}}">
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>
