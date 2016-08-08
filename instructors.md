---
layout: default
title: Instructor info
---

# {{site.course}}, {{site.year}} Instructor Info

<ul>
 {% for item in site.instructor %}
   <li><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
</ul>

![SPIS_logo](images/SPIS_logo.jpg)