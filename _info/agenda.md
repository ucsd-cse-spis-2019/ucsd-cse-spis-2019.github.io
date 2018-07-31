---
title: Agenda (SPIS overall calendar)
layout: default
---

{% assign start_date_yyyymmdd = site.start_date | date: "%Y%m%d" %}
{% assign end_date_yyyymmdd = site.end_date | date: "%Y%m%d" %}

<h2>Agenda (from SPIS Google Calendar)</h2>
<iframe src="{{site.google_calendar_embed_height_600px}}&amp;dates={{start_date_yyyymmdd}}%2F{{end_date_yyyymmdd}}" style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>




