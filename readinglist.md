---
layout: page
title: Reading List
permalink: /readinglist/
tags: books
---
{% assign sorted_books = site.data.obsidianbooks | sort: "author" %}
Below you'll find books i'm currently reading. If you have any recommendation which one(s) to include, please let me know as i'll always try to keep it updated. Ty!

## ⏯ Reading right now

<ul>
{% for book in sorted_books %}
    {% if book.status == "reading" %}
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

### ⏸️ Up Next

These are already bought and waiting until I can start with them

<ul>
{% for book in sorted_books %}
    {% if book.status == "paused" or book.status == "unread" and book.inventory != "open" %}
     <li>
        <a href="{{ book.link}}">
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author | join: ", " }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}

</ul>
## 🌠 Wishlist

My wishlist currently features {{ site.data.obsidianbooks | where: "status","unread" | where: "inventory","open" | size }} books. If you are looking for a gift, this is the right place.

### :1st_place_medal: Gold Tier 

<ul>
{% for book in sorted_books %}
    {% if book.status == "unread" and book.tier == 1 and book.inventory == "open" %}
     <li>
        <a href="{{ book.link}}">{{ book.author | join: ", " }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### :2nd_place_medal: Silver Tier

<ul>
{% for book in sorted_books %}
    {% if book.status == "unread" and book.tier == 2 and book.inventory == "open" %}
     <li>
        <a href="{{ book.link}}">{{ book.author | join: ", " }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### :3rd_place_medal: Bronze Tier

<ul>
{% for book in sorted_books %}
    {% if book.status == "unread" and book.tier == 3 and book.inventory == "open" %}
     <li>
        <a href="{{ book.link}}">{{ book.author | join: ", " }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

## ✅ Completed

### 2022

In this year I was able to complete {{ site.data.obsidianbooks | where: "status","read" | where: "completed_in",2022 | size }} books so far.
<ul>
{% for book in sorted_books %}
    {% if book.status == "read" and book.completed_in == 2022 %}
     <li>
        <a href="{{ book.link}}">        
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author | join: ", " }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### 2021

In this year I was able to complete these {{ site.data.obsidianbooks | where: "status","read" | where: "completed_in",2021 | size }} books.
<ul>
{% for book in sorted_books %}
    {% if book.status == "read" and book.completed_in == 2021 %}
     <li>
        <a href="{{ book.link}}">        
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author | join: ", " }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### 2020

In this year I was able to complete these {{ site.data.obsidianbooks | where: "status","read" | where: "completed_in",2020 | size }} books.
<ul>
{% for book in sorted_books  %}
    {% if book.status == "read" and book.completed_in == 2020 %}
     <li>
        <a href="{{ book.link}}">
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author | join: ", " }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>

### 2019

In this year I was able to complete these {{ site.data.obsidianbooks | where: "status","read" | where: "completed_in",2019 | size }} books.
<ul>
{% for book in sorted_books  %}
    {% if book.status == "read" and book.completed_in == 2019 %}
     <li>
        <a href="{{ book.link}}">
        {% if book.tier == 1 %}
        :1st_place_medal:
        {% elsif book.tier == 2 %}
        :2nd_place_medal:
        {% else %}
        :3rd_place_medal:
        {% endif %}
        {{ book.author | join: ", " }} - {{ book.title }} </a> </li>
    {% endif %}
{% endfor %}
</ul>
