import streamlit as st
import pandas as pd
from resume_parser import extract_text_from_pdf
from llm_matcher import match_resume_with_job
from PIL import Image
import base64, io

st.set_page_config(page_title="HireLens", page_icon="Favicon.png", layout="wide")

# --------------------- STYLING ---------------------
st.markdown("""
<style>
body, .main {
    background-color: #1E88E5;
    font-family: 'Segoe UI', sans-serif;
    color: #0d47a1;
}

/* 🔹 Full-width container */
.block-container {
    background-color: #E3F2FD;
    border-radius: 20px;
    padding: 40px 80px !important;
    width: 95% !important;
    margin: 40px auto !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
}

/* Center logo and title */
.app-logo {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 5px;
}
.app-logo img {
    width: 85px;
    height: 85px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}
.app-title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    color: #0d47a1;
    margin-top: 5px;
    margin-bottom: 25px;
}

/* Job description input */
.search-container {
    position: relative;
    width: 100%;
    margin: 0 auto 25px auto;
}
.search-container input {
    width: 100%;
    padding: 14px 50px 14px 20px;
    border-radius: 12px;
    border: 2px solid #64b5f6;
    font-size: 16px;
}
.search-icon {
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 22px;
    color: #1565c0;
}

/* Uploaded files display */
.uploaded-files {
    text-align: center;
    color: #0d47a1;
    font-weight: 500;
    margin-top: 10px;
}

/* Buttons and controls */
.top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: 30px;
}
.analyze-btn, .clear-btn {
    border: none;
    padding: 12px 35px;
    border-radius: 10px;
    font-size: 16px;
    color: white;
}
.analyze-btn {
    background-color: #1565c0;
}
.analyze-btn:hover {
    background-color: #0d47a1;
}
.clear-btn {
    background-color: #ef5350;
}
.clear-btn:hover {
    background-color: #c62828;
}

/* Score display boxes */
.score-box {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px 30px;
    margin: 20px 0;
    box-shadow: 0 3px 8px rgba(0,0,0,0.1);
}

/* Footer */
.footer {
    text-align: center;
    font-size: 15px;
    color: #0d47a1;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# --------------------- HEADER ---------------------
try:
    logo = Image.open("icon.png")
    buffered = io.BytesIO()
    logo.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()
    st.markdown(f"<div class='app-logo'><img src='data:image/png;base64,{img_base64}'/></div>", unsafe_allow_html=True)
except:
    st.warning("⚠️ Logo file (loOGO.png) not found.")

st.markdown("<div class='app-title'>HireLens</div>", unsafe_allow_html=True)

# --------------------- JOB DESCRIPTION ---------------------
st.markdown("""
<div class="search-container">
  <input type="text" id="jobdesc" name="jobdesc" placeholder="Enter job description here..." />
  <span class="search-icon">🔍</span>
</div>
""", unsafe_allow_html=True)

# --------------------- UPLOAD SECTION ---------------------
uploaded_files = st.file_uploader(
    "Upload resumes (PDF only)",
    type=["pdf"],
    accept_multiple_files=True
)

# --------------------- Uploaded Files ---------------------
if uploaded_files:
    st.markdown("<div class='uploaded-files'>📂 Uploaded Files:</div>", unsafe_allow_html=True)
    for file in uploaded_files:
        st.markdown(f"<div style='text-align:center;'>{file.name}</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='uploaded-files'>No resumes uploaded yet.</div>", unsafe_allow_html=True)

# --------------------- CONTROL BAR ---------------------
col1, col2 = st.columns([8, 1])
with col1:
    analyze_button = st.button("🔍 Analyze", key="analyze", help="Analyze uploaded resumes")
with col2:
    clear_button = st.button("🧹 Clear", key="clear", use_container_width=True)

# --------------------- LOGIC ---------------------
if analyze_button and uploaded_files:
    results = []
    with st.spinner("Analyzing resumes... ⏳"):
        for file in uploaded_files:
            resume_text = extract_text_from_pdf(file)
            ai_result = match_resume_with_job(resume_text, "Job Description Placeholder")
            score_line = [line for line in ai_result.split("\n") if "Score" in line]
            score = int(score_line[0].split(":")[1].split("/")[0].strip()) if score_line else 0
            results.append({"Candidate": file.name, "Score": score, "AI Feedback": ai_result})

    df = pd.DataFrame(results).sort_values(by="Score", ascending=False)
    for _, row in df.iterrows():
        st.markdown(f"<div class='score-box'>", unsafe_allow_html=True)
        st.write(f"### 📄 {row['Candidate']}")
        st.write(f"**Resume Score: {row['Score']}/10**")
        st.progress(row["Score"]/10)
        st.write("**ATS Compatibility:**")
        st.progress(row["Score"]/10)
        st.write("**Match with Job Description:**")
        st.progress(row["Score"]/10)
        st.caption(f"AI Feedback: {row['AI Feedback']}")
        st.markdown("</div>", unsafe_allow_html=True)

elif clear_button:
    st.experimental_rerun()
else:
    st.info("Upload resumes and enter job description to begin.")

# --------------------- FOOTER ---------------------
st.markdown("<div class='footer'>💡 HireLens uses Gemini AI to analyze resumes, providing ATS and job-based insights for better hiring decisions.</div>", unsafe_allow_html=True)
