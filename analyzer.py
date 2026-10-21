from skill_extractor import extract_skills, categorize_skills
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(cv_text, job_description):
    """
    Calculate text similarity using TF-IDF and cosine similarity.
    """

    documents = [cv_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    return round(float(similarity[0][0]) * 100, 2)


def analyze_skill_gap(cv_text, job_description):
    """
    Compare CV skills with job skills and calculate
    both text similarity and skill-match percentage.
    """

    cv_skills = set(extract_skills(cv_text))
    required_skills = set(extract_skills(job_description))

    matching_skills = cv_skills.intersection(required_skills)
    missing_skills = required_skills - cv_skills

    cv_skills_by_category = categorize_skills(cv_skills)
    required_skills_by_category = categorize_skills(required_skills)

    # Calculate text similarity
    similarity_score = calculate_similarity(
        cv_text,
        job_description
    )

    # Calculate skill match percentage
    if len(required_skills) > 0:
        skill_match_score = (
            len(matching_skills) / len(required_skills)
        ) * 100
    else:
        skill_match_score = 0

    return {
        "cv_skills": sorted(cv_skills),
        "required_skills": sorted(required_skills),
        "matching_skills": sorted(matching_skills),
        "missing_skills": sorted(missing_skills),
        "similarity_score": round(similarity_score, 2),
        "skill_match_score": round(skill_match_score, 2),
        "cv_skills_by_category": cv_skills_by_category,
        "required_skills_by_category": required_skills_by_category,
    }