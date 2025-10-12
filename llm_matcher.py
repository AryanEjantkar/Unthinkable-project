import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file")

# Configure Gemini client
genai.configure(api_key=API_KEY)

def match_resume_with_job(resume_text: str, job_description: str) -> str:
    """
    Compare a resume and job description using Gemini 2.5.
    Returns a score (1–10) and short justification.
    """
    # You can switch between flash/pro here
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
You are an AI recruiter. Compare the following RESUME with the JOB DESCRIPTION.
Rate how well the candidate matches the role on a scale of 1 to 10 and how the resume overlaps the requirements or misses them..

Resume:
{resume_text}

Job Description:
{job_description}

Output format strictly:
Score: X/10
Justification: <short explanation>
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating content: {e}"
