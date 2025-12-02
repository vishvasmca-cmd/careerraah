import streamlit as st
from pathlib import Path
import base64

# --- 0. HELPER FUNCTION ---
def get_image_as_base64(path):
    try:
        base_path = Path(__file__).parent
        full_path = base_path / path
        if full_path.exists():
            with open(full_path, "rb") as f:
                data = f.read()
            return f"data:image/{full_path.suffix.strip('.')};base64,{base64.b64encode(data).decode()}"
    except Exception:
        return None

# --- 1. KNOWLEDGE BASE ---
KNOWLEDGE_BASE = {
    "Class 12": {
        "B.Tech vs BCA?": "👉 **B.Tech:** 4 years. High value for big MNCs (Google/Microsoft). Best if you have time & budget.\n\n👉 **BCA:** 3 years. Faster & cheaper. To match B.Tech salary, you usually need MCA later.\n\n**Verdict:** Want a job ASAP? Go BCA. Want top-tier product roles? Go B.Tech.",
        "High paying Arts jobs?": "Arts ≠ Poor! Top roles in 2025:\n\n1. **UX Designer:** ₹6-12 LPA (Requires Portfolio)\n2. **Corp Lawyer:** ₹8-15 LPA (Requires CLAT)\n3. **Public Policy:** ₹6-10 LPA (Think Tanks)\n4. **Digital Marketing:** ₹4-8 LPA (Agency life)",
        "Gap Year risks?": "Taking a drop for JEE/NEET is normal. \n\n**Risk:** If you sit idle, it looks bad. \n**Fix:** During your gap year, learn a skill (like Excel or Python) or do a freelance gig. Companies care about *skills*, not just timelines.",
        "Best Pvt Colleges?": "If you can't get IIT/NIT, look for colleges with **high ROI** (Return on Investment).\n\n✅ **Good:** BITS, VIT, Manipal, Thapar (High fees, but good placements).\n⚠️ **Risky:** Local private colleges with big ads but no placement data. Always check their 'Median Salary', not 'Highest Salary'."
    },
    "Class 10": {
        "Science or Commerce?": "Don't choose based on friends!\n\n🧬 **Science:** Choose if you like solving problems & logic. (Engineers/Doctors).\n📊 **Commerce:** Choose if you like money management & numbers. (CA/MBA).\n🎨 **Arts:** Choose if you are creative & analytical. (Law/Design/UPSC).",
        "Diploma after 10th?": "✅ **Yes** if you have financial pressure and need a job by age 19 (Junior Engineer).\n❌ **No** if you want to aim for top-tier management roles later (Degree is preferred).",
        "School vs Dummy School?": "**For JEE/NEET Aspirants:**\n\n🏫 **Dummy School:** Saves time for coaching. Best for serious rankers.\n🎒 **Regular School:** Better personality development and backup options if JEE fails.",
        "UPSC start guide": "**Start Slow.** Don't read heavy books yet.\n\n1. Read NCERTs (Class 6-12) for History/Geography.\n2. Read one newspaper daily (The Hindu/Express).\n3. Focus on passing 12th first!"
    },
    "Job Seeker": {
        "Resume Templates": "**The ATS Rule:** \nKeep it simple. No photos, no two-columns, no graphics.\n\n✅ Use 'Standard Harvard Format' (Black & White text).\n✅ Highlight 'Projects' and 'Impact' (e.g., 'Increased sales by 20%').",
        "Salary Negotiation": "Never say 'As per industry standards'.\n\n**Say:** 'Based on my research and skills, I am looking for a range of X to Y.' Always ask for 10-20% more than you expect.",
        "Remote Work": "Top sites for remote jobs:\n1. **Wellfound** (Startups)\n2. **LinkedIn** (Filter by 'Remote')\n3. **Toptal/Upwork** (Freelance)\n\nSkill is key here. English must be good."
    }
}

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="CareerRaah", layout="centered", page_icon="🚀", initial_sidebar_state="collapsed")

