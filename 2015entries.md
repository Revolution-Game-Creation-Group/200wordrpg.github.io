---
layout: default
---
# 2015 Entries

The 2015 Challenge was the first year! We allowed pictures and fancy layouts, so all of these entries are images, not text, which makes them stand out from future entries.

{% assign sorted_pages = site.categories.2015 | sort:"title" %}
{% tablerow post in sorted_pages cols:3 %}
<strong><a href="{{ post.url }}">{{ post.title }}</a></strong>
{% endtablerow %}
