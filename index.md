---
layout: default
title: "UCSD CSE 2016 SPIS: Foundations of Computer Science"
---

# {{site.course}}, {{site.year}}

<div id="info" data-role="collapsible" data-collapsed="false" name="info">
<h2>Course Information</h2>
<ul>
{% for item in site.info %}
<li><a href="{{item.url}}"  data-ajax="false">{{item.title }}</a></li>
{% endfor %}
</ul>
</div>

<div data-role="collapsible" data-collapsed="false" markdown="0" name="lectures">
<h2 id="labs">Lectures</h2>
  {% include lectures_for_week.html week="1"
    collapsible="true" collapsed="true" %}
  {% include lectures_for_week.html week="2"
    collapsible="true" collapsed="true" %}
  {% include lectures_for_week.html week="3"
    collapsible="true" collapsed="true" %}
  {% include lectures_for_week.html week="4"
    collapsible="true" collapsed="false" %}
  {% include lectures_for_week.html week="5" section_title="Projects"
    collapsible="true" collapsed="true" extra_item="0902" %}
</div>

<div data-role="collapsible" data-collapsed="false" name="homework">
<h2 id="homework">Homework</h2>
{% include hwk_table.html %}
</div>

<div data-role="collapsible" data-collapsed="false" name="labs">
<h2 id="labs">Labs</h2>
{% include lab_table.html %}
</div>

<div data-role="collapsible" data-collapsed="false" name="topics">
<h2 id="labs">Topics</h2>
 <ul>
 {% for item in site.topics %}
   <li><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
 </ul>
</div>


<div data-role="collapsible" data-collapsed="false" name="projects">
<h2 id="labs">Projects</h2>

 <div data-role="collapsible" data-collapsed="false" name="bigdata">
 <h3>The Marvelous Big Data Guide</h3>
 <p>(Procured by your ever-faithful data tour guide, Maxwell Bland)</p>
 <ul>
 {% for item in site.bigdata %}
   <li><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
 </ul>
 </div>

 <div data-role="collapsible" data-collapsed="false" name="robotics">
 <h3>Robotics</h3>
 <ul>
 {% for item in site.robotics %}
   <li><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
 </ul>
 </div>
 
 <div data-role="collapsible" data-collapsed="false" name="webapps"> 
 <h3>Web Apps</h3>
 <ul>
 {% for item in site.webapps %}
   <li {% if item.indent %} class="indent" {% endif %} ><a href="{{item.url}}">{{item.topic}}&mdash;{{item.desc}}</a></li>
 {% endfor %}
 </ul>
 </div>
 
</div>



----

![SPIS_logo](images/SPIS_logo.jpg)
