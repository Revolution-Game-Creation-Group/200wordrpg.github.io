---
layout: default
---
# News & Updates

<a id="random_button" href="{{site.baseurl}}/feed.xml" class="button">News RSS Feed</a>

<p>
{% assign sorted_pages = site.categories.news | sort:"date" | reverse %}
  {% for post in sorted_pages %}
      <h3><strong><a href="{{ post.url }}">
        {{ post.date | date: "%B %d %Y" }} - {{ post.title }}
      </a></strong></h3>
  {% endfor %}
</p>