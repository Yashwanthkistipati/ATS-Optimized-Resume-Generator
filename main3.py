import streamlit as st
from datetime import date
import re
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Function to clean text for ATS optimization
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespaces
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters
    return text.strip()


# Function to generate PDF resume
def generate_pdf(name, email, phone, linkedin, github, summary, experience, education, skills):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Add content to the PDF
    c.drawString(30, height - 40, name)
    c.drawString(30, height - 60, f"{email} | {phone}")
    c.drawString(30, height - 80, f"LinkedIn: {linkedin} | GitHub: {github}")

    c.drawString(30, height - 120, "SUMMARY")
    c.drawString(30, height - 140, summary)

    c.drawString(30, height - 180, "EXPERIENCE")
    c.drawString(30, height - 200, experience)

    c.drawString(30, height - 240, "EDUCATION")
    c.drawString(30, height - 260, education)

    c.drawString(30, height - 300, "SKILLS")
    c.drawString(30, height - 320, skills)

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer


# Streamlit interface
st.title('ATS Optimized Resume Generator')

# Collecting user input
name = st.text_input('Full Name')
email = st.text_input('Email')
phone = st.text_input('Phone Number')
linkedin = st.text_input('LinkedIn Profile')
github = st.text_input('GitHub Profile')
summary = st.text_area('Professional Summary')
experience = st.text_area('Work Experience')
education = st.text_area('Education')
skills = st.text_area('Skills')

if st.button('Generate Resume'):
    # Clean text inputs
    name = clean_text(name)
    email = clean_text(email)
    phone = clean_text(phone)
    linkedin = clean_text(linkedin)
    github = clean_text(github)
    summary = clean_text(summary)
    experience = clean_text(experience)
    education = clean_text(education)
    skills = clean_text(skills)

    # Generate PDF
    pdf_buffer = generate_pdf(name, email, phone, linkedin, github, summary, experience, education, skills)

    st.download_button(
        label="Download Resume",
        data=pdf_buffer,
        file_name=f"resume_{name.replace(' ', '_').lower()}.pdf",
        mime="application/pdf"
    )
