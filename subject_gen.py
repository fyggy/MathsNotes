import datetime as dt
import os

## EDITABLE

start_date = dt.date(2024, 9, 23)
end_date = dt.date(2024, 12, 13)

start_dates = [
    dt.date(2024, 9, 23),
    dt.date(2024, 9, 24),
    ]

breaks = [
    [dt.date(2024, 10, 28), dt.date(2024, 11, 3)],
    ]

name = "Groups and Symmetries 1"
TAG = "grp_sym1"
root = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\University\Undergraduate\Second Year"
template = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\University\Undergraduate\Second Year\{TITLE}.md"

## SET

path = root + "\\" + name
def next_event(start, end, starts, breaks):
    week = 0
    while True:
        diff = dt.timedelta(days=7 * week)
        for date in starts:
            current = date + diff
            for brek in breaks:
                if brek[0] <= current <= brek[1]:
                    break
            else:
                if current <= end:
                    yield current
                else:
                    break
        else:
            week += 1
            continue
        break

def relativise(path):
    indx = path.find(r"MathsNotes")
    return path[indx + len("MathsNotes\\"):]


#[print(i) for i in next_event(start_date, end_date, start_dates, breaks)]
nr_lecs = len([i for i in next_event(start_date, end_date, start_dates, breaks)])
#print(nr_lecs)
indx = 3
FIRST = "1. "
LAST = f"{nr_lecs}. "
PREV = ""
NEXT = "2. "
TITLE = "1."
PREFIX = (relativise(path) + "\\").replace("\\", "/")
PREFIX_P = ""
PREFIX_N = PREFIX
#print(PREFIX)
try:
    os.mkdir(path)
except FileExistsError:
    pass

with open(template, mode="r", encoding="utf-8") as f:
    template = f.read()

for date in next_event(start_date, end_date, start_dates, breaks):
    DATE = f"{date.year}-{date.month}-{date.day}"
    print(TITLE)
    current = template.format(FIRST=FIRST, LAST=LAST, PREV=PREV, NEXT=NEXT,
                              TAG=TAG, DATE=DATE, PREFIX=PREFIX, SUB_DIR=name,
                              PREFIX_N=PREFIX_N, PREFIX_P=PREFIX_P)
    with open(path + "\\" + TITLE + ".md", mode="w+", encoding="utf-8") as f:
        f.write(current)
    PREV = TITLE + " "
    TITLE = NEXT[:-1]
    if indx <= nr_lecs:
        NEXT = str(indx) + ". "
    else:
        NEXT = ""
        PREFIX_N = ""
    PREFIX_P = PREFIX
    indx += 1
    
