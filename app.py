import streamlit as st
import pandas as pd
import numpy as np
import time
from urllib.parse import quote_plus

st.set_page_config(page_title="CareerRaah", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
        /* Hide Streamlit's default menu and footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* App-wide font */
        html, body, [class*="st-"] {
            font-family: 'sans-serif';
        }

        /* Header styling */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem;
            background-color: #0056D2; /* Trust Blue */
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .header .title {
            font-size: 2.5rem;
            font-weight: bold;
        }
        .header .button {
            background-color: #FF6B00; /* Action Orange */
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        }

        /* Hero Banner */
        .hero {
            padding: 3rem 1rem;
            background: linear-gradient(to right, #0056D2, #007BFF);
            border-radius: 10px;
            text-align: center;
            color: white;
            margin-bottom: 2rem;
        }
        .hero h1 {
            font-size: 3rem;
            font-weight: bold;
        }

        /* Footer styling */
        .footer {
            margin-top: 3rem;
            padding: 2rem 1rem;
            background-color: #f0f2f6;
            text-align: center;
            border-radius: 10px;
        }
        .footer a {
            color: #0056D2;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer .disclaimer {
            color: gray;
            font-size: 0.9rem;
        }
        .footer .socials {
            margin-top: 1rem;
        }
        .footer .socials a {
            font-size: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="header title">CareerRaah</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="#" class="button">Login / Sign Up</a>', unsafe_allow_html=True)

# --- Hero Banner ---
st.markdown("""
<div class="hero">
    <h1>Confused About Your Career?</h1>
    <p>Get a personalized Roadmap to Google, UPSC, or MBA in 30 seconds. Powered by AI.</p>
</div>
""", unsafe_allow_html=True)


# --- Input Engine ---
with st.form(key='inputs'):
    current_status = st.selectbox("Current Status", ["Class 10", "Class 12", "College Student"])
    goal = st.selectbox("Goal", ["Engineer", "Doctor", "CA", "Govt Job", "Not Sure"])
    budget = st.selectbox("Budget", ["< ₹1L", "₹2L-5L", "₹5L+"])
    marks = st.selectbox("Marks", ["<60%", "60-80%", ">90%"])
    generate = st.form_submit_button("Generate My CareerRaah ⚡")


def build_roadmap(status, goal, budget, marks):
    # This is a placeholder for a more complex AI-driven logic.
    # For now, we use a simple rule-based system.
    
    strategy = "Based on your inputs, here is a starting point."
    if budget == "< ₹1L":
        strategy = "Since your budget is low, we recommend focusing on free online resources and entrance exams for government colleges."
    elif budget == "₹2L-5L" and marks in ["60-80%", ">90%"]:
        strategy = "With your budget and marks, you can consider private colleges with good placement records or specialized online certifications."
    
    immediate_step = "Watch this specific YouTube Playlist today."
    if goal == "Engineer":
        immediate_step = "Start with the 'Data Structures and Algorithms in One Shot' playlist by Apna College on YouTube."
    elif goal == "Doctor":
        immediate_step = "Review the NEET syllabus and start with NCERT biology textbooks."

    monetization = {
        "text": "Recommended Certification: [Link to Coursera/Udemy] - 20% Off.",
        "url": f"https://example.com/recommended?course={quote_plus(goal)}"
    }
    
    roadmap = {
        "strategy": strategy,
        "immediate_step": immediate_step,
        "monetization": monetization
    }
    return roadmap


if generate:
    with st.spinner("Analyzing market trends... Checking colleges... Building your path..."):
        time.sleep(1.6)

    roadmap = build_roadmap(current_status, goal, budget, marks)

    st.markdown("---")
    st.markdown("### Your Personalized CareerRaah")

    # Result Cards
    st.info(f"**The Strategy:** {roadmap['strategy']}")
    st.success(f"**Immediate Step:** {roadmap['immediate_step']}")
    
    st.warning(f"**Recommended Certification:** [{roadmap['monetization']['text']}]({roadmap['monetization']['url']})")
    st.caption("(Affiliate link placeholder)")

else:
    st.write("Enter your details and click 'Generate My CareerRaah ⚡' to get started.")

# --- Footer ---
st.markdown("""
    <div class="footer">
        <p>
            <a href="#">About Us</a> | 
            <a href="#">Privacy Policy</a> | 
            <a href="#">Terms of Service</a> | 
            <a href="#">Partner with Us</a>
        </p>
        <p class="disclaimer">
            CareerRaah uses AI to provide suggestions. Please verify with human experts before making financial decisions.
        </p>
        <p class="copyright">
            © 2025 CareerRaah Technologies. Made with ❤️ in India.
        </p>
        <div class="socials">
            <a href="https://www.linkedin.com" target="_blank">LinkedIn</a> | 
            <a href="https://www.instagram.com" target="_blank">Instagram</a>
        </div>
    </div>
""", unsafe_allow_html=True)
