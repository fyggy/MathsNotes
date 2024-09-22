---
tags:
  - preamble
date: {START_DATE}
completed: false
year: {YEAR}
level: {LEVEL}
---
[[Directory]]

Textbooks:

KEATS:

Due Homework:
```dataview
LIST FROM {TAG} AND #homework 
WHERE NOT completed AND date <= date(sow)
SORT date ASC
```


Directory:
```dataview
LIST FROM #{TAG} AND #chapter
SORT date ASC
```


Homework:
```dataview
LIST FROM #{TAG} AND #homework 
SORT pset ASC
```
