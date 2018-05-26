---
layout: default
---

# 2018 Entries

Here are the entries submitted so far in 2018! 

**If you submitted your entry** it might take a day or two before it shows up here. I'll upload them as fast as I can!

{% assign sorted_pages = (site.categories.2018 | sort:"date") | reverse %}
<table>{% for post in sorted_pages %}
  {% assign loopindex = forloop.index | modulo: 3 %}
  {% if loopindex == 1 %}
    <tr><td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% elsif loopindex == 0 %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td></tr>
  {% else %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% endif %}
 {% endfor %}</table>
