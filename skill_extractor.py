SKILLS = [

    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "data science",
    "data analysis",
    "nlp",
    "tensorflow",
    "pytorch",
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "power bi",
    "tableau",
    "excel",
    "flask",
    "django",
    "spring boot",
    "react",
    "javascript",
    "html",
    "css",
    "mysql",
    "postgresql",
    "mongodb"

]

def extract_skills(text):

    text = text.lower()

    skills_found = []

    for skill in SKILLS:

        if skill in text:
            skills_found.append(skill)

    return list(set(skills_found))