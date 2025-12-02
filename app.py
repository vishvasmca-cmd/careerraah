import streamlit as st
from urllib.parse import quote_plus
from fpdf import FPDF

# --- 1. & 2. Brand Personality & Global Design System ---
st.set_page_config(page_title="CareerRaah", layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Montserrat:wght@400;600&family=Inter:wght@400;600&family=Roboto:wght@400;600&display=swap');
        
        /* Brand Colors */
        :root {
            --primary-blue: #1A3C8D;
            --secondary-yellow: #F9C80E;
            --soft-white: #FFFFFF;
            --light-grey: #F1F3F6;
            --dark-text: #1A1A1A;
        }

        /* Typography */
        html, body, [class*="st-"], [class*="css-"] {
            font-family: 'Inter', 'Roboto', sans-serif;
            color: var(--dark-text);
        }
        h1, h2, h3 {
            font-family: 'Poppins', 'Montserrat', sans-serif;
            font-weight: 600;
            color: var(--primary-blue);
        }

        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .st-emotion-cache-1c5k3kr {display: none;}

        /* --- 3.1 Header --- */
        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2rem;
            background-color: var(--soft-white);
            box-shadow: 0 2px 4px 0 rgba(0,0,0,0.1);
            z-index: 1000;
        }
        .header .title {
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--primary-blue);
        }
        .header .nav {
            display: flex;
            align-items: center;
        }
        .header .nav a {
            margin: 0 1rem;
            color: var(--dark-text);
            text-decoration: none;
            font-weight: 600;
        }
        .header .nav .cta-button {
            background-color: var(--secondary-yellow);
            color: var(--dark-text);
            padding: 0.5rem 1rem;
            border-radius: 12px;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        /* --- 3.2 Hero Section --- */
        .hero {
            padding-top: 8rem; /* Space for sticky header */
            text-align: center;
        }
        .hero h1 {
            font-size: 3.5rem;
            color: var(--primary-blue);
        }
        .hero p {
            font-size: 1.2rem;
            color: var(--dark-text);
            max-width: 600px;
            margin: 0 auto;
        }
        .hero .cta-button {
            background-color: var(--secondary-yellow);
            color: var(--dark-text);
            padding: 1rem 2rem;
            border-radius: 16px;
            font-size: 1.2rem;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
            margin-top: 2rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        .hero .sub-cta {
            margin-top: 1rem;
            color: gray;
        }

        /* --- 4. Why CareerRaah --- */
        .trust-section {
            padding: 4rem 2rem;
            background-color: var(--light-grey);
            text-align: center;
        }
        .trust-section h2 {
            margin-bottom: 2rem;
        }
        .trust-card {
            background-color: var(--soft-white);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            text-align: center;
        }
        .trust-card h3 {
            font-size: 1.2rem;
            margin-top: 1rem;
        }

        /* --- 5. Choose Your Goal --- */
        .goal-section {
            padding: 4rem 2rem;
            text-align: center;
        }
        .goal-section h2 {
            margin-bottom: 2rem;
        }
        
        /* --- 9. Footer --- */
        .footer {
            padding: 4rem 2rem 2rem 2rem;
            background-color: var(--primary-blue);
            color: var(--soft-white);
        }
        .footer h3 {
            color: var(--secondary-yellow);
        }
        .footer a {
            color: var(--soft-white);
            text-decoration: none;
            display: block;
            margin-bottom: 0.5rem;
        }
        .footer .bottom-line {
            margin-top: 2rem;
            text-align: center;
            color: var(--light-grey);
        }

    </style>
""", unsafe_allow_html=True)


# --- PDF Generation ---
def generate_pdf(roadmap_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Your CareerRaah Blueprint", ln=True, align='C')
    
    for key, value in roadmap_data.items():
        pdf.cell(200, 10, txt=f"{key.replace('_', ' ').title()}: {value}", ln=True)
        
    return pdf.output(dest='S').encode('latin-1')


# --- Session State ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'
if 'goal' not in st.session_state:
    st.session_state.goal = None
if 'form_inputs' not in st.session_state:
    st.session_state.form_inputs = {}


def navigate_to(page_name):
    st.session_state.page = page_name

# --- 3.1 Header ---
st.markdown("""
    <div class="header">
        <div class="title">CareerRaah</div>
        <div class="nav">
            <a href="#">Why CareerRaah</a>
            <a href="#">Features</a>
            <a href="#">Pricing</a>
            <a href="#">For Parents</a>
            <a href="#">Login</a>
            <a href="#" class="cta-button">Start Your Path →</a>
        </div>
    </div>
""", unsafe_allow_html=True)


# --- Page Routing ---
if st.session_state.page == 'Home':
    # --- 3.2 Hero Section ---
    st.markdown("""
        <div class="hero">
            <h1>Find Your Path. Build Your Future.</h1>
            <p>Private. Instant. Judgment-free career guidance — for every student in India.</p>
            <a href="#" class="cta-button">Start My Career Journey →</a>
            <p class="sub-cta">Free • Private • Takes 30 seconds</p>
        </div>
    """, unsafe_allow_html=True)

    # --- 4. Why CareerRaah ---
    with st.container():
        st.markdown('<div class="trust-section">', unsafe_allow_html=True)
        st.markdown('<h2>Guidance You Can Trust</h2>', unsafe_allow_html=True)
        cols = st.columns(3, gap="large")
        with cols[0]:
            st.markdown("""
                <div class="trust-card">
                    <h3>🛡️ Judgment-Free</h3>
                    <p>Share marks, dreams, fears — privately.</p>
                </div>
            """, unsafe_allow_html=True)
        with cols[1]:
            st.markdown("""
                <div class="trust-card">
                    <h3>⚡ Instant Clarity</h3>
                    <p>Get personalized career roadmaps in 30 seconds.</p>
                </div>
            """, unsafe_allow_html=True)
        with cols[2]:
            st.markdown("""
                <div class="trust-card">
                    <h3>₹ Affordable for Everyone</h3>
                    <p>Most guidance is free. Premium starts at ₹29.</p>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # --- 5. Choose Your Goal ---
    with st.container():
        st.markdown('<div class="goal-section">', unsafe_allow_html=True)
        st.markdown('<h2>Choose Your Goal</h2>', unsafe_allow_html=True)
        
        cols = st.columns(4)
        goals = ["Engineer", "UPSC Officer", "MBA / Business", "Software Developer", "Designer", "Government Jobs", "Abroad Study", "Not Sure?"]
        for i, goal in enumerate(goals):
            if cols[i%4].button(goal, key=f"goal_{i}", use_container_width=True):
                st.session_state.goal = goal
                st.info(f"You selected: {goal}. Now, tell us more below. (Note: Smooth scroll is a UX goal, this is a functional stand-in)")

        st.markdown('</div>', unsafe_allow_html=True)


    # --- 6. Smart Career Generator ---
    with st.form(key='generator_form'):
        st.markdown("### Tell us about yourself")
        
        status = st.selectbox("Step 1: Your Current Stage", ["9–10", "11–12", "College", "Graduate", "Working Professional"])
        
        goal_options = ["Engineer", "UPSC Officer", "MBA / Business", "Software Developer", "Designer", "Government Jobs", "Abroad Study", "Not Sure?"]
        goal_index = goal_options.index(st.session_state.goal) if st.session_state.goal in goal_options else len(goal_options) - 1
        goal = st.selectbox("Step 2: Your Goal", goal_options, index=goal_index)
        
        challenges = st.multiselect("Step 3: Your Biggest Challenge(s)", ["Low Marks", "No Money", "Confused", "Parents Pressure", "All of these"])
        
        submitted = st.form_submit_button("Generate My CareerRaah ⚡")

        if submitted:
            st.session_state.form_inputs = {
                "status": status,
                "goal": goal,
                "challenges": challenges
            }
            with st.spinner("Building your personalized roadmap..."):
                import time
                time.sleep(2)
            navigate_to("Roadmap")
            st.rerun()

elif st.session_state.page == 'Roadmap':
    # --- 7. Output Page ---
    st.balloons()
    st.markdown("## Your Personalized Career Blueprint")

    # This is placeholder data. In a real app, this would be generated by an AI model.
    roadmap_data = {
        "Selected Goal": st.session_state.form_inputs.get('goal', 'Not specified'),
        "Action Plan": "Based on your inputs, here's a 6-month plan...",
        "Month 1-2": "Foundational Skills in your chosen field.",
        "Month 3-4": "Build 2-3 portfolio projects.",
        "Month 5-6": "Focus on advanced topics and interview prep.",
        "Exams to Consider": "JEE Mains, UPSC CSE, CAT",
        "Free Resources": "NPTEL, Coursera's free courses, Khan Academy"
    }

    st.markdown("---")
    st.markdown("### Recommended Action Plan")
    st.info(f"**Month 1-2:** {roadmap_data['Month 1-2']}")
    st.success(f"**Month 3-4:** {roadmap_data['Month 3-4']}")
    st.warning(f"**Month 5-6:** {roadmap_data['Month 5-6']}")

    st.markdown("---")
    st.markdown("### Exams & Colleges")
    st.write(f"Top exams to prepare for: {roadmap_data['Exams to Consider']}")

    st.markdown("---")
    st.markdown("### Free Resources")
    st.write(roadmap_data['Free Resources'])

    pdf_data = generate_pdf(roadmap_data)
    st.download_button(
        label="Download My Career Blueprint PDF",
        data=pdf_data,
        file_name=f"CareerRaah_Blueprint_{st.session_state.form_inputs.get('goal', 'general')}.pdf",
        mime="application/pdf"
    )
    
    if st.button("← Start Over"):
        navigate_to("Home")
        st.session_state.goal = None
        st.rerun()

# --- 8. Parents Trust Section ---
st.markdown("""
    <div style="background-color: #fef9e7; padding: 4rem 2rem; text-align: center;">
        <h2 style="color: #1A3C8D;">A Safe, Private, Affordable Guide for Every Child.</h2>
        <p style="max-width: 600px; margin: 1rem auto; color: #1A1A1A;">
            Career decisions are stressful. CareerRaah offers your child a quiet, supportive space to explore their options without judgment or pressure. Our AI provides data-backed suggestions, helping them build confidence and clarity.
        </p>
    </div>
""", unsafe_allow_html=True)


# --- 9. Footer ---
with st.container():
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    cols = st.columns(4)
    with cols[0]:
        st.markdown("<h3>Company</h3>", unsafe_allow_html=True)
        st.markdown('<a href="#">About</a>', unsafe_allow_html=True)
        st.markdown('<a href="#">Contact</a>', unsafe_allow_html=True)
        st.markdown('<a href="#">Partner</a>', unsafe_allow_html=True)
        st.markdown('<a href="#">Careers</a>', unsafe_allow_html=True)
    with cols[1]:
        st.markdown("<h3>Legal</h3>", unsafe_allow_html=True)
        st.markdown('<a href="#">Privacy Policy</a>', unsafe_allow_html=True)
        st.markdown('<a href="#">Terms</a>', unsafe_allow_html=True)
    with cols[2]:
        st.markdown("<h3>Social</h3>", unsafe_allow_html=True)
        st.markdown('<a href="#">LinkedIn</a>', unsafe_allow_html=True)
        st.markdown('<a href="#">Instagram</a>', unsafe_allow_html=True)
    with cols[3]:
        st.markdown("<h3>CareerRaah</h3>", unsafe_allow_html=True)
        st.markdown("<p>Sahi Raah, Sahi Career.</p>", unsafe_allow_html=True)

    st.markdown('<div class="bottom-line">Made with ❤️ in India • © 2025 CareerRaah Technologies</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
