---
layout: default
---

# 2016 Entries

The 2016 challenge featured two categories: **Supplements** and **RPGs**. There were some incredible submissions in both categories, all of which are listed below.

{% assign sorted_pages = site.categories.2016 %}
{% assign rpg_sorted_pages = sorted_pages.categories.rpg | sort:"title" %}
{% for currentpost in categories.2016 %}
    {% if post.categories contains "supplement" %}
    {% assign supplement_posts = currentpost %}
    {% else %}
    {% assign rpg_posts = currentpost %}
    {% endif %}
{% endfor %}

## 2016 RPGs

<table>{% for post in rpg_posts %}
  {% assign loopindex = forloop.index | modulo: 3 %}
  {% if loopindex == 1 %}
    <tr><td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% elsif loopindex == 0 %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td></tr>
  {% else %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% endif %}
 {% endfor %}</tr></table>

<hr>

## 2016 Supplements

<table>{% for post in supplement_posts %}
  {% assign loopindex = forloop.index | modulo: 3 %}
  {% if loopindex == 1 %}
    <tr><td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% elsif loopindex == 0 %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td></tr>
  {% else %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% endif %}
 {% endfor %}</tr></table>
