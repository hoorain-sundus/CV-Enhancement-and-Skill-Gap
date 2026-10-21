from pdf_reader import extract_text_from_pdf
from skill_extractor import extract_skills


with open("sample_cv.pdf", "rb") as file:
    cv_text = extract_text_from_pdf(file)


print("========== EXTRACTED CV TEXT ==========")
print(cv_text)

print("\n========== EXTRACTED CV SKILLS ==========")

skills = extract_skills(cv_text)

for skill in skills:
    print("-", skill)