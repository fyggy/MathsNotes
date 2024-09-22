import os
import gmpy2
import PyPDF2 as pdf
from subject_gen import relativise
from datetime import date
import shutil

## EDITABLE

textbook_path = r"C:\Users\fyggy\OneDrive\Documents\Textbooks\Personal\Topology\Topology - James Dugundji.pdf"
NAME = "Topology Dugundji"
TAG = "topo_dugundji"
LEVEL = 6
YEAR = 2

root = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\Textbooks\Undergraduate\Second Year"
template_dir = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\Templates"
preamble_temp = "Textbook Preamble Template.md"
exercises_temp = "Exercises Template.md"

# 0 is top level, 1 is one level down, etc. list multiple if on both level 1 and 3, but not
# 2, etc
contents_depths = [1]

number_prefixes = True
exclude_list = ["Problems"]

## SET

textbook_name = textbook_path.split("\\")[-1]
path = root + "\\" + NAME
ex_path = path + "\\" + "Exercises"
TEXTBOOK = relativise(path+"\\"+textbook_name).replace("\\", "/")

def traverse(outline, targets, exclude=[""], depth=0):
    ret = depth in targets
    for i in outline:
        #print(type(i))
        if type(i) == pdf.generic._data_structures.Destination:
            if ret:
                chk = i["/Title"]
                if not any(substring in chk for substring in exclude):
                    yield chk
        elif type(i) == list:
            for j in traverse(i, targets, exclude=exclude, depth=depth+1):
                yield j
        

try:
    os.mkdir(path)
except FileExistsError:
    pass

try:
    os.mkdir(ex_path)
except FileExistsError:
    pass

shutil.copy2(textbook_path, path)

with open(template_dir + "\\" + preamble_temp, mode="r", encoding="utf-8") as f:
    pre_template = f.read()

preamble = pre_template.format(DATE=str(date.today()), YEAR=YEAR, LEVEL=LEVEL, TAG=TAG,
                               TEXTBOOK=TEXTBOOK, NAME=NAME)

with open(path + "\\" + NAME + ".md", mode="w", encoding="utf-8") as f:
    f.write(preamble)

with open(template_dir + "\\" + exercises_temp, mode="r", encoding="utf-8") as f:
    ex_template = f.read()

reader = pdf.PdfReader(textbook_path)
outline = reader.outline

contents = [i for i in traverse(outline, contents_depths, exclude=exclude_list)]
nr_exercises = len(contents)
if number_prefixes:
    FIRST = "1. " + contents[0]
    
    LAST = f"{nr_exercises}. " + contents[-1]
else:
    FIRST = contents[0]
    LAST = contents[-1]

COUNT = 1
PREV = ""
TITLE = FIRST

PREFIX = (relativise(ex_path) + "\\").replace("\\", "/")
PREFIX_P = ""
PREFIX_N = PREFIX
PREFIX_S = (relativise(path) + "\\").replace("\\", "/")

for i in range(len(contents)):
    print(TITLE)
    if number_prefixes:
        try:
            NEXT = str(COUNT + 1) + ". " + contents[i+1]
        except IndexError:
            NEXT = ""
            PREFIX_N = PREFIX
    else:
        try:
            NEXT = contents[i+1]
        except IndexError:
            NEXT = ""
            PREFIX_N = PREFIX

    current = ex_template.format(FIRST=FIRST, LAST=LAST, PREV=PREV, NEXT=NEXT,
                                  TAG=TAG, PREFIX=PREFIX, SUB_DIR=NAME,
                                  PREFIX_N=PREFIX_N, PREFIX_P=PREFIX_P,
                                  PREFIX_S=PREFIX_S, COUNT=COUNT)
    with open(ex_path + "\\" + TITLE + ".md", mode="w+", encoding="utf-8") as f:
        f.write(current)
    PREV = TITLE
    TITLE = NEXT
    COUNT += 1
    
    

