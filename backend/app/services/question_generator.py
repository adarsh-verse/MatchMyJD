import requests
import json
def generate_question_prompt(missing_skills, jd_text):
    prompt = f"""
    You are an expert interviewer.
    
    Based on the missing skills:
    {missing_skills}
    
    AND the job description:
    {jd_text}
    
    Generate output STRICTLY in JSON format:

    {{
      "technical_questions": ["...", "...", "..."],
      "behavioral_questions": ["...", "...", "..."]
    }}

    
    Do not hallucinate skills not mentioned.
    Do NOT add any explanations.
    Do NOT add extra text.
    Only return JSON.
    Focus on realistic job interview questions.
    """
    
    return prompt

def generate_questions(missing_skills, jd_text):
    prompt = generate_question_prompt(missing_skills, jd_text)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json ={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )
    
    result = response.json()["response"]
    try:
        return json.loads(result)
    except:
        return{
            "technical_questions": [],
            "behavioral_questions":[],
            "raw_output": result 
        }
    