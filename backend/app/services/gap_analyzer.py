SKILL_EXPLANATIONS = {
    "python": "Python is widely used for backend development, scripting, and data analysis.",
    "java": "Java is commonly used for enterprise applications and backend systems.",
    "sql": "SQL is essential for working with databases and querying structured data.",
    "react": "React is a frontend library used for building interactive user interfaces.",
    "docker": "Docker is used for containerization and deploying applications consistently.",
    "kubernetes": "Kubernetes is used for container orchestration and scaling applications.",
    "aws": "AWS is a cloud platform used for deploying and managing applications.",
    "excel": "Excel is used for data analysis, reporting, and business insights.",
    "communication": "Communication skills are important for teamwork and collaboration."
}

def analyze_gaps(missing_skills):
    gap_analysis = []
    
    for skill in missing_skills:
        if skill in SKILL_EXPLANATIONS:
            explanation = SKILL_EXPLANATIONS[skill]
        else:
            explanation = f"{skill} is required for this role but not found in your resume."
        
        gap_analysis.append(explanation)
        
    return gap_analysis