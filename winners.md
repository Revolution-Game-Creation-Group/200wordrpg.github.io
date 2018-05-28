---
layout: default
---

# Winners
Chosen by the [Judges]({{site.baseurl}}/judges), these entries were particularly creative and engaging! There are no 1st, 2nd, or 3rd places, only top three winners in no particular order.

### **2017** :&emsp;[MECHANICAL ORYX]({% post_url /2017/2017-04-15-MECHANICALORYX %})&emsp;•&emsp;[Memories]({% post_url /2017/2017-04-21-Memories %})&emsp;•&emsp;[Route Clearance]({% post_url /2017/2017-04-22-RouteClearance %})

### **2016** RPGs:&emsp;[Deconstruction]({{site.baseurl}}{% post_url /2016/2016-04-12-Deconstruction %})&emsp;•&emsp;[Stardust]({{site.baseurl}}{% post_url /2016/2016-04-09-Stardust %})&emsp;•&emsp;[Time Travel Thaw]({{site.baseurl}}{% post_url /2016/2016-04-14-TimeTravelThaw %})
 
### **2016** Supplements:&emsp;[The College Animalia]({{site.baseurl}}{% post_url /2016/2016-04-06-TheCollegeAnimalia %})&emsp;•&emsp;[First Steps]({{site.baseurl}}{% post_url /2016/2016-04-17-FirstStepsAdventuringWorkshop %})&emsp;•&emsp;[Foam Dart RPG]({{site.baseurl}}{% post_url /2016/2016-04-07-FoamDartRPG %})

### **2015**:&emsp;[All Fall Down]({{site.baseurl}}{% post_url /2015/2015-04-01-AllFallDown %})&emsp;•&emsp;[Escape Pod One]({{site.baseurl}}{% post_url /2015/2015-04-01-EscapePodOne %})&emsp;•&emsp;[LOVEINT]({{site.baseurl}}{% post_url /2015/2015-04-01-LOVEINT %})

# 2017 Finalists

Out of nearly 700 entries, these were chosen by a [panel of judges]({{site.baseurl}}/judges) to be among the best of 2017:

{% assign sorted_pages = site.categories.2017 | where_exp: "post", "post.categories contains 'finalist'" | sort:"title" %}
<table>{% for post in sorted_pages %}
  {% assign loopindex = forloop.index | modulo: 3 %}
  {% if loopindex == 1 %}
    <tr><td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% elsif loopindex == 0 %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td></tr>
  {% else %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% endif %}
 {% endfor %}</tr></table>

# 2016 Finalists

Out of over 300 entries, these were chosen by a [panel of judges]({{site.baseurl}}/judges) to be among the best of 2016:

{% assign sorted_pages = site.categories.2016 | where_exp: "post", "post.categories contains 'finalist'" | sort:"title" %}
<table>{% for post in sorted_pages %}
  {% assign loopindex = forloop.index | modulo: 3 %}
  {% if loopindex == 1 %}
    <tr><td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% elsif loopindex == 0 %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td></tr>
  {% else %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% endif %}
 {% endfor %}</tr></table>

# 2015 Finalists

Out of nearly 250 entries, these were chosen by a [panel of judges]({{site.baseurl}}/judges) to be among the best of 2015:

{% assign sorted_pages = site.categories.2015 | where_exp: "post", "post.categories contains 'finalist'" | sort:"title" %}
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
