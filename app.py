import sys, os
sys.path.append(os.path.dirname(__file__))  
import streamlit as st
import pandas as pd
from resume_parser import extract_text_from_pdf
from llm_matcher import match_resume_with_job

st.set_page_config(page_title="Smart Resume Screener", layout="wide")

st.title("🧠 Smart Resume Screener Dashboard")
st.write("Upload multiple resumes and compare them with a job description using AI!")

# Sidebar
st.sidebar.header("⚙️ Controls")
job_desc = st.sidebar.text_area("📋 Paste Job Description", height=200)
analyze_button = st.sidebar.button("🚀 Analyze All")

# File uploader
uploaded_files = st.file_uploader(
    "📄 Upload Multiple Resumes (PDFs)",
    type=["pdf"],
    accept_multiple_files=True
)

if analyze_button and uploaded_files and job_desc.strip():
    results = []
    with st.spinner("Analyzing resumes... ⏳"):
        for file in uploaded_files:
            resume_text = extract_text_from_pdf(file)
            ai_result = match_resume_with_job(resume_text, job_desc)

            # Extract Score from AI output
            score_line = [line for line in ai_result.split("\n") if "Score" in line]
            score = (
                int(score_line[0].split(":")[1].split("/")[0].strip())
                if score_line else None
            )

            results.append({
                "Candidate": file.name,
                "Score": score,
                "AI Feedback": ai_result
            })
    
    # Convert to DataFrame & sort by score
    df = pd.DataFrame(results).sort_values(by="Score", ascending=False)
    st.success("✅ Analysis Complete!")

    # Display ranked results
    st.subheader("🏆 Ranked Candidates")
    st.dataframe(df[["Candidate", "Score"]], use_container_width=True)

    # Expandable details for each candidate
    for _, row in df.iterrows():
        with st.expander(f"📜 {row['Candidate']} — Score: {row['Score']}"):
            st.write(row["AI Feedback"])

else:
    st.info("👉 Upload resumes and paste a job description to begin.")
