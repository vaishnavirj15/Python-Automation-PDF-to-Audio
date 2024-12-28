# PDF to Audio Converter

This project is a Flask-based application that converts PDF pages into audio files (MP3). Users can upload a PDF, select a specific page, and generate an audio file from the text on that page. The application supports both text-based PDFs and scanned PDFs using OCR (Optical Character Recognition), making it versatile and user-friendly. 

---

## Features

**PDF Upload**: Users can upload a PDF file via a clean and intuitive interface.
**Page Selection**: After uploading, users can select a specific page to convert to audio.
**Text Extraction**: 
  - Extracts text from text-based PDFs using **PyMuPDF**.
  - For scanned PDFs, uses OCR (via **pytesseract**) to extract text from images.
**Audio Conversion**: Converts the extracted text into audio using **pyttsx3** and saves it as an MP3 file.
  **Audio Playback and Download**: Users can:
  - Listen to the audio directly in the browser.
  - Download the audio file for offline use.

---

## Technologies Used

### **Backend**
- **Flask**: Python web framework for application development.
- **PyMuPDF**: Extracts text from text-based PDFs.
- **pytesseract**: OCR technology for scanned PDFs.
- **pyttsx3**: Converts extracted text to audio.
- **pdf2image**: Converts scanned PDF pages into images.

### **Frontend**
- **HTML**: Structures the web page.
- **CSS**: Styles the application for a visually appealing interface.
- **JavaScript**: Manages form submissions, displays the audio player, and handles dynamic content.

---

## Setup Instructions

### **Pre-requisites**
- Python 3.7 or higher.
- Install Tesseract OCR for scanned PDF support.  
  - For Windows: [Download Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
  - For Linux/MacOS: Install via package manager (`sudo apt install tesseract-ocr` or equivalent).

---

### **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/pdf-to-audio-converter.git
   cd pdf-to-audio-converter
2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Set up Tesseract OCR**:
   - **Ensure Tesseract is installed and accessible in your system's PATH**.
   - **Update the Tesseract command path in the Python script if necessary**.
4. **Prepare the application**:
   -- **Place the Flask application code in app.py**.
---


### **Running the Application**

1. **Start the Flask server**:
   ```bash
   python app.py
2. **Access the application**:
   - **Click on the localhost link generated or go to browser and open: http://127.0.0.1:5000/**.
---


### **Deployment on GitHub**

1. **Host the repository**:
   - **Push the project to GitHub for version control and collaboration**.
2. **Deploy Online**:
   - **Use a platform like Heroku, Streamlit Cloud, or PythonAnywhere for hosting**.
---


### **Usage Instructions**
**Upload a PDF**: Use the web interface to upload a PDF file.
**Select a Page**: Choose the page number you want to convert.
**Generate Audio**:The application extracts text and converts it into an MP3 file.
Listen to the audio in the browser or download it for offline use.
---

## **Notes**
**Ensure the PDF file is either text-based or scanned (OCR-compatible)**.
**Configure Tesseract for optimal OCR performance if dealing with scanned PDFs**.
**Modify the frontend code in templates or static folders for custom UI changes**.
---

# **Acknowledgements**
This project uses the following libraries:

**Flask**
**PyMuPDF**
**pytesseract**
**pyttsx3**
**pdf2image**


### Key Highlights:
1. **Clear Setup Instructions**: Explains pre-requisites, installation, and running the app locally or deploying it online.
2. **Detailed Features Section**: Breaks down functionality for clarity.
3. **Tech Stack Breakdown**: Separates backend and frontend tools for better understanding.

Replace `https://github.com/your-username/pdf-to-audio-converter.git` with the actual GitHub URL. Let me know if you need further refinements!





