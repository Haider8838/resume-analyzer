import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from job_matcher import compute_match_score

st.set_page_config(page_title="Smart Resume Analyzer")

st.title("🧠 Smart Resume Analyzer")
st.write("Upload your resume and a job description to see how well they match!")

resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Paste the job description here", height=200)

if st.button("Analyze") and resume_file and job_desc:
    if resume_file.name.endswith("pdf"):
        resume_text = extract_text_from_pdf(resume_file)
    else:
        resume_text = extract_text_from_docx(resume_file)

    score = compute_match_score(resume_text, job_desc)

    st.success(f"✅ Resume Match Score: **{score}%**")

    if score > 80:
        st.balloons()
        st.write("🎯 Great match! Your resume fits the job well.")
    elif score > 60:
        st.write("👍 Decent match, but you can improve keywords.")
    else:
        st.write("⚠️ Low match. Try tailoring your resume more closely to the job description.")