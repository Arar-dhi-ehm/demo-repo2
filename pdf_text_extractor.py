"""
pdf_text_extractor.py
    Capabilities:
        Convert pdf to text
    Limitations:
        No idea yet if how many pages it can extract
        It might not be always accurate if there are image or tables and etc.
    Improvements:
        Add a button to copy the converted text
            - Alert: Copied to clipboard.
        Add a vertical scroll bar [done]
        Add a progress bar using tkinter
        Save as .txt
            - Add Save button
    Prerequisite:
        Install pypdf2 package
"""
import PyPDF2
import tkinter
from tkinter import filedialog

# This is the window widget (container)
window = tkinter.Tk()
window.title('PDF Text Extractor')

def open_file():
    # This will store the name of the file that will be opened
    filename = filedialog.askopenfilename(
        title='Open PDF File',
        # Will open a file dialogue in this directory
        initialdir='/home/renzo/Documents/automation_scripts/automation_project/extract_pdf_text',
        # It will show any(*) files that ends with .pdf
        filetypes=[('PDF files', '*.pdf')])
    print(filename)

    # Make the label name the same with file name uploaded
    file_name_label.configure(text=filename)
    # Clear the output file text before extraction. 1.0 means from the start.
    output_file_text.delete('1.0', tkinter.END)
    # Reader Object
    reader = PyPDF2.PdfReader(filename)
    # Extract text from pdf using for loop and show it in the terminal
    for page_number in range(len(reader.pages)):
        # Get page 1, 2, 3, and so on.
        current_text = reader.pages[page_number].extract_text()
        # To print in the terminal
        # print(current_text)
        # To print on tkinter window. It will print at the end of the printed line because of (END)
        output_file_text.insert(tkinter.END, current_text)


file_name_label = tkinter.Label(window, text='No file selected')
# Name of text widget
output_file_text = tkinter.Text(window)
open_file_text = tkinter.Button(window, text='Open PDF File', command=open_file)

# Right Scrollbar
scrollbar_tasks = tkinter.Scrollbar(window)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
output_file_text.config(yscrollcommand=scrollbar_tasks.set, border=5)
scrollbar_tasks.config(command=output_file_text.yview)

# To show in the popup
file_name_label.pack(fill='x', padx=20, pady=3)
output_file_text.pack(fill='x', padx=20, pady=3)
open_file_text.pack(fill='x', padx=20, pady=3)

# This will create an infinite loop of the app
window.mainloop()