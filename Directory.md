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
# To do Lectures
```dataview
LIST FROM #chapter 
where !completed AND date < date(now) AND date >= date(2024-06-01)
SORT date ASC
```
```dataview
length(LIST FROM #chapter WHERE !completed AND date < date(now) AND date >= date(2024-06-01))
```

`= dv.pages("#chapter").length`



