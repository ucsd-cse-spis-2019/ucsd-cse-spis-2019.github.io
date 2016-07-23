---
layout: default
title: "FOCS Lectures"
desc: "Week 5"
week: "5"
omit_from_collection: true
---

# {{site.course}}, {{site.year}}

{% include lectures_for_week.html week="5" section_title="Projects" collapsed="false" %}

<!-- Make a link to the lecture page for the date of project demos
     Specified in _config.yml as project_demos_mmdd (e.g. 0902) -->

<ul>
   {% for item in site.lectures %}
   {% assign mmdd = item.lecture_date | date: "%m%d" %}
   {% if mmdd == site.project_demos_mmdd %}
   {% include lecture_link.html
               link_topic_desc_only=item.link_topic_desc_only
               indent=item.indent
               topic=item.topic
               desc=item.desc
               url=item.url
               lecture_date=item.lecture_date
             %}
    {% endif %}
    {% endfor %}
</ul>

----

![SPIS_logo](/images/SPIS_logo.jpg)
