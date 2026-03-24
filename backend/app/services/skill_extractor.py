SKILLS_DB = [
    "python", "java", "c++", "sql", "excel",
    "machine learning", "deep learning", "data analysis",
    "power bi", "tableau", "communication", "teamwork",
    "leadership", "aws", "docker", "kubernetes", "react"
]

def extract_skills(text):
    found_skills = []
    
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    
    return found_skills

