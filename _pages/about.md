---
layout: academic
title: Home
nav_title: Home
permalink: /
nav: false
nav_order: 1
selected_papers: false
social: false
---

<link rel="stylesheet" href="{{ '/assets/css/academic-layout.css' | relative_url }}">
<div class="academic-biography" markdown="1">

I am a Senior Software Engineer in Surgical Robotics at Medtronic in Boston. My work includes control algorithm and robotics, real-time inverse kinematics, and trajectory generation.

I received my Ph.D. in Mechanical Engineering, with a focus on Robotics/Mechatronics, from Northeastern University in 2021. My dissertation studied tunable active metamaterials using feed-forward and feedback controllers. I earned my M.Sc. and B.Sc. in Mechanical Engineering from Sharif University of Technology.

My research interests include control theory, robotics, mechatronics, machine learning, multibody dynamics, wave propagation, vibrations, and acoustics.

</div>

## Selected Publications

{% assign selected_publications = site.data.publications | where: "selected", true %}
{% for publication in selected_publications %}
{% include publication-entry.liquid publication=publication selected=true %}
{% endfor %}

<p class="all-publications"><a href="{{ '/publications/' | relative_url }}" aria-label="View all publications">All Publications →</a></p>

## Education

{% for education in site.data.academic.education %}
- **{{ education.degree | escape }}**, {{ education.institution | escape }} ({{ education.dates | escape }}).{% if education.thesis %} {{ education.thesis_label | escape }}: {{ education.thesis | escape }}{% endif %}
{% endfor %}

## Experience

{% for experience in site.data.academic.experience %}
- **{{ experience.role | escape }}**, {{ experience.organization | escape }} ({{ experience.dates | escape }}).
{% endfor %}

## Selected Honors and Awards

{% for award in site.data.academic.awards %}
- {{ award | escape }}
{% endfor %}
