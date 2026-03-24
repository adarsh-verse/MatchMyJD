from fastapi import APIRouter, UploadFile, File
from app.utils.parser import parse_file
from app.utils.cleaner import clean_text
from app.services.skill_extractor import extract_skills
from app.services.matcher import match_skills

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
    
    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        
        
    }
    