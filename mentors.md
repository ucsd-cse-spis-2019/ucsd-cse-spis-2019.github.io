---
layout: default
title: Mentor info
---

# {{site.course}}, {{site.year}} Mentor Info

<ul>
 {% for item in site.mentor %}
   <li><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
</ul>

![SPIS_logo](images/SPIS_logo.jpg)