import streamlit as st

from pdf_reader import extract_text_from_pdf
from analyzer import analyze_skill_gap
from suggestions import generate_suggestions


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="CV Skill Gap Analyzer",
    page_icon="📄",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("📄 CV Enhancement & Skill-Gap Analyzer")

st.write(
    "Upload your CV in PDF format and paste a job description "
    "to analyze your skills, identify skill gaps, and improve your CV."
)


# --------------------------------------------------
# Upload CV
# --------------------------------------------------
uploaded_cv = st.file_uploader(
    "📎 Upload your CV (PDF)",
    type=["pdf"]
)


# --------------------------------------------------
# Job Description
# --------------------------------------------------
job_description = st.text_area(
    "💼 Paste the Job Description",
    height=250,
    placeholder="Paste the job description here..."
)


# --------------------------------------------------
# Analyze Button
# --------------------------------------------------
if st.button("🔍 Analyze CV"):

    if uploaded_cv is None:

        st.warning("⚠️ Please upload your CV PDF.")

    elif not job_description.strip():

        st.warning("⚠️ Please enter a job description.")

    else:

        # --------------------------------------------------
        # Extract CV Text
        # --------------------------------------------------
        cv_text = extract_text_from_pdf(uploaded_cv)

        if not cv_text.strip():

            st.error(
                "❌ Could not extract text from this PDF. "
                "Please upload a text-based CV PDF."
            )

        else:

            # --------------------------------------------------
            # Show Extracted Text
            # --------------------------------------------------
            st.subheader("🔍 Extracted CV Text")

            st.text_area(
                "Text extracted from your PDF:",
                cv_text,
                height=250
            )


            # --------------------------------------------------
            # Analyze
            # --------------------------------------------------
            result = analyze_skill_gap(
                cv_text,
                job_description
            )

            st.success(
                "✅ CV analysis completed successfully!"
            )


            # --------------------------------------------------
            # CV-Job Analysis
            # --------------------------------------------------
            st.subheader("📊 CV–Job Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "📄 Text Similarity",
                    f'{result["similarity_score"]}%'
                )

                st.progress(
                    result["similarity_score"] / 100
                )

            with col2:

                st.metric(
                    "🎯 Skill Match",
                    f'{result["skill_match_score"]}%'
                )

                st.progress(
                    result["skill_match_score"] / 100
                )


            # --------------------------------------------------
            # Matching + Missing Skills
            # --------------------------------------------------
            st.subheader("🎯 Skill Comparison")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("✅ Matching Skills")

                if result["matching_skills"]:

                    for skill in result["matching_skills"]:
                        st.write(f"✅ {skill}")

                else:

                    st.write(
                        "No matching skills found."
                    )


            with col2:

                st.subheader("❌ Missing Skills")

                if result["missing_skills"]:

                    for skill in result["missing_skills"]:
                        st.write(f"❌ {skill}")

                else:

                    st.write(
                        "No missing skills found!"
                    )


            # --------------------------------------------------
            # Categorized CV Skills
            # --------------------------------------------------
            st.subheader("🧑‍💻 Skills Found in Your CV")

            cv_categories = result[
                "cv_skills_by_category"
            ]

            if cv_categories:

                for category, skills in cv_categories.items():

                    st.markdown(
                        f"### {category}"
                    )

                    st.write(
                        ", ".join(skills)
                    )

            else:

                st.write(
                    "No recognized skills found."
                )


            # --------------------------------------------------
            # Categorized Required Skills
            # --------------------------------------------------
            st.subheader(
                "💼 Skills Required by the Job"
            )

            required_categories = result[
                "required_skills_by_category"
            ]

            if required_categories:

                for category, skills in required_categories.items():

                    st.markdown(
                        f"### {category}"
                    )

                    st.write(
                        ", ".join(skills)
                    )

            else:

                st.write(
                    "No recognized skills found."
                )


            # --------------------------------------------------
            # CV Enhancement Suggestions
            # --------------------------------------------------
            st.subheader(
                "💡 CV Enhancement Suggestions"
            )

            suggestions = generate_suggestions(
                result["missing_skills"],
                cv_text
            )

            if suggestions:

                for suggestion in suggestions:

                    st.write(
                        f"💡 {suggestion}"
                    )

            else:

                st.write(
                    "✅ Your CV looks well aligned "
                    "with the selected job."
                )