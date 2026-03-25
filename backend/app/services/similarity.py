from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resume_text, jd_text):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    
    similarity_score = util.cos_sim(resume_embedding, jd_embedding)
    
    return float(similarity_score[0][0])
    