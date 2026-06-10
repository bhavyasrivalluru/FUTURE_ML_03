def missing_skills(job_skills, candidate_skills):

    return list(
        set(job_skills) -
        set(candidate_skills)
    )