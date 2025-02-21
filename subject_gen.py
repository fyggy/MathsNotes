

import datetime as dt
import os

def relativise(path):
    indx = path.find(r"MathsNotes")
    return path[indx + len("MathsNotes\\"):]

def next_event(start, end, starts, breaks):
    week = 0
    while True:
        diff = dt.timedelta(days=week * 7)
        for date in starts:
            current = date + diff
            # print(current)
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

if __name__ == "__main__":
    ## EDITABLE

    start_date = dt.date(2025, 1, 13)
    end_date = dt.date(2025, 3, 28)

    start_dates = [
        
        dt.date(2025, 1, 17),
        ]

    breaks = [
        ]

    NAME = "Algebraic Geometry"
    TAG = "alggeo"
    YEAR = 2
    LEVEL = 7
    worksheet = "alg_geo_{PSET}.pdf"
    INSTITUTION = "King's Collage London"

    root = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\University\Undergraduate\Second Year"
    template_dir = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\Templates"
    lecture_temp = "Lecture Template.md"
    preamble_temp = "Preamble Template.md"
    homework_temp = "Homework Template.md"

    ## SET

    path = root + "\\" + NAME
    lec_path = path + "\\" + "Lectures"
    hw_path = path + "\\" + "Homework"
    ws_path = hw_path + "\\" + "Worksheets"
    textbook_path = path + "\\" + "Textbooks"

    

    mondays = start_date - dt.timedelta(days = start_date.weekday())

    nr_lecs = len([i for i in next_event(start_date, end_date, start_dates, breaks)])
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

    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    try:
        os.mkdir(lec_path)
    except FileExistsError:
        pass

    try:
        os.mkdir(hw_path)
    except FileExistsError:
        pass

    try:
        os.mkdir(ws_path)
    except FileExistsError:
        pass

    try:
        os.mkdir(textbook_path)
    except FileExistsError:
        pass

    with open(template_dir + "\\" + preamble_temp, mode="r", encoding="utf-8") as f:
        pre_template = f.read()

    preamble = pre_template.format(START_DATE=start_date, YEAR=YEAR, LEVEL=LEVEL,
                                   TAG=TAG, INSTITUTION=INSTITUTION)

    with open(path + "\\" + NAME + ".md", mode="w", encoding="utf-8") as f:
        f.write(preamble)

    with open(template_dir + "\\" + lecture_temp, mode="r", encoding="utf-8") as f:
        lec_template = f.read()

    for date in next_event(start_date, end_date, start_dates, breaks):
        DATE = f"{date.year:04d}-{date.month:02d}-{date.day:02d}"
        print(f"Lecture at {DATE}")
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

    with open(template_dir + "\\" + homework_temp, mode="r", encoding="utf-8") as f:
        hw_template = f.read()

    nr_hws = len([i for i in next_event(mondays, end_date, [mondays], breaks)])
    PSET = 1
    FIRST = "Homework 1"
    LAST = f"Homework {nr_hws}"

    PREV = ""
    TITLE = "Homework 1"
    NEXT = "Homework 2"

    PREFIX = (relativise(hw_path) + "\\").replace("\\", "/")
    PREFIX_P = ""
    PREFIX_N = PREFIX
    PREFIX_W = (relativise(ws_path) + "\\").replace("\\", "/")

    WORKSHEET = worksheet.format(PSET=PSET)
    for date in next_event(mondays, end_date, [mondays], breaks):
        DATE = f"{date.year:04d}-{date.month:02d}-{date.day:02d}"
        print(f"Homework at {DATE}")
        current = hw_template.format(FIRST=FIRST, LAST=LAST, PREV=PREV, NEXT=NEXT,
                                  TAG=TAG, DATE=DATE, PREFIX=PREFIX, SUB_DIR=NAME,
                                  PREFIX_N=PREFIX_N, PREFIX_P=PREFIX_P,
                                  PREFIX_S=PREFIX_S, PSET=PSET, PREFIX_W=PREFIX_W, WORKSHEET=WORKSHEET)

        with open(hw_path + "\\" + TITLE + ".md", mode="w+", encoding="utf-8") as f:
            f.write(current)
            
        PSET += 1
        PREV = TITLE
        TITLE = NEXT
        NEXT = f"Homework {PSET+1}"
        PREFIX_P = PREFIX
        WORKSHEET = worksheet.format(PSET=PSET)
        if PSET < nr_hws:
            NEXT = f"Homework {PSET+1}"
        else:
            NEXT = ""
            PREFIX_N = ""


    print("Remember to fill in data to the preamble")

