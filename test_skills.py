from skill_extractor import extract_skills


text = """
I am a Python developer with experience in
Machine Learning, Pandas, SQL, Git, Streamlit,
and TensorFlow.
"""


skills = extract_skills(text)

print("Skills found:")

for skill in skills:
    print("-", skill)