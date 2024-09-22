---
tags:
  - preamble
  - "#todo"
date: {START_DATE}
completed: false
year: {YEAR}
level: {LEVEL}
---
[[Directory]]

Textbooks:
#todo 

KEATS:
#todo
Due Homework:
```dataview
LIST FROM #{TAG} AND #homework 
WHERE !completed AND date <= date(eow)
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
