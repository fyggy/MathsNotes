---
tags:
  - preamble
date: 2024-09-23
completed: false
year: 2
level: 5
---
[[Directory]]

Textbooks:

KEATS:

Due Homework:
```dataview
LIST FROM #grp_sym1 AND #homework 
WHERE !completed AND date > date(sow)
SORT date ASC
```


Directory:
```dataview
LIST FROM #grp_sym1 AND #chapter
SORT date ASC
```


Homework:
```dataview
LIST FROM #grp_sym1 AND #homework 
SORT pset ASC
```
