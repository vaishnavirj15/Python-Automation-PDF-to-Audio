from flask import Flask, render_template, request, send_from_directory
import os
import PyPDF2
import pyttsx3
import pytesseract
from pdf2image import convert_from_path
import fitz  # PyMuPDF

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = 'audio_files'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

def extract_text_from_pdf(pdf_path, page_number):
    try:
        # Try using PyMuPDF for better text extraction
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_number - 1)  # Page numbering starts from 0
        page_content = page.get_text("text")
        return page_content
    except Exception as e:
        print(f"Error extracting text with PyMuPDF: {e}")
        return None

def extract_text_from_scanned_pdf(pdf_path, page_number):
    try:
        # Convert the page to an image
        images = convert_from_path(pdf_path, first_page=page_number, last_page=page_number)
        image = images[0]
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error extracting text from scanned page: {e}")
        return None

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return 'No file part', 400
    file = request.files['pdf_file']
    if file.filename == '':
        return 'No selected file', 400

    if file and file.filename.endswith('.pdf'):
        pdf_filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(pdf_filename)
        return render_template('index.html', pdf_filename=file.filename)

    return 'Invalid file type, please upload a PDF.', 400

@app.route('/convert/<filename>', methods=['POST'])
def convert_to_audio(filename):
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    page_number = int(request.form['page_number'])

    # Try extracting text from the PDF
    page_content = extract_text_from_pdf(pdf_path, page_number)
    
    if not page_content:
        # If text extraction fails, try OCR for scanned PDFs
        page_content = extract_text_from_scanned_pdf(pdf_path, page_number)

    if not page_content:
        return "Unable to extract text from the PDF.", 400

    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # Speech rate
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    # Generate audio file
    audio_path = os.path.join(app.config['AUDIO_FOLDER'], f'{filename}_audio.mp3')
    engine.save_to_file(page_content, audio_path)
    engine.runAndWait()

    return render_template('index.html', audio_path=audio_path)

@app.route('/audio/<filename>')
def play_audio(filename):
    return send_from_directory(app.config['AUDIO_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(AUDIO_FOLDER):
        os.makedirs(AUDIO_FOLDER)
    app.run(debug=True)


