# resume_parser.py

import PyPDF2

def parse_resume(pdf_path):
    # Extract text from PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    
    # Example: Simple parsing logic (to be enhanced)
    resume_data = {
        'skills': extract_skills(text),
        'experience': extract_experience(text)
    }
    
    return resume_data

def extract_skills(text):
    # Placeholder function for skill extraction
    return ["Python", "Data Analysis"]

def extract_experience(text):
    # Placeholder function for experience extraction
    return "3 years of experience in data analysis and machine learning."

if __name__ == "__main__":
    resume_data = parse_resume('sample_resume.pdf')
    print("Parsed Resume Data:", resume_data)
