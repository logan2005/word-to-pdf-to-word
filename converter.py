import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
from docx2pdf import convert

def pdf_to_word():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
        if save_path:
            cv = Converter(file_path)
            cv.convert(save_path, start=0, end=None)
            cv.close()
            messagebox.showinfo("Success", f"Converted PDF to Word:\n{save_path}")
        else:
            messagebox.showwarning("Save Cancelled", "No save location provided.")
    else:
        messagebox.showwarning("Open Cancelled", "No file selected.")

def word_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if file_path:
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if save_path:
            convert(file_path, save_path)
            messagebox.showinfo("Success", f"Converted Word to PDF:\n{save_path}")
        else:
            messagebox.showwarning("Save Cancelled", "No save location provided.")
    else:
        messagebox.showwarning("Open Cancelled", "No file selected.")

app = tk.Tk()
app.title("PDF to Word & Word to PDF Converter")
app.geometry("300x150")

btn_pdf_to_word = tk.Button(app, text="Convert PDF to Word", command=pdf_to_word, width=25, height=2)
btn_pdf_to_word.pack(pady=10)

btn_word_to_pdf = tk.Button(app, text="Convert Word to PDF", command=word_to_pdf, width=25, height=2)
btn_word_to_pdf.pack(pady=10)

app.mainloop()
