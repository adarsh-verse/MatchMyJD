def calculate_score(matched_skills, jd_skills):
    if len(jd_skills) == 0:
        return 0
    score = (len(matched_skills) / len(jd_skills))*100
    
    return round(score,2)

def calculate_final_score(skill_score, similarity_score):
    similarity_percent = similarity_score * 100
    
    final_score = (skill_score * 0.7) + (similarity_percent * 0.3)
    
    return round(final_score, 2)