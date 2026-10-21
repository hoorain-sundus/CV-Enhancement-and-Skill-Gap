def generate_suggestions(missing_skills, cv_text):
    """
    Generate CV improvement suggestions based on missing skills
    and the existing CV text.
    """

    suggestions = []

    # Suggestions based on missing skills
    for skill in missing_skills:
        suggestions.append(
            f"Consider adding relevant experience, projects, or "
            f"coursework related to {skill} if you have experience with it."
        )

    # General CV suggestions
    if len(cv_text.split()) < 100:
        suggestions.append(
            "Your CV contains relatively little text. Consider adding "
            "relevant projects, achievements, certifications, or experience."
        )

    if "project" not in cv_text.lower():
        suggestions.append(
            "Consider adding a Projects section describing practical "
            "work you have completed."
        )

    if "achievement" not in cv_text.lower():
        suggestions.append(
            "Consider highlighting specific achievements or measurable "
            "results instead of only listing responsibilities."
        )

    if "objective" in cv_text.lower():
        suggestions.append(
            "Consider keeping your career objective concise and "
            "tailoring it to the specific job you're applying for."
        )

    return suggestions