from fastapi import APIRouter, UploadFile, File
from app.utils.parser import parse_file
from app.utils.cleaner import clean_text

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    raw_text = parse_file(file)
    cleaned_text = clean_text(raw_text)
    
    return {
        "filename": file.filename,
        "extracted_text_preview": cleaned_text[:500]
        
    }
    