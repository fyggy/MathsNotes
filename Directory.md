# Current Classes:
```dataview
LIST FROM #preamble and #current
SORT  file.name ASC, date asc
```
# Due Homework:
```dataview
LIST FROM #homework 
where !completed AND date <= date(eow)
SORT date ASC
```

# Maths notes:
```dataview
LIST FROM #preamble 
SORT file.name ASC, date ASC
```
# Other
- [[The plan]]
