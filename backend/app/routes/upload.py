from fastapi import APIRouter, UploadFile, File
from app.utils.parser import parse_file
from app.utils.cleaner import clean_text
from app.services.skill_extractor import extract_skills
from app.services.matcher import match_skills
from app.services.scorer import calculate_score, calculate_final_score
from app.services.similarity import calculate_similarity
from app.services.gap_analyzer import analyze_gaps

router = APIRouter()

@router.post("/upload")
async def upload_file(
    resume: UploadFile = File(...),
    jd: UploadFile = File(...) 
    ):
    
    
    resume_text = parse_file(resume)
    jd_text = parse_file(jd)
    
    resume_cleaned_text = clean_text(resume_text)
    jd_cleaned_text = clean_text(jd_text)
    
    resume_skills = extract_skills(resume_cleaned_text)
    jd_skills = extract_skills(jd_cleaned_text)
    
    matched, missing = match_skills(resume_skills, jd_skills)
    score = calculate_score(matched, jd_skills)
    
    similarity = calculate_similarity(resume_cleaned_text, jd_cleaned_text)
    
    final_score = calculate_final_score(score, similarity)
    
    gap_analysis = analyze_gaps(missing)
    
    
    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "gap_analysis": gap_analysis,
        "score": score,
        "similarity_score": similarity,
        "final_score": final_score
    }
    