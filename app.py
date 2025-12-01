import streamlit as st
import pandas as pd
import numpy as np
import time
from urllib.parse import quote_plus

st.set_page_config(page_title="CareerRaah", page_icon="🚀", layout="centered")

st.title("CareerRaah")
st.markdown("#### Sahi Raah, Sahi Career")

with st.form(key='inputs'):
    name = st.text_input("Name")
    career_goal = st.selectbox("Career Goal", [
        "Software Engineer",
        "Data Scientist",
        "Govt Job",
        "MBA",
    ])
    budget = st.slider("Budget (INR)", 0, 200000, 20000, step=1000)
    generate = st.form_submit_button("Generate Roadmap")


def build_roadmap(name, career_goal, budget):
    person = name.strip() if name else "Candidate"

    # Base templates
    templates = {
        "Software Engineer": {
            "Immediate": [
                "Polish your resume and GitHub profile",
                "Learn core data structures & algorithms (2-4 weeks)",
                "Apply to internships / junior roles consistently"
            ],
            "Short": [
                "Complete 2–3 real-world projects and publish on GitHub",
                "Prepare system design basics and mock interviews",
                "Take a focused course (web/backend/frontend depending on interest)"
            ],
            "Long": [
                "Target stable role at a reputable product/engineering company",
                "Contribute to open-source and mentor juniors",
                "Plan specializations (cloud, ML infra, security)"
            ]
        },
        "Data Scientist": {
            "Immediate": [
                "Refresh Python, statistics, and SQL basics",
                "Build a simple end-to-end ML project",
                "Create a portfolio notebook (Kaggle or GitHub)"
            ],
            "Short": [
                "Complete courses on ML and model deployment",
                "Participate in competitions / internships",
                "Learn tools: pandas, scikit-learn, basic MLOps"
            ],
            "Long": [
                "Aim for roles delivering business impact with models",
                "Master advanced ML topics and deployment pipelines",
                "Publish case studies or talks"
            ]
        },
        "Govt Job": {
            "Immediate": [
                "Identify the specific exam or service you want to target",
                "Collect syllabus and past papers",
                "Set a daily study schedule"
            ],
            "Short": [
                "Join a focused coaching/class or follow a disciplined course",
                "Regular mock tests and time management practice",
                "Strengthen general knowledge and optional subject"
            ],
            "Long": [
                "Attempt the exam with multiple mocks and revisions",
                "Follow through with interviews or document processes",
                "Plan backups and upskilling for alternate careers"
            ]
        },
        "MBA": {
            "Immediate": [
                "Research target business schools and their requirements",
                "Strengthen your profile (work experience highlights)",
                "Prepare for entrance tests (CAT/GMAT/GRE)"
            ],
            "Short": [
                "Take a structured test-prep course if needed",
                "Work on essays, recommendations, and interview practice",
                "Network with alumni and attend info sessions"
            ],
            "Long": [
                "Aim for admission and plan specialization",
                "Leverage internships and leadership opportunities",
                "Build long-term career goals post-MBA"
            ]
        }
    }

    # Budget-sensitive suggestions
    budget_hint = []
    if budget < 5000:
        budget_hint.append("Budget low: prioritize free resources (YouTube, free courses) and community projects.")
    elif budget < 30000:
        budget_hint.append("Moderate budget: selective paid courses, mentorship calls, or guided projects can help.")
    else:
        budget_hint.append("Healthy budget: consider end-to-end professional courses, mentorship, and bootcamps.")

    chosen = templates.get(career_goal)

    roadmap = {
        "person": person,
        "career_goal": career_goal,
        "budget_hint": budget_hint,
        "Immediate": chosen["Immediate"],
        "Short Term": chosen["Short"],
        "Long Term": chosen["Long"]
    }
    return roadmap


if generate:
    with st.spinner("Generating your personalized roadmap..."):
        time.sleep(1.6)

    roadmap = build_roadmap(name, career_goal, budget)

    st.subheader(f"Roadmap — {roadmap['career_goal']}")
    st.write(f"Personalized for: **{roadmap['person']}**")

    st.markdown("**Immediate Action**")
    for item in roadmap["Immediate"]:
        st.write("- " + item)

    st.markdown("**Short Term**")
    for item in roadmap["Short Term"]:
        st.write("- " + item)

    st.markdown("**Long Term**")
    for item in roadmap["Long Term"]:
        st.write("- " + item)

    if roadmap["budget_hint"]:
        st.info(" ".join(roadmap["budget_hint"]))

    st.markdown("---")

    # Affiliate / recommended course placeholder
    sample_url = f"https://example.com/recommended?course={quote_plus(roadmap['career_goal'])}"
    st.markdown(f"[Recommended Course 🔗]({sample_url})")
    st.caption("(Affiliate link placeholder)")

else:
    st.write("Enter your details and click 'Generate Roadmap' to get started.")
