import PyPDF2
import re
import tabula
import subprocess
import autopep8
import tkinter as tk
from tkinter import filedialog, messagebox
import pdfminer
import pandas as pd

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = pdfminer.PDFParser(file)
        doc = pdfminer.PDFDocument()
        reader.set_document(doc)
        doc.set_parser(reader)
        doc.initialize()
        for page in doc.get_pages():
            text += page.extract_text()
    return text

def separate_chat_logs_and_code(text):
    chat_logs = []
    python_code = []
    lines = text.split("\n")
    for line in lines:
        if re.match(r"\d2/\d2/\d4 \d2:\d2:\d2 - .*", line):
            chat_logs.append(line)
        elif re.match(r"\s*#.*", line):
            python_code.append(line)
    return chat_logs, python_code

def extract_python_code(text):
    python_code = []
    lines = text.split("\n")
    for line in lines:
        if re.match(r"\s*#.*", line):
            python_code.append(line)
    return python_code

def format_python_code(code):
    formatted_code = autopep8.fix_code(code)
    return formatted_code

def extract_tables_from_pdf(file_path):
    tables = tabula.read_pdf(file_path, pages="all", lattice=True, pandas_options={"header": None})
    return tables

def parse_table_data(tables):
    parsed_data = []
    for table in tables:
        parsed_data.append(table.to_dict(orient="records"))
    return parsed_data

def run_custom_script(file_path):
    subprocess.run(["python", "custom_script.py", file_path])

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        text = extract_text_from_pdf(file_path)
        chat_logs, python_code = separate_chat_logs_and_code(text)
        formatted_code = format_python_code("\n".join(python_code))
        save_file_dialog(formatted_code)

def save_file_dialog(code):
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(code)
        messagebox.showinfo("Save Successful", "Python code saved successfully.")

def main():
    root = tk.Tk()
    root.title("PDF Python Code Extractor")
    root.geometry("400x200")

    open_button = tk.Button(root, text="Open PDF", command=open_file_dialog)
    open_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
