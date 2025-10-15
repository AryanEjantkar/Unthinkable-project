# 🧠 HireLens – Smart Resume Screener

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![LLM-Powered](https://img.shields.io/badge/AI-LLM%20Powered-green?logo=google-gemini)

An AI-powered resume screening system that uses **LLMs** (like Gemini / GPT) to analyze resumes, score candidates, and provide feedback for recruiters.

---

## 📘 Table of Contents
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Workflow](#-workflow)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation--usage)
- [Future Enhancements](#-future-enhancements)
- [LLM Prompts Used](#-llm-prompts-used-to-create-this-project)
- [Author](#-author)

---

## 🚀 Features
- 📂 Upload multiple resumes in PDF format  
- 🔍 Extract skills and experience automatically  
- 🧠 Evaluate resumes using LLMs  
- 📊 Display ranked candidates with match scores  
- 💬 Provide recruiter-style AI feedback  

---

## 🏗️ System Architecture

![Architecture Diagram](/Architecture.png)

> The system integrates resume parsing, job matching, and LLM evaluation into a unified intelligent pipeline.

---

## 💡 Workflow
1. Upload resumes (`PDF`)  
2. Paste job description  
3. Click **Analyze**  
4. Get ranked resumes with AI feedback  

---

## 🧩 Tech Stack

| Layer | Technology |
|--------|-------------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | Gemini / GPT |
| Parsing | PyPDF2 |
| Visualization | Pandas, Streamlit Charts |
| Deployment | Vercel / Streamlit Cloud |

---

## ⚙️ Installation & Usage
 git clone https://github.com/AryanEjantkar/Unthinkable-project.git
 cd HireLens
 pip install -r requirements.txt
 streamlit run app.py

## 🪄 Future Enhancements

AI-based Resume Rewriter

Bulk Resume Comparison

ATS Optimization Suggestions

Cloud Storage for Resume Data

## 🧠 LLM Prompts Used to Create This Project

This project was developed with the help of **Large Language Models (LLMs)** such as **Gemini** and **GPT**, which assisted in concept ideation, architecture design, UI/UX planning, and documentation writing.

Below are the high-quality prompts that were used throughout the **creation process of HireLens**.

---

### 💡 1. Project Ideation and Concept Development  
> You are an AI product designer.  
> Suggest an innovative project idea for a Streamlit-based AI tool that automates resume screening using LLMs.  
> The project should sound professional, useful for recruiters, and feasible for a student developer.  
> Give a catchy project name and a brief description.

---

### 🧱 2. Architecture and Workflow Design  
> I have a Streamlit app that performs AI-based resume screening.  
> Describe a detailed **high-level architecture** for this project, including components like the frontend, backend, AI model integration, and database.  
> Write the description in a way that even a non-technical reader can visualize it.  

---

### 🪄 3. UI/UX and Frontend Layout Prompts  
> Design a professional and modern **Streamlit UI** for the Smart Resume Scanner.  
> It should include sections for uploading resumes, viewing ATS scores, and visualizing insights.  
> Suggest layout design, color palette, icons, and markdown styling ideas to make it visually appealing.

---

### ⚙️ 4. Core Functionality Development  
> Write Streamlit code to extract text from uploaded PDF resumes and analyze them using NLP/LLM.  
> Provide ATS-friendly feedback such as missing skills, keyword density, and improvement tips.

---
### 📊 5. Visualization and Dashboard Design  
> Suggest an elegant way to visualize resume insights using charts in Streamlit.  
> Include bar charts, pie charts, or progress bars to represent keyword match rates and skill relevance.
---
###  6 Live Demo
[Watch Demo video](https://drive.google.com/file/d/1bVY3fu1aikhlyG6B98dNxlKnDCfzLXBJ/view?usp=sharing)

---
### 🚀 7. Enhancement Brainstorming  
> Suggest creative **future enhancements** for an AI Resume Screening system using LLMs and cloud integration.  
> Include ideas like ATS optimization, resume rewriting, and cloud storage features.

---
### 8. Deployement Link
https://hirelens03.streamlit.app/
---




👨‍💻 Author

Aryan Vimal Ejantkar
🎓 B.Tech (AIML) – VIT Bhopal
💼 Passionate about AI, ML, and automation

