import re
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import pdfplumber
import black
import tabula
import PyMuPDF
from PyMuPDF import PdfFileReader
from tkinter.scrolledtext import ScrolledText

class PDFCodeExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Python Code Extractor")
        self.root.geometry("600x400")

        self.open_button = ttk.Button(self.root, text="Open PDF", command=self.open_file_dialog)
        self.open_button.pack(pady=20)

        self.preview_text = ScrolledText(self.root, wrap=tk.WORD, width=60, height=15)
        self.preview_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            try:
                text = self.extract_text_from_pdf(file_path)
                chat_logs, python_code = self.separate_chat_logs_and_code(text)
                formatted_code = self.format_python_code("\n".join(python_code))
                tables = self.extract_tables_from_pdf(file_path)
                parsed_tables = self.parse_table_data(tables)
                self.preview_text.delete(1.0, tk.END)
                self.preview_text.insert(tk.END, formatted_code)
                self.save_file_dialog(formatted_code, parsed_tables)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def extract_text_from_pdf(self, file_path):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text

    def separate_chat_logs_and_code(self, text):
        chat_logs = []
        python_code = []
        lines = text.split("\n")
        for line in lines:
            if re.match(r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2} - .*", line):
                chat_logs.append(line)
            elif re.match(r"\s*#.*", line):
                python_code.append(line)
        return chat_logs, python_code

    def format_python_code(self, code):
        formatted_code = black.format_str(code, mode=black.FileMode())
        return formatted_code

    def extract_tables_from_pdf(self, file_path):
        tables = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_tables = page.extract_tables()
                if page_tables:
                    tables.extend(page_tables)
        return tables

    def parse_table_data(self, tables):
        parsed_data = []
        for table in tables:
            parsed_data.append(table.df.to_dict())
        return parsed_data

    def save_file_dialog(self, code, tables):
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(code)
            messagebox.showinfo("Save Successful", "Python code saved successfully.")
            if tables:
                table_file_path = file_path.replace(".py", "_tables.csv")
                df = pd.DataFrame(tables)
                df.to_csv(table_file_path, index=False)
                messagebox.showinfo("Table Data Saved", "Table data saved as CSV.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFCodeExtractorApp(root)
    root.mainloop()
