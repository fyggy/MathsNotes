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

## SET

textbook_name = textbook_path.split("\\")[-1]
path = root + "\\" + NAME
ex_path = path + "\\" + "Exercises"

def traverse(outline, targets, depth=0):
    ret = depth in targets
    for i in outline:
        #print(type(i))
        if type(i) == pdf.generic._data_structures.Destination:
            if ret:
                yield i["/Title"]
        elif type(i) == list:
            for j in traverse(i, targets, depth=depth+1):
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
                               TEXTBOOK=path+"\\"+textbook_name)

reader = pdf.PdfReader(textbook_path)
outline = reader.outline

for i in traverse(outline, contents_depths):
    pass
    

