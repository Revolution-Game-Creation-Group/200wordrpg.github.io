---
layout: default
---

# 2016 Entries

The 2016 challenge featured two categories: **Supplements** and **rpgs**. There were some incredible submissions in both categories, all of which are listed below.

## 2016 RPGs

<p>
{% assign sorted_pages = site.categories.2016 | sort: "title" %}
  {% for post in sorted_pages %}
      {% if post.categories contains 'rpg' %}
      <strong>&emsp;•&emsp;<a href="{{ post.url }}">
        {{ post.title }}
      </a></strong>
        {% endif %}
  {% endfor %}
</p>

<hr>

## 2016 Supplements

<p>
{% assign sorted_pages = site.categories.2016 | sort: "title" %}
  {% for post in sorted_pages %}
      {% if post.categories contains 'supplement' %}
      <strong>&emsp;•&emsp;<a href="{{ post.url }}">
        {{ post.title }}
      </a></strong>
        {% endif %}
  {% endfor %}
</p>