import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def compute_match_score(resume_text, job_text):
    corpus = [preprocess(resume_text), preprocess(job_text)]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)