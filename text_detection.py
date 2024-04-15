import os
import docx
import easyocr
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pdfminer.high_level import extract_text

reader = easyocr.Reader(['en', 'hi']) #language

def extract_text_from_pdf(pdf_file, output_file):
    text = extract_text(pdf_file)
    
    # extracted to text file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(text)
    print(f"Text extracted from {pdf_file} and saved to {output_file}")

def extract_text_from_doc(doc_file, output_file):
    doc = docx.Document(doc_file)
    
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(text)
    print(f"Text extracted from {doc_file} and saved to {output_file}")

def extract_text_from_image(image_file, output_file):
    result = reader.readtext(image_file)

    with open(output_file, 'w', encoding='utf-8') as text_file:
        for detection in result:
            text = detection[1]
            text_file.write(text + '\n')

    print(f"Text extracted from {image_file} and saved to {output_file}")

Tk().withdraw() 
file_path = askopenfilename() 
file_name, file_extension = os.path.splitext(file_path)

#file type 
if file_extension.lower() == '.pdf':
    output_file = file_name + '_extracted.txt'
    extract_text_from_pdf(file_path, output_file)
elif file_extension.lower() == '.docx':
    output_file = file_name + '_extracted.txt'
    extract_text_from_doc(file_path, output_file)
elif file_extension.lower() in ['.jpg', '.jpeg', '.png']:
    output_file = file_name + '_extracted.txt'
    extract_text_from_image(file_path, output_file)
else:
    print("Unsupported file format. Only PDF, DOCX, JPG, JPEG, and PNG files are supported.")

#extracted text
print("Extraction completed.")
