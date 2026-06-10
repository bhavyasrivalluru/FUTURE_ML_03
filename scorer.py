from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def similarity_scores(job_description, resumes):

    documents = [job_description]

    documents.extend(resumes)

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    job_vector = tfidf_matrix[0]

    resume_vectors = tfidf_matrix[1:]

    scores = cosine_similarity(
        job_vector,
        resume_vectors
    )

    return scores.flatten()