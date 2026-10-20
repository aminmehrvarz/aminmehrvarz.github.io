---
layout: academic
permalink: /research/
title: Research
description: Amin Mehrvarz's research interests and documented projects.
nav: true
nav_order: 2
---

<link rel="stylesheet" href="{{ '/assets/css/academic-layout.css' | relative_url }}">

My research interests span control theory, robotics, mechatronics, machine learning, multibody dynamics, wave propagation, vibrations, and acoustics. My doctoral work at Northeastern University focused on tunable active metamaterials using feed-forward and feedback control. My earlier research at Sharif University of Technology addressed nonlinear and adaptive control, PDE-based control, and fluid–structure interaction.

## Projects

{% for project in site.data.research_projects %}
<article class="my-6 border-b pb-6">
  <h2>{{ project.title | escape }}</h2>
  <p>{{ project.description | escape }}</p>
  {% if project.image %}
    <img class="my-4 h-auto max-w-full" src="{{ project.image | relative_url }}" alt="{{ project.image_alt | default: project.title | escape }}" loading="lazy">
  {% endif %}
  {% if project.paper_url or project.code_url %}
    <p class="flex flex-wrap gap-x-3">
      {% if project.paper_url %}<a href="{{ project.paper_url | escape }}">Paper</a>{% endif %}
      {% if project.code_url %}<a href="{{ project.code_url | escape }}">Code</a>{% endif %}
    </p>
  {% endif %}
</article>
{% endfor %}
