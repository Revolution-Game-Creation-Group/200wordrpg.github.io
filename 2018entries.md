---
layout: default
---

# 2018 Entries

Here are the entries submitted so far in 2018! 

**If you submitted your entry** it might take a day or two before it shows up here. I'll upload them as fast as I can!

{% assign sorted_pages = (site.categories.2018 | sort:"date") | reverse %}
{% tablerow post in sorted_pages cols:3 %}
<strong><a href="{{ post.url }}">{{ post.title }}</a></strong>
{% endtablerow %}
