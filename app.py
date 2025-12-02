import streamlit as st
from urllib.parse import quote_plus
from fpdf import FPDF

# --- 1. & 2. Brand Personality & Global Design System ---
st.set_page_config(page_title="CareerRaah", page_icon="🚀", layout="centered")

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
        
        p, .stMarkdown {
            font-size: 16px !important; /* Bigger text for mobile reading */
        }

        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .st-emotion-cache-1c5k3kr {display: none;}

        /* --- Layout improvements --- */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }

        /* --- 3.1 Header --- */
        .header-container {
            padding: 1rem 2rem;
            background-color: var(--soft-white);
        }
        .header-title {
            font-family: 'Poppins', sans-serif;
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary-blue);
            padding-top: 10px; /* Adjust for vertical alignment */
        }
        
        /* --- 3.2 Hero Section --- */
        .hero {
            padding-top: 2rem;
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

        /* Mobile-First Improvements */
        @media (max-width: 767px) {
            /* Header becomes stacked to save horizontal space */
            .header-container {
                padding: 0.6rem 0.8rem;
            }
            .header-title {
                font-size: 1.25rem;
                padding-top: 6px;
            }
            .header-cta { display: none; }

            /* Hero & headings scaled for mobile */
            .hero h1 { font-size: 1.6rem; line-height:1.15; }
            .hero p { font-size: 0.95rem; padding: 0 0.5rem; }

            /* Ensure columns stack vertically */
            .stColumns [class*="css-"] {
                flex-direction: column !important;
            }

            img, .logo img { max-width: 100% !important; height: auto !important; }
        }

        /* Make Buttons "Fat" & "Clickable" (Thumb-friendly) */
        .stButton>button {
            width: 100%;
            border-radius: 12px;
            height: 3em;
            font-weight: bold;
            font-size: 18px;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        }

        /* Make Expanders (Accordions) look like Cards */
        .streamlit-expanderHeader {
            background-color: #f0f2f6;
            border-radius: 10px;
            font-weight: 600;
            color: #1A3C8D; /* Your Brand Blue */
        }

        /* Desktop container width to improve readability */
        @media (min-width: 768px) {
            .block-container { max-width: 960px; margin: 0 auto; }
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
        
    # fpdf2's output may return bytes or a bytearray depending on the environment.
    pdf_bytes = pdf.output(dest='S')
    if isinstance(pdf_bytes, bytearray):
        return bytes(pdf_bytes)
    if isinstance(pdf_bytes, str):
        return pdf_bytes.encode('latin-1')
    return pdf_bytes


# --- Session State ---
if 'goal' not in st.session_state:
    st.session_state.goal = None
if 'form_inputs' not in st.session_state:
    st.session_state.form_inputs = {}
if 'page' not in st.session_state:
    st.session_state.page = 'Home'


# --- Simplified Header ---
st.markdown('<div class="header-title">CareerRaah</div>', unsafe_allow_html=True)


# --- Hero Section ---
st.markdown("""
    <div class="hero">
        <h1>Find Your Path. Build Your Future.</h1>
        <p>Private. Instant. Judgment-free career guidance — for every student in India.</p>
    </div>
""", unsafe_allow_html=True)

# --- KNOWLEDGE BASE ---
knowledge_base = {
    "Confused Student (Class 9-10)": {
        "What subjects should I choose after 10th?": "Focus on your interests and strengths. Science is great for engineering/medical, Commerce for business/finance, and Arts for creative fields. We can help you find the best fit.",
        "How do I tell my parents what I want to do?": "Show them a plan. Research the career you're interested in, the courses you'll need, and the job prospects. We can help you build a detailed roadmap to share with them.",
        "I'm not good at studies, what can I do?": "Everyone has unique talents. Let's explore vocational courses, creative fields, or skill-based training that can lead to a successful career. There are many paths to success.",
    },
    "Ambitious Student (Class 11-12)": {
        "Which competitive exam is best for me?": "It depends on your goal. JEE for Engineering, NEET for Medical, CLAT for Law, and CUET for many central universities. Let's analyze your profile to find the right one.",
        "How can I get into a top college abroad?": "You'll need good grades, a strong profile with extracurriculars, and high scores in exams like SAT/ACT and TOEFL/IELTS. We can guide you through the entire process.",
        "What skills should I learn along with my studies?": "Communication, coding, and financial literacy are valuable in any field. We can suggest specific skills and resources based on your career goals.",
    },
    "Concerned Parent": {
        "Is my child choosing the right career?": "We can help you and your child explore various options based on their aptitude and interests, providing a clear path and reducing uncertainty.",
        "How can I support my child's non-traditional career choice?": "Understand their passion, research the field together, and create a backup plan. We provide resources to help parents support their child's dreams.",
        "The career my child wants is too expensive, what can we do?": "There are many scholarships, education loans, and 'earn-while-you-learn' options available. We can help you find the right financial aid.",
    }
}

# --- MOBILE-FIRST LAYOUT ---
if st.session_state.page == 'Home':
    # 1. The Persona Selector (Sticky-ish Navigation)
    st.write("#### 👤 Who are you?")
    selected_persona = st.selectbox(
        "Select your profile:",
        list(knowledge_base.keys()),
        label_visibility="collapsed"  # Hides the label to save space
    )

    st.divider()

    # 2. The Questions (Accordion Style - Saves Vertical Space)
    st.write(f"**🔥 Top Questions for {selected_persona}**")

    # Loop through the dictionary
    questions = knowledge_base[selected_persona]
    for q, ans in questions.items():
        with st.expander(f"❓ {q}"):
            st.markdown(ans)
            # Add a CTA button inside the answer
            if st.button(f"👉 Get Roadmap for this", key=q):
                st.session_state.goal = q
                st.session_state.page = "Roadmap"
                st.rerun()

elif st.session_state.page == 'Roadmap':
    # --- 7. Output Page ---
    st.balloons()
    st.markdown("## Your Personalized Career Blueprint")

    # This is placeholder data. In a real app, this would be generated by an AI model.
    roadmap_data = {
        "Selected Goal": st.session_state.goal,
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
        file_name=f"CareerRaah_Blueprint_{st.session_state.goal}.pdf",
        mime="application/pdf"
    )

    if st.button("← Start Over"):
        st.session_state.page = "Home"
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
