---
tags:
  - preamble
  - current
  - dynamics
  - classdyn1
  - mechanics
  - newtonian_mechanics
  - applied
  - physics
  - differential_equations
  - calculus
date: 2024-09-23
completed: false
year: 2
level: 5
institution: King's Collage London
---
[[Directory]]

Textbooks:
[[classical_dynamics_lecture_notes.pdf|Lecture Notes]]
#todo 

KEATS:
https://keats.kcl.ac.uk/course/view.php?id=119766

Due Homework:
```dataview
LIST FROM #classdyn1 AND #homework 
WHERE !completed AND date <= date(eow)
SORT date ASC
```
Directory:
```dataview
LIST FROM #classdyn1 AND #chapter
SORT date ASC
```
Homework:
```dataview
LIST FROM #classdyn1 AND #homework 
SORT pset ASC
```