# --- 3. CSS STYLING ---
bg_image_css = get_image_as_base64("logo/background.jpg")
header_bg = f"url('{bg_image_css}')" if bg_image_css else "linear-gradient(135deg, #1A3C8D 0%, #0d255e 100%)"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #FFF8F0; }}
    .block-container {{ padding-top: 1rem !important; padding-bottom: 6rem !important; }}
    
    /* Header Style */
    .header-container {{
        background: {header_bg};
        background-size: cover; 
        background-position: center;
        border-radius: 0 0 20px 20px;
        
        /* FIX: Set fixed height because we removed the text */
        height: 220px; 
        
        margin: -1rem -1rem 1rem -1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    
    /* Expander Styling */
    .streamlit-expanderHeader {{
        background-color: white; border: 1px solid #ddd;
        border-radius: 8px; color: #1A3C8D; font-weight: 600;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    
    /* Radio Button as Toggle Pills */
    div[role="radiogroup"] {{
        display: flex;
        justify-content: center;
        width: 100%;
        background: white;
        padding: 5px;
        border-radius: 50px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }}
    
    div[role="radiogroup"] label {{
        flex: 1;
        text-align: center;
        padding: 8px 20px;
        border-radius: 40px;
        border: none;
        transition: 0.3s;
    }}
    
    div[role="radiogroup"] label[data-baseweb="radio"] {{
        background-color: transparent;
    }}
    
    /* Bottom Nav */
    .bottom-nav {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 70px;
        background-color: white; border-top: 1px solid #eee;
        display: flex; justify-content: space-around; align-items: center;
        z-index: 99999; padding-bottom: 5px;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    }}
    .nav-item {{ text-align: center; font-size: 0.7rem; color: #888; cursor: pointer; }}
    .nav-icon {{ font-size: 1.4rem; display: block; }}
    .nav-item.active {{ color: #FF6B00; font-weight: bold; }}
    
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# --- 4. APP LOGIC ---

# A. Header
# We removed the <h1> and <p> tags because the text is now in the background image
st.markdown(f"""
    <div class="header-container">
        &nbsp; </div>
""", unsafe_allow_html=True)

# B. THE MAIN VIEW SWITCHER (Sub-Tabs)
# This keeps the UI clean. User chooses what they want to see.
view_mode = st.radio(
    "Select View", 
    ["🔥 Trends", "💰 Salary Tool"], 
    horizontal=True, 
    label_visibility="collapsed"
)

# --- VIEW 1: TRENDS ---
if view_mode == "🔥 Trends":
    st.markdown("### 🔍 What's on your mind?")
    
    # Persona Pills
    try:
        persona = st.pills("", list(KNOWLEDGE_BASE.keys()), default="Class 12", label_visibility="collapsed")
    except:
        persona = st.radio("", list(KNOWLEDGE_BASE.keys()), horizontal=True, label_visibility="collapsed")

    if persona:
        questions_dict = KNOWLEDGE_BASE[persona]
        for question, answer in questions_dict.items():
            with st.expander(f"❓ {question}"):
                formatted_ans = answer.replace('\n', '<br>')
                st.markdown(f"""
                    <div style="border-left: 3px solid #FF6B00; padding-left: 10px; margin-bottom: 10px; color: #444;">
                        {formatted_ans}
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"👉 Get Roadmap", key=f"btn_{question}"):
                    st.toast("🗺️ Roadmap feature is coming soon!", icon="✨")

# --- VIEW 2: SALARY TOOL ---
elif view_mode == "💰 Salary Tool":
    st.markdown("### 🔮 Future Income Predictor")
    st.info("Set your target. We'll tell you the path.")
    
    target = st.slider("Target Monthly Income (Age 25)", 15000, 150000, 30000, step=5000, format="₹%d")
    
    # Logic
    if target < 25000:
        role = "Support / Admin Roles"
        path = "General Graduates (BA/BSc/BCom)"
        color = "#7f8c8d"
    elif 25000 <= target < 50000:
        role = "Junior Developer / Analyst"
        path = "BCA / B.Tech (Tier-3) / MBA (Tier-3)"
        color = "#27ae60"
    elif 50000 <= target < 100000:
        role = "Specialist / Consultant"
        path = "B.Tech (CS) / CA / Corporate Law"
        color = "#2980b9"
    else:
        role = "Elite / Leadership Roles"
        path = "IIT/NIT / IIM / Top Rankers"
        color = "#8e44ad"

    # The Result Card
    st.markdown(f"""
        <div style='background:white; padding:20px; border-radius:15px; border:2px solid {color}; text-align:center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-top:20px;'>
            <div style='font-size: 1.2rem; font-weight:bold; color: #555;'>You are aiming for:</div>
            <h2 style='color: {color}; margin: 5px 0;'>{role}</h2>
            <hr style='border: 0; border-top: 1px solid #eee; margin: 15px 0;'>
            <div style='font-size: 0.9rem; color: #888;'>Required Education Path:</div>
            <div style='font-size: 1.1rem; font-weight:bold; color: #333;'>{path}</div>
        </div>
    """, unsafe_allow_html=True)

# Spacer
st.markdown("<br><br>", unsafe_allow_html=True)

# C. Bottom Nav
st.markdown("""
    <div class="bottom-nav">
        <div class="nav-item active">
            <span class="nav-icon">🏠</span>Home
        </div>
        <div class="nav-item" onclick="alert('Roadmap feature is coming soon!');">
            <span class="nav-icon">🗺️</span>Roadmap
        </div>
        <div class="nav-item" onclick="alert('Profile feature is coming soon!');">
            <span class="nav-icon">👤</span>Profile
        </div>
    </div>
""", unsafe_allow_html=True)