#AI Resume Screening System
Overview

The AI Resume Screening System is an NLP-powered recruitment tool that automatically screens, scores, and ranks resumes based on a selected job role.

The system helps recruiters and hiring teams reduce manual effort by comparing resume content against job requirements, identifying relevant skills, calculating similarity scores, and highlighting missing skills.

##Features
Resume text cleaning and preprocessing
Skill extraction using NLP techniques
Job description matching
TF-IDF based resume scoring
Cosine Similarity calculation
Candidate ranking based on role fit
Skill gap identification
Interactive Streamlit dashboard
CSV export of ranked candidates

##Technologies Used
Programming Language
Python
Libraries
Pandas
NLTK
Scikit-learn
Streamlit
Machine Learning & NLP
TF-IDF Vectorization
Cosine Similarity
Text Preprocessing
Skill Extraction
Dataset

Dataset Used:

Resume Dataset (Kaggle)

The dataset contains resumes from multiple domains such as:

HR
Engineering
Information Technology
Finance
Business Development
Agriculture
Consultant
Digital Media
And more

Dataset Columns Used:

ID
Resume_str
Category
Project Structure
Resume-Screening-System/
│
├── data/
│   └── Resume.csv
│
├── src/
│   ├── preprocess.py
│   ├── skill_extractor.py
│   ├── scorer.py
│   ├── gap_analysis.py
│   └── ranker.py
│
├── app.py
├── ranked_candidates.csv
├── requirements.txt
└── README.md
