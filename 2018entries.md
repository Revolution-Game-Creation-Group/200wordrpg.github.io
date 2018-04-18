---
layout: default
---

# 2018 Entries

The 2018 Challenge will start on May 18th! Check the [front page](/) for details and updates.

<p>
{% assign sorted_pages = (site.categories.2018 | sort: 'title') %}
  {% for post in sorted_pages %}
      <strong>&emsp;•&emsp;<a href="{{ post.url }}">
        {{ post.title }}
      </a></strong>
  {% endfor %}
</p>
