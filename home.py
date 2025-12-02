import streamlit as st
from pathlib import Path
import base64

# --- 0. HELPER FUNCTION ---
def get_image_as_base64(path):
    """Reads an image file and returns it as a base64 encoded string."""
    try:
        base_path = Path(__file__).parent
        full_path = base_path / path
        if full_path.exists():
            with open(full_path, "rb") as f:
                data = f.read()
            return f"data:image/{full_path.suffix.strip('.')};base64,{base64.b64encode(data).decode()}"
    except Exception as e:
        return None

# --- 1. KNOWLEDGE BASE (Questions & Best Answers) ---
# --- 1. KNOWLEDGE BASE (Questions & Best Answers) ---
KNOWLEDGE_BASE = {
    "Class 12": {
        "B.Tech vs BCA?": "👉 **B.Tech:** 4 years. High value for big MNCs (Google/Microsoft). Best if you have time & budget.\n\n👉 **BCA:** 3 years. Faster & cheaper. To match B.Tech salary, you usually need MCA later.\n\n**Verdict:** Want a job ASAP? Go BCA. Want top-tier product roles? Go B.Tech.",
        "High paying Arts jobs?": "Arts ≠ Poor! Top roles in 2025:\n\n1. **UX Designer:** ₹6-12 LPA (Requires Portfolio)\n2. **Corp Lawyer:** ₹8-15 LPA (Requires CLAT)\n3. **Public Policy:** ₹6-10 LPA (Think Tanks)\n4. **Digital Marketing:** ₹4-8 LPA (Agency life)",
        "Gap Year risks?": "Taking a drop for JEE/NEET is standard in India.\n\n**The Risk:** Sitting idle at home looks bad.\n**The Fix:** Learn a skill (Python/Excel) or intern during your gap. If you have a skill, HR doesn't care about the gap.",
        "Best Pvt Colleges?": "If IIT/NIT is missed, look for **ROI** (Return on Investment).\n\n✅ **Good:** BITS, Thapar, VIT, Manipal (Good placements, high fees).\n⚠️ **Risky:** Colleges with full-page newspaper ads but no transparent placement report.",
        "Commerce without Maths?": "Yes! You can still do:\n1. **BBA/BMS:** Management roles.\n2. **Law (BA LLB):** High paying.\n3. **CA:** Maths is not mandatory, but accounts logic is needed.\n4. **Hotel Management:** Great for extroverts."
    },
    "Class 10": {
        "Science or Commerce?": "Don't choose based on friends!\n\n🧬 **Science:** For builders & curers (Engineers/Doctors). Hardest workload.\n📊 **Commerce:** For money managers (CA/MBA). Medium workload.\n🎨 **Arts:** For creators & leaders (Law/UPSC/Design).",
        "Diploma after 10th?": "✅ **Choose Diploma if:** You need to earn money by age 19 (Junior Engineer role).\n❌ **Avoid Diploma if:** You want to be a CEO or Manager later (Degree is preferred).",
        "School vs Dummy School?": "**For JEE/NEET Aspirants:**\n\n🏫 **Dummy School:** Saves 6-7 hours/day. Best for serious rankers.\n🎒 **Regular School:** Better for personality, English speaking, and backup options if JEE fails.",
        "UPSC start guide": "**Start Slow.** Don't read heavy books yet.\n\n1. **Read NCERTs** (Class 6-12 History/Geo).\n2. **Read Newspaper** (The Hindu) daily.\n3. **Focus on 12th Marks:** You need a graduation degree to sit for UPSC!"
    },
    "College": {
        "Internship Guide": "Don't wait for 3rd year!\n\n1. **Build Proof:** GitHub for coders, Behance for designers.\n2. **Cold Email:** Don't apply on portals. Email HRs directly.\n3. **LinkedIn:** Connect with alumni from your college who are working there.",
        "Placement Prep": "**The 3 Pillars of Placement:**\n1. **Aptitude:** R.S. Aggarwal (Qualifying round).\n2. **Technical:** DSA / Core subjects (Interview).\n3. **Soft Skills:** English speaking (HR Round).",
        "Off-Campus Jobs": "Campus placement failed? Use the **'Referral Strategy'**.\n\nFind alumni from your college on LinkedIn. Message them: 'I have the skills, can you refer me?' Referrals skip the resume queue.",
        "MBA or Job?": "📉 **Freshers:** Do MBA only if it's IIM/Tier-1.\n📈 **Experience:** Work for 2 years, THEN do MBA. You get better roles, higher salary, and more respect in class.",
        "Gate vs GRE?": "🇮🇳 **GATE:** For PSU jobs (Govt) or M.Tech in IITs. Low cost.\n🇺🇸 **GRE:** For MS abroad (USA/Germany). High cost, high global exposure."
    },
    "Job Seeker": {
        "Resume Templates": "**The ATS Rule:** \nKeep it simple. No photos, no two-columns, no graphics.\n\n✅ Use 'Standard Harvard Format' (Black & White text).\n✅ Highlight 'Impact' (e.g., 'Increased sales by 20%').",
        "Interview Tips": "**The STAR Method:**\nWhen asked 'Tell me about a challenge', answer with:\n**S**ituation\n**T**ask\n**A**ction\n**R**esult.",
        "Salary Negotiation": "Never say 'As per industry standards'.\n\n**Say:** 'Based on my research and skills, I am looking for X.'\n**Tip:** Always ask for 10-20% more than you actually want.",
        "Remote Work": "Best sites for remote jobs:\n1. **Wellfound** (Startups)\n2. **LinkedIn** (Filter by 'Remote')\n3. **Toptal/Upwork** (Freelance)\n\n*Skill is key here. English must be good.*",
        "Service vs Product co?": "🏢 **Service (TCS/Infy):** Bulk hiring, easier to enter, slow growth.\n🚀 **Product (Amazon/Uber):** Hard to enter, very high salary, fast growth. \n\n**Advice:** Start Service if you must, but upskill to switch to Product ASAP."
    },
    "Govt Aspirant": {
        "SSC vs Banking?": "⚡ **Banking (IBPS/SBI):** Fast process (Job in 6 months). High work pressure.\n🐢 **SSC CGL:** Slow process (1-2 years). Better work-life balance & power.",
        "UPSC Plan B?": "Always have a backup!\n1. **State PCS:** Syllabus overlaps 70%.\n2. **Teaching (NET/B.Ed):** Respectable & stable.\n3. **Corporate Public Policy:** If you have good communication.",
        "Railway Jobs": "Massive vacancies (RRB NTPC/Group D).\n**Pros:** unparalleled job security, free travel.\n**Cons:** Slow promotion, transferable jobs."
    }
}

