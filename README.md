# Resume and Job Description Matcher host online independently using render

This project is a **Gradio web application** that analyzes how well a resume matches a given job description.  
It uses **LangChain + Ollama** for LLM‑powered analysis and **PyPDF2** for PDF text extraction.


## Features
- Upload your **resume (PDF)**.
- Upload or paste a **job description (PDF or text)**.
- Analyze the match using an Cloud based LLM (via Ollama).
- Get structured JSON output with:
  - Job Title match
  - Roles & Responsibilities match
  - Years of Experience match
  - Keywords match
  - Scores (out of 10)
  - Summary
  - Suggestions for improvement

### It's similar to my R-JD-Analyser-Offine but its completly a cloud version and it improves efficiency and greatly reduces timetaken for analysis.

# To install dependencies
  pip install -r requirements.txt

# To Run a Application in web
  run app.py

PROJECT HIERARCHY
-- requirements.txt
-- main.py
-- app.py
