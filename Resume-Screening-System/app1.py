import pandas as pd
import streamlit as st

from src.preprocess import clean_text
from src.skill_extractor import extract_skills
from src.scorer import similarity_scores
from src.gap_analysis import missing_skills
from src.ranker import rank_candidates
st.set_page_config(
    page_title="AI Resume Screening System",
    layout="wide"
)
st.title("AI Resume Screening System")
st.markdown(
    """
    Automatically screen, score, and rank resumes
    based on job requirements.
    """
)
job_role = st.selectbox(
    "Select Job Role",
    [
        "Data Scientist",
        "Python Developer",
        "Data Analyst"
    ]
)
job_descriptions = {

    "Data Scientist":
    """
    Looking for a Data Scientist with strong skills in
    Python, SQL, Machine Learning, Deep Learning,
    NLP, TensorFlow, Pandas, NumPy, AWS,
    and Data Analysis.
    """,

    "Python Developer":
    """
    Looking for a Python Developer with strong
    knowledge of Python, Django, Flask, SQL,
    REST APIs, Git, AWS and backend development.
    """,

    "Data Analyst":
    """
    Looking for a Data Analyst with experience in
    SQL, Excel, Power BI, Tableau, Python,
    Data Visualization and Reporting.
    """
}

job_description = job_descriptions[job_role]
st.subheader(" Selected Job Description")
st.info(job_description)
if st.button(" Screen Candidates"):

    try:

        df = pd.read_csv("data/Resume.csv")

        df = df.dropna(subset=["Resume_str"])

        df["clean_resume"] = df["Resume_str"].apply(
            clean_text
        )

        clean_job = clean_text(
            job_description
        )

        scores = similarity_scores(
            clean_job,
            df["clean_resume"].tolist()
        )

        df["Similarity"] = scores * 100
        job_skills = extract_skills(
            clean_job
        )

        df["Skills"] = df[
            "clean_resume"
        ].apply(extract_skills)
        df["Skill_Match"] = df["Skills"].apply(

            lambda skills:

            (
                len(
                    set(skills).intersection(
                        job_skills
                    )
                )
                /
                max(len(job_skills), 1)
            )

            * 100

        )

        df["Missing_Skills"] = df[
            "Skills"
        ].apply(

            lambda skills:

            missing_skills(
                job_skills,
                skills
            )
        )

        df["Final_Score"] = (

            0.4 * df["Similarity"]

            +

            0.6 * df["Skill_Match"]

        )

        df = df[
            df["Skill_Match"] > 0
        ]

        ranked = rank_candidates(df)

        st.subheader("Dashboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Resumes",
                len(pd.read_csv("data/Resume.csv"))
            )

        with col2:
            st.metric(
                "Matching Candidates",
                len(ranked)
            )

        with col3:
            st.metric(
                "Required Skills",
                len(job_skills)
            )

        st.subheader(
            "Top 10 Ranked Candidates"
        )

        st.dataframe(

            ranked.head(10)[
                [
                    "ID",
                    "Category",
                    "Final_Score",
                    "Similarity",
                    "Skill_Match",
                    "Missing_Skills"
                ]
            ],

            use_container_width=True

        )


        st.subheader(
            "Complete Ranking"
        )

        st.dataframe(

            ranked[
                [
                    "ID",
                    "Category",
                    "Final_Score",
                    "Similarity",
                    "Skill_Match",
                    "Missing_Skills"
                ]
            ],

            use_container_width=True

        )

        ranked.to_csv(
            "ranked_candidates.csv",
            index=False
        )

        st.success(
            "Candidate ranking completed successfully!"
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )