import os
import gmpy2
import PyPDF2 as pdf
from subject_gen import relativise
import json

## EDITABLE

textbook_path = r"C:\Users\fyggy\OneDrive\Documents\Textbooks\Personal\Topology\Topology - James Dugundji.pdf"
NAME = "Topology Dugundji"
TAG = "topo_dugundji"
LEVEL = 6
YEAR = 2

root = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\Textbooks\Undergraduate\Second Year"
template_dir = r"C:\Users\fyggy\OneDrive\Documents\Obsidian Valuts\MathsNotes\Templates"
preamble_temp = "Textbook Premable Template.md"
exercises_temp = "Exercises Template.md"

## SET

path = root + "\\" + NAME
ex_path = path + "\\" + "Exercises"


reader = pdf.PdfReader(textbook_path)
outline = reader.outline
print(outline)
for i in outline:
    print(i["/Title"])

