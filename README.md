PDF to Word & Word to PDF Converter
This Python program provides a simple graphical user interface (GUI) for converting PDF files to Word documents and vice versa. The application uses the pdf2docx library to convert PDF files to Word documents and the docx2pdf library to convert Word documents to PDF files.

Features
Convert PDF files to Word documents (.docx)
Convert Word documents (.docx) to PDF files
Requirements
  Python 3.x
  tkinter (usually included with Python)
  pdf2docx
  docx2pdf
  
Installation
Clone the repository:

sh
Copy code
(https://github.com/logan2005/word-to-pdf-to-word.git)
cd pdf-word-converter
Install the required Python packages:


pip install pdf2docx docx2pdf

Usage
Run the program:


python converter.py

Click the "Convert PDF to Word" button to convert a PDF file to a Word document:

Select the PDF file you want to convert.
Choose the save location and filename for the Word document.
Click the "Convert Word to PDF" button to convert a Word document to a PDF file:

Select the Word document you want to convert.
Choose the save location and filename for the PDF file.
Files
converter.py: The main Python script that runs the application.
README.md: This readme file.
Example
Below is an example of how to use the application:

Run the script:

sh
Copy code
python converter.py
The GUI window will appear:


Click the desired button to convert files and follow the prompts.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
pdf2docx for PDF to Word conversion.
docx2pdf for Word to PDF conversion.