# --- 2. CONFIGURATION ---
st.set_page_config(
    page_title="CareerRaah",
    layout="centered",
    page_icon="🚀",
    initial_sidebar_state="collapsed"
)

# --- 3. CSS STYLING ---
# Get background image
bg_image_css = get_image_as_base64("logo/background.jpg")

header_style = f"""
    background-image: url("{bg_image_css}");
    background-size: cover;
    background-position: center;
""" if bg_image_css else """
    background: linear-gradient(135deg, #1A3C8D 0%, #0d255e 100%);
"""

st.markdown(f"""
    <style>
    /* GLOBAL MOBILE FIXES */
    .stApp {{ background-color: #FFF8F0; }}
    
    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }}

    /* HEADER BANNER */
    .header-container {{
        {header_style}
        height: 200px;
        display: flex; flex-direction: column; justify-content: center;
        border-radius: 0 0 20px 20px;
        padding: 1rem;
        margin: -1rem -1rem 2rem -1rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    
    .header-title {{
        color: white; font-family: sans-serif; font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5); margin: 0;
    }}
    
    /* BUTTONS */
    div.stButton > button {{
        width: 100%; background-color: white; color: #1A3C8D;
        border: 1px solid #ddd; border-radius: 12px;
        height: auto; min-height: 3.5rem; /* Allow height to grow */
        font-weight: 600; text-align: left; padding-left: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    div.stButton > button:active, div.stButton > button:focus {{
        background-color: #FFFAE6; border-color: #F9C80E; color: #000;
    }}

    /* ANSWER CARD STYLE */
    .answer-card {{
        background-color: white;
        border-left: 5px solid #FF6B00;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        animation: fadeIn 0.5s;
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(-10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* BOTTOM NAV */
    .bottom-nav {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 70px;
        background-color: white; border-top: 1px solid #eee;
        display: flex; justify-content: space-around; align-items: center;
        z-index: 99999; padding-bottom: 5px;
    }}
    .nav-item {{ text-align: center; font-size: 0.7rem; color: #888; cursor: pointer; }}
    .nav-icon {{ font-size: 1.4rem; display: block; }}
    .nav-item.active {{ color: #FF6B00; font-weight: bold; }}
    
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# --- 4. APP LOGIC ---

# A. Header Section
st.markdown("""
    <div class="header-container">
        <p class="sub-text" style="color: #f0f0f0; margin-top: 5px;"></p>
    </div>
""", unsafe_allow_html=True)

# B. Trending Section
st.markdown("### 🔥 Trending Questions")

# Persona Selector
try:
    persona = st.pills(
        "Who are you?",
        list(KNOWLEDGE_BASE.keys()),
        default="Class 12"
    )
except Exception:
    persona = st.radio("Who are you?", list(KNOWLEDGE_BASE.keys()), horizontal=True)

# C. Question & Answer Logic
if persona:
    # Get questions for the selected persona
    questions_dict = KNOWLEDGE_BASE[persona]
    
    # Create the buttons
    for question, answer in questions_dict.items():
        if st.button(question, key=question):
            # Store the selected answer in session state
            st.session_state['selected_answer'] = answer
            st.session_state['selected_question'] = question

# D. Display the Answer (If clicked)
if 'selected_answer' in st.session_state:
    # Pre-format the answer to avoid backslash issues in f-string
    formatted_answer = st.session_state['selected_answer'].replace('\n', '<br>')
    
    st.markdown(f"""
        <div class="answer-card">
            <h4 style="margin-top:0; color:#1A3C8D;">{st.session_state['selected_question']}</h4>
            <hr style="margin: 10px 0; border-top: 1px solid #eee;">
            <div style="color: #444; font-size: 1rem; line-height: 1.6;">
                {formatted_answer}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # "Close" button logic
    if st.button("Close Answer"):
        del st.session_state['selected_answer']
        st.rerun()

# Spacer
st.markdown("<br><br>", unsafe_allow_html=True)

# E. Bottom Navigation
st.markdown("""
    <div class="bottom-nav">
        <div class="nav-item active">
            <span class="nav-icon">🏠</span>Home
        </div>
        <div class="nav-item">
            <span class="nav-icon">🗺️</span>Roadmap
        </div>
        <div class="nav-item">
            <span class="nav-icon">👤</span>Profile
        </div>
    </div>
""", unsafe_allow_html=True)