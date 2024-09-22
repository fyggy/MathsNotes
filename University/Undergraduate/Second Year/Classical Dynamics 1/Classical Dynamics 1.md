---
tags:
  - preamble
  - "#todo"
date: 2024-09-23
completed: false
year: 2
level: 5
---
[[Directory]]

Textbooks:
#todo 

KEATS:
#todo
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
