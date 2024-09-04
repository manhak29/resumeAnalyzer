# utils.py

def load_job_description(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extract_keywords(text):
    # Placeholder function to extract keywords from job description
    return set(word.lower() for word in text.split() if len(word) > 3)

if __name__ == "__main__":
    job_description = load_job_description('job_description.txt')
    keywords = extract_keywords(job_description)
    print("Keywords Extracted:", keywords)
