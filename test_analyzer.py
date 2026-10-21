from analyzer import analyze_skill_gap


cv_text = """
I am a Python developer with experience in Python,
SQL, Pandas, Machine Learning, Streamlit and Git.
"""


job_description = """
We are looking for a developer with experience in
Python, SQL, Machine Learning, TensorFlow, Docker
and Git.
"""


result = analyze_skill_gap(cv_text, job_description)


print("CV Skills:")
print(result["cv_skills"])

print("\nRequired Skills:")
print(result["required_skills"])

print("\nMatching Skills:")
print(result["matching_skills"])

print("\nMissing Skills:")
print(result["missing_skills"])

print("\nCV-Job Similarity:")
print(f'{result["similarity_score"]}%')