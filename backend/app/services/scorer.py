def calculate_score(matched_skills, jd_skills):
    if len(jd_skills) == 0:
        return 0
    score = (len(matched_skills) / len(jd_skills))*100
    
    return round(score,2)