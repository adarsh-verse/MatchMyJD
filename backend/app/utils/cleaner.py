import re
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    
    text = re.sub(r'[^a-z\s]', ' ', text)
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    words = text.split()
    
    words = [word for word in words if word not in STOPWORDS]
    
    cleaned_text = " ".join(words)
    
    return cleaned_text