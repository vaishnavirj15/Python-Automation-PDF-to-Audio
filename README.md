PDF to Audio Converter
Overview:
This project is a PDF to Audio Converter that allows users to upload a PDF file, select a page, and convert the selected page into an audio file (MP3). The application uses Flask as the backend framework, PyMuPDF for PDF text extraction, pyttsx3 for text-to-speech conversion, and HTML, CSS, JavaScript for the front-end interface.
The project supports both OCR (Optical Character Recognition) for scanned PDFs and text-based PDFs, ensuring that users can convert text from both types of documents into an audio format.

Features:
PDF Upload: Users can upload a PDF file via a user-friendly interface.
Page Selection: After uploading, users can select a specific page from the PDF to convert to audio.
Text Extraction: The application extracts text from the selected PDF page using PyMuPDF. For scanned PDFs, OCR technology (via pytesseract) is used to convert images of text to actual text.
Audio Conversion: The extracted text is then converted into speech using pyttsx3 and saved as an audio file (MP3).
Audio Playback and Download: Once the audio is generated, users can listen to the audio directly from the browser and download it for offline use.

Technologies Used:
Backend:
Flask: Python web framework for building the application.
PyMuPDF: For extracting text from non-scanned PDFs.
Pytesseract: For OCR to extract text from scanned PDF pages.
pyttsx3: A Python text-to-speech library used to convert text to audio.
pdf2image: For converting scanned PDF pages into images.
Frontend:
HTML: Markup language used to structure the web page.
CSS: Styling for a visually appealing user interface.
JavaScript: Used for handling form submissions, displaying audio player, and managing dynamic content.
