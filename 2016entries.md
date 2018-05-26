---
layout: default
---

# 2016 Entries

The 2016 challenge featured two categories: **Supplements** and **RPGs**. There were some incredible submissions in both categories, all of which are listed below.

## 2016 RPGs

{% assign sorted_pages = site.categories.2016 | sort:"title" %}
{% tablerow post in sorted_pages cols:3 %}
<strong><a href="{{ post.url }}">{{ post.title }}</a></strong>
{% endtablerow %}

<hr>

## 2016 Supplements

{% assign sorted_pages = site.categories.2016 | sort:"title" %}
{% tablerow post in sorted_pages cols:3 %}
<strong><a href="{{ post.url }}">{{ post.title }}</a></strong>
{% endtablerow %}
