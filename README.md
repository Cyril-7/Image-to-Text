---

# Text Extraction Tool

This Python script extracts text from PDF, DOCX, and image files (JPG, JPEG, PNG). It utilizes libraries like `pdfminer`, `docx`, and `easyocr` for text extraction. The extracted text is then saved to a text file.

## Usage

1. **Installation**:
   - Make sure you have Python installed on your system.
   - Install the required libraries using pip:
     ```
     pip install pdfminer.six docx easyocr
     ```

2. **Running the Script**:
   - Run the script `text_extraction.py`.
   - You will be prompted to select a file using a file dialog.
   - Supported file formats: PDF, DOCX, JPG, JPEG, PNG.

3. **Output**:
   - The extracted text will be saved to a text file with the same name as the input file but with `_extracted.txt` appended.

## Libraries Used

- **pdfminer**: For extracting text from PDF files.
- **docx**: For extracting text from DOCX files.
- **easyocr**: For extracting text from image files.

## File Structure

- `text_extraction.py`: The main Python script.
- `README.md`: This file, providing information about the script.
- Other files: Any PDF, DOCX, or image files you want to extract text from.

## Notes

- Make sure to install the necessary libraries before running the script.
- This script may not perfectly extract text from complex documents or images with poor quality.
- For more complex requirements or specific use cases, consider extending or modifying the script accordingly.

---
