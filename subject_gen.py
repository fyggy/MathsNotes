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

NAME = "Groups and Symmetries 1"
TAG = "grp_sym1"
YEAR = 2
LEVEL = 5

root = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\University\Undergraduate\Second Year"
template_dir = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\Templates"
lecture_temp = "Lecture Template.md"
preamble_temp = "Preamble Template.md"

## SET

path = root + "\\" + NAME
lec_path = path + "\\" + "Lectures"
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


print(sorted([str(i) for i in next_event(start_date, end_date, start_dates, breaks)]))
nr_lecs = len([i for i in next_event(start_date, end_date, start_dates, breaks)])
#print(nr_lecs)
indx = 3
FIRST = "1. "
LAST = f"{nr_lecs}. "
PREV = ""
NEXT = "2. "
TITLE = "1."
PREFIX = (relativise(lec_path) + "\\").replace("\\", "/")
PREFIX_P = ""
PREFIX_N = PREFIX
PREFIX_S = (relativise(path) + "\\").replace("\\", "/")
#print(PREFIX)
try:
    os.mkdir(path)
except FileExistsError:
    pass

try:
    os.mkdir(lec_path)
except FileExistsError:
    pass

with open(template_dir + "\\" + preamble_temp, mode="r", encoding="utf-8") as f:
    pre_template = f.read()

preamble = pre_template.format(START_DATE=start_date, YEAR=YEAR, LEVEL=LEVEL,
                               TAG=TAG)

with open(path + "\\" + NAME + ".md", mode="w", encoding="utf-8") as f:
    f.write(preamble)

with open(template_dir + "\\" + lecture_temp, mode="r", encoding="utf-8") as f:
    lec_template = f.read()

for date in next_event(start_date, end_date, start_dates, breaks):
    DATE = f"{date.year}-{date.month}-{date.day}"
    print(TITLE)
    current = lec_template.format(FIRST=FIRST, LAST=LAST, PREV=PREV, NEXT=NEXT,
                              TAG=TAG, DATE=DATE, PREFIX=PREFIX, SUB_DIR=NAME,
                              PREFIX_N=PREFIX_N, PREFIX_P=PREFIX_P,
                              PREFIX_S=PREFIX_S)
    with open(lec_path + "\\" + TITLE + ".md", mode="w+", encoding="utf-8") as f:
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
    
