from pdf_reader import extract_text_from_pdf


with open("sample_cv.pdf", "rb") as file:
    text = extract_text_from_pdf(file)

print("----- CV TEXT -----")
print(text)