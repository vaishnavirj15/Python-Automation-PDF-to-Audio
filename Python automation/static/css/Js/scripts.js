document.getElementById('pdfForm').onsubmit = function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    
    fetch('/upload_pdf', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('extractButton').style.display = 'inline'; // Show extract button
        }
    })
    .catch(error => console.error('Error:', error));
};

function extractText() {
    const pageNumber = prompt("Enter the page number to convert to audio:");
    if (pageNumber) {
        fetch('/extract_text_and_convert', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ page_number: pageNumber })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('audioSource').src
            }
        }
    )
}
}
