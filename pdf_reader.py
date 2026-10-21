import pymupdf


def extract_text_from_pdf(pdf_file):
    """Extract all text from an uploaded PDF file."""
    
    text = ""

    pdf = pymupdf.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text