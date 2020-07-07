import fitz
import re
import os 

file_name = "KSG 10000 Volume 1 UPSC CSE Prelims 2020.pdf"

doc = fitz.open(file_name)

with open('out.txt','w+',encoding='utf-8') as out:
    for page in doc:
        print(f"writing {page} to out")
        out.write(page.getText())
    out.close() 