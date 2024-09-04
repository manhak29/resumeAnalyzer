# analyzer.py

import spacy
from resume_parser import parse_resume
from utils import load_job_description, extract_keywords

nlp = spacy.load("en_core_web_sm")

def analyze_resume(resume_text, job_description_text):
    resume_data = parse_resume(resume_text)
    job_keywords = extract_keywords(job_description_text)
    
    # Extracting skills and experience from the resume
    resume_skills = resume_data.get('skills', [])
    resume_experience = resume_data.get('experience', [])
    
    # Analyzing the match between job keywords and resume skills
    matched_skills = [skill for skill in resume_skills if skill in job_keywords]
    
    analysis_results = {
        'matched_skills': matched_skills,
        'experience_summary': resume_experience
    }
    
    return analysis_results

if __name__ == "__main__":
    # Load resume and job description
    with open('sample_resume.pdf', 'r') as resume_file:
        resume_text = resume_file.read()
    
    job_description_text = load_job_description('job_description.txt')
    
    results = analyze_resume(resume_text, job_description_text)
    
    print("Matched Skills:", results['matched_skills'])
    print("Experience Summary:", results['experience_summary'])
