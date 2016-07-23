---
layout: default
title: "UCSD CSE 2016 SPIS: Foundations of Computer Science"
---

# {{site.course}}, {{site.year}}

<div id="info" data-role="collapsible" data-collapsed="false">
<h2>Course Information</h2>
<ul>
{% for item in site.info %}
<li><a href="{{item.url}}"  data-ajax="false">{{item.title }}</a></li>
{% endfor %}
</ul>
</div>

<div data-role="collapsible" data-collapsed="false">
<h2 id="labs">Lectures</h2>
  {% include lectures_for_week.html week="1" collapsed="false" %}
  {% include lectures_for_week.html week="2" collapsed="true" %}
  {% include lectures_for_week.html week="3" collapsed="true" %}
  {% include lectures_for_week.html week="4" collapsed="true" %}
  {% include lectures_for_week.html week="5" section_title="Projects" collapsed="false" %}
</div>

<div data-role="collapsible" data-collapsed="false">
<h2 id="homework">Homework</h2>
{% include hwk_table.html %}
</div>

<div data-role="collapsible" data-collapsed="false">
<h2 id="labs">Labs</h2>
{% include lab_table.html %}
</div>

<div data-role="collapsible" data-collapsed="false">
<h2 id="labs">Topics</h2>
 <ul>
 {% for item in site.topics %}
   <li><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
 </ul>
</div>


<div data-role="collapsible" data-collapsed="false">
<h2 id="labs">Projects</h2>

 <div data-role="collapsible" data-collapsed="false">
 <h3>Big Data</h3>
 <ul>
 {% for item in site.bigdata %}
   <li><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
 </ul>
 </div>

 <div data-role="collapsible" data-collapsed="false">
 <h3>Robotics</h3>
 <ul>
 {% for item in site.robotics %}
   <li><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
 </ul>
 </div>
 
 <div data-role="collapsible" data-collapsed="false">
 <h3>Big Data</h3>
 <ul>
 {% for item in site.webapps %}
   <li><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
 </ul>
 </div>
 
</div>



----

![SPIS_logo](images/SPIS_logo.jpg)
