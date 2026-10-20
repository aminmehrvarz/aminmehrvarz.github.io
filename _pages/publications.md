---
layout: academic
permalink: /publications/
title: Publications
description: Publications listed in Amin Mehrvarz's supplied CV.
nav: true
nav_order: 3
---

<link rel="stylesheet" href="{{ '/assets/css/academic-layout.css' | relative_url }}">

{% assign publications = site.data.publications | sort: "year" | reverse %}
{% for publication in publications %}
{% include publication-entry.liquid publication=publication %}
{% endfor %}
