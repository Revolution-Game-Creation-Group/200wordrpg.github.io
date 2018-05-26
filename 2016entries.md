---
layout: default
---

# 2016 Entries

The 2016 challenge featured two categories: **Supplements** and **RPGs**. There were some incredible submissions in both categories, all of which are listed below.

## 2016 RPGs

{% assign sorted_pages = site.categories.2016 %}
{% assign rpg_sorted_pages = sorted_pages.categories.rpg | sort:"title" %}
<table>{% for post in rpg_sorted_pages %}
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

{% assign sorted_pages = site.categories.2016 %}
{% assign supplement_sorted_pages = sorted_pages.categories.supplement | sort:"title" %}
<table>{% for post in supplement_sorted_pages %}
  {% assign loopindex = forloop.index | modulo: 3 %}
  {% if loopindex == 1 %}
    <tr><td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% elsif loopindex == 0 %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td></tr>
  {% else %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% endif %}
 {% endfor %}</tr></table>
