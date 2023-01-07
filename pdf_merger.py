"""
pdf_merger.py
    Capabilities:

    Limitations:

    Improvements:

    Prerequisite:
        Install pypdf2 package
"""

import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

# Save in the current directory
for file in os.listdir(os.curdir):
    if file.endswith('.pdf'):
        merger.append(file)
    merger.write('combined_pdf_docs.pdf')