---
layout: default
---
# 2015 Entries

The 2015 Challenge was the first year! We allowed pictures and fancy layouts, so all of these entries are images, not text, which makes them stand out from future entries.

<table>
{% assign sorted_pages = site.categories.2015 | sort:"title" %}
  {% for post in sorted_pages %}
  {% assign loopindex = forloop.index | modulo: 3 %}
  {% if loopindex == 1 %}
    <tr><td id="centeredText">
      <strong><a href="{{ post.url }}">{{ post.title }}</a></strong>
    </td>
  {% elsif loopindex == 0 %}
    <td id="centeredText">
      <strong><a href="{{ post.url }}">{{ post.title }}</a></strong>
    </td></tr>
  {% else %}
    <td id="centeredText">
      <strong><a href="{{ post.url }}">{{ post.title }}</a></strong>
    </td>
  {% endif %}
 {% endfor %}
</table>
