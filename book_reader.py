"""
book_reader.py
    Capabilities:
        Read a pdf book like an audiobook
    Limitations:

    Improvements:
        Check the naming adjustments in the documentation
"""

import pyttsx3
import PyPDF2

book = open('/home/renzo/Documents/organize_files_backup/learn_python.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(book)
pages = pdf_reader.numPages
print(pages)
bot = pyttsx3.init()

for num in range(0, pages):
    page = pdf_reader.getPage(0)
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()