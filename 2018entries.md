---
layout: default
---

# 2018 Entries

Here are the entries submitted in 2018! 

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
 {% endfor %}
  {% if loopindex == 0 %}
    </table>
  {% else %}
    </tr></table>
  {% endif %}
