---
layout: default
---

# 2017 Entries

The 2017 challenge was the largest yet, featuring nearly 700 entries! They are all listed below, along with author comments. Enjoy!

{% assign sorted_pages = site.categories.2017 | sort:"title" %}
{% tablerow post in sorted_pages cols:3 %}
<strong><a href="{{ post.url }}">{{ post.title }}</a></strong>
{% endtablerow %}
