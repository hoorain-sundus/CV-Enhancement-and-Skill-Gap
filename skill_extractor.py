import spacy
from spacy.matcher import PhraseMatcher


# --------------------------------------------------
# Load spaCy model
# --------------------------------------------------
nlp = spacy.load("en_core_web_sm")


# --------------------------------------------------
# Skill dictionary
# --------------------------------------------------
SKILL_CATEGORIES = {
    "Programming": [
        "python",
        "java",
        "c++",
        "javascript",
    ],

    "Web Development": [
        "html",
        "css",
        "react",
        "react.js",
        "node.js",
        "express",
    ],

    "Databases": [
        "mongodb",
        "sql",
        "mysql",
    ],

    "AI & Machine Learning": [
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data science",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
    ],

    "Tools": [
        "streamlit",
        "git",
        "github",
        "docker",
        "aws",
        "azure",
        "power bi",
    ],

    "Soft Skills": [
        "teamwork and collaboration",
        "communication skills",
        "time management",
        "leadership",
        "problem solving",
        "problem-solving",
        "critical thinking",
        "adaptability",
        "creativity",
        "organization",
        "organizational skills",
        "interpersonal skills",
    ],
}


# --------------------------------------------------
# Create canonical skill list
# --------------------------------------------------
SKILLS = []

for skills in SKILL_CATEGORIES.values():
    SKILLS.extend(skills)


# --------------------------------------------------
# Skill aliases
# --------------------------------------------------
SKILL_ALIASES = {
    "communication skills": "communication",
    "teamwork and collaboration": "teamwork & collaboration",
    "time management": "time management",
    "problem-solving": "problem solving",
}


# --------------------------------------------------
# Create PhraseMatcher
# --------------------------------------------------
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

patterns = [
    nlp.make_doc(skill)
    for skill in SKILLS
]

matcher.add("SKILLS", patterns)


# --------------------------------------------------
# Extract skills
# --------------------------------------------------
def extract_skills(text):
    """
    Extract skills using spaCy PhraseMatcher.

    Longer phrases are preferred over shorter overlapping
    phrases.
    """

    doc = nlp(text)

    matches = matcher(doc)

    found_matches = []

    for match_id, start, end in matches:

        skill = doc[start:end].text.lower()

        found_matches.append({
            "skill": skill,
            "start": start,
            "end": end
        })

    # Longer phrases first
    found_matches.sort(
        key=lambda item: item["end"] - item["start"],
        reverse=True
    )

    selected = []

    for match in found_matches:

        overlaps = False

        for existing in selected:

            if not (
                match["end"] <= existing["start"]
                or match["start"] >= existing["end"]
            ):
                overlaps = True
                break

        if not overlaps:
            selected.append(match)

    # Apply aliases
    final_skills = []

    for item in selected:

        skill = item["skill"]

        if skill in SKILL_ALIASES:
            skill = SKILL_ALIASES[skill]

        final_skills.append(skill)

    return sorted(set(final_skills))


def categorize_skills(skills):
    """
    Organize extracted skills into their categories.
    """

    categorized = {}

    for category, category_skills in SKILL_CATEGORIES.items():

        matched = []

        for skill in skills:

            # Check whether skill belongs to this category
            canonical_skills = []

            for original_skill in category_skills:

                canonical_skill = SKILL_ALIASES.get(
                    original_skill,
                    original_skill
                )

                canonical_skills.append(canonical_skill)

            if skill in canonical_skills:
                matched.append(skill)

        if matched:
            categorized[category] = sorted(set(matched))

    return categorized