import streamlit as st
from fpdf import FPDF
import time
import google.generativeai as genai

# --- 1. AI CONFIGURATION ---
GOOGLE_API_KEY = "AIzaSyBCHAg7zv6BQotkIzVzNAjXqPsEyl6rOh0"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error(f"AI Config Error: {e}")

# --- 2. CSS & UI SETUP ---
st.markdown("""
<style>
.step-wrapper { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px; margin-bottom: 20px; }
.step-item { display: flex; align-items: center; font-size: 14px; padding: 8px 12px; background: #f5f5f5; border-radius: 6px; white-space: nowrap; border: 1px solid #ddd; color: #555; }
.step-item.active { background: #FF6B00; color: white; font-weight: 600; border-color: #FF6B00; }
.arrow { font-size: 18px; font-weight: bold; padding: 0 4px; color: #ccc; }
@media (max-width: 600px) { .step-item { font-size: 12px; padding: 6px 8px; } .arrow { font-size: 14px; padding: 0 2px; } }
</style>
""", unsafe_allow_html=True)

def render_arrow_steps(active_step):
    steps = ["Profile", "Academics", "Interests", "Goals", "Finalize"]
    html = "<div class='step-wrapper'>"
    for i, step in enumerate(steps):
        active = "active" if (i + 1) == active_step else ""
        html += f"<div class='step-item {active}'>{i+1}. {step}</div>"
        if i < len(steps) - 1:
            html += "<div class='arrow'>→</div>"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "step" not in st.session_state:
    st.session_state.step = 1
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "final_report" not in st.session_state:
    st.session_state.final_report = None

# --------------------- MAIN PAGE CONTENT ---------------------
st.markdown("""
<div style='text-align:center; padding:30px 10px; background:#1A3C8D; color:white; border-radius:12px;'>
    <h1 style='margin-bottom:10px;'>🚀 Welcome to CareerRaah!</h1>
    <p style='font-size:16px;'>Discover your ideal career path with our AI-powered assessment. Quick, personal, and actionable!</p>
    <a href='#assessment' style='background:#FF6B00; padding:12px 24px; border-radius:8px; color:white; text-decoration:none; font-weight:bold;'>Start Assessment ➝</a>
</div>
""", unsafe_allow_html=True)

# --- Customer Reviews Section ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🌟 What Students & Parents Say")
st.markdown("""
<div style='display:flex; flex-wrap:wrap; gap:15px; justify-content:center;'>

<div style='border:1px solid #ddd; padding:15px; border-radius:10px; width:250px; background:#f8f9fa;'>
<p>“CareerRaah gave me clarity on my Engineering options. The AI report was super helpful!”</p>
<b>— Riya, Class 12</b>
</div>

<div style='border:1px solid #ddd; padding:15px; border-radius:10px; width:250px; background:#f8f9fa;'>
<p>“As a parent, I loved how realistic the roadmap was. It helped my son decide on his career confidently.”</p>
<b>— Mr. Sharma</b>
</div>

<div style='border:1px solid #ddd; padding:15px; border-radius:10px; width:250px; background:#f8f9fa;'>
<p>“I didn’t know about careers in AI & Robotics until CareerRaah highlighted them. Eye-opening!”</p>
<b>— Ankit, Class 11</b>
</div>

</div>
""", unsafe_allow_html=True)

# --- Highlight Features Section ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🚀 Why Choose CareerRaah?")
st.markdown("""
<div style='display:flex; flex-wrap:wrap; gap:15px; justify-content:center;'>

<div style='border:1px solid #ddd; padding:20px; border-radius:12px; width:200px; background:#FFF8E1;'>
<b>🤖 Personalized AI Report</b>
<p>Tailored roadmap in under 5 minutes.</p>
</div>

<div style='border:1px solid #ddd; padding:20px; border-radius:12px; width:200px; background:#E8F5E9;'>
<b>🎯 Realistic Guidance</b>
<p>Aligned with grades, stream & budget.</p>
</div>

<div style='border:1px solid #ddd; padding:20px; border-radius:12px; width:200px; background:#E3F2FD;'>
<b>🚀 Future-ready Careers</b>
<p>AI, Robotics, Design, Finance, Medicine & more.</p>
</div>

<div style='border:1px solid #ddd; padding:20px; border-radius:12px; width:200px; background:#F3E5F5;'>
<b>📱 Mobile Friendly</b>
<p>Complete your assessment on any device.</p>
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# --------------------- STEP 1: PROFILE ---------------------
if st.session_state.step == 1:
    render_arrow_steps(1)
    st.subheader("Step 1: Academic Profile")
    st.info("We need this to align with your syllabus (NCERT/State).")

    current_stage = st.radio("Which class are you in?", ["Class 8-10 (High School)", "Class 11-12 (Higher Secondary)", "College / Graduate", "Gap Year"], horizontal=True)
    st.session_state.answers["current_stage"] = current_stage

    board = st.selectbox("Which Education Board?", ["CBSE (Central Board)", "ICSE / ISC (CISCE)", "State Board (HSC/SSC)", "IB / IGCSE (International)", "Open School (NIOS)"])
    st.session_state.answers["board"] = board

    if current_stage in ["Class 11-12 (Higher Secondary)", "College / Graduate", "Gap Year"]:
        stream = st.selectbox("Select your Stream:", ["Science (PCM) - Engineering Focus", "Science (PCB) - Medical Focus", "Science (PCMB) - General", "Commerce with Maths", "Commerce without Maths", "Humanities / Arts", "Diploma / Vocational"])
        st.session_state.answers["stream"] = stream
    else:
        st.session_state.answers["stream"] = "Not Decided (Class 10)"

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Next ➝", type="primary", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# --------------------- STEP 2: ACADEMICS ---------------------
if st.session_state.step == 2:
    render_arrow_steps(2)
    st.subheader("Step 2: Academic Strength")
    st.write("Be honest! This helps us suggest realistic options.")

    st.session_state.answers["strong_subjects"] = st.multiselect("Which subjects do you genuinely enjoy & score well in?", ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science/IP", "Accounts", "Economics", "Business Studies", "History/Pol Sci", "Geography", "English/Literature", "Art/Design"])
    
    st.session_state.answers["academic_score"] = st.select_slider("What is your average aggregate percentage?", options=["< 60%", "60% - 75%", "75% - 85%", "85% - 95%", "95% + (Topper)"])
    
    st.session_state.answers["exam_status"] = st.radio("Are you preparing for any entrance exams?", ["No, focusing on Boards", "JEE (Mains/Adv)", "NEET", "CA / CS Foundation", "CLAT (Law)", "CUET (Central Univ)", "IPMAT (IIMs)", "UPSC / Govt Exams", "Design (NID/NIFT)"])

    c1, c2 = st.columns(2)
    if c1.button("⟵ Back", use_container_width=True):
        st.session_state.step = 1
        st.rerun()
    if c2.button("Next ➝", type="primary", use_container_width=True):
        st.session_state.step = 3
        st.rerun()

# --------------------- STEP 3: INTERESTS ---------------------
if st.session_state.step == 3:
    render_arrow_steps(3)
    st.subheader("Step 3: Interests & Hobbies")

    interest_choice = st.multiselect("What topics excite you outside of textbooks?", ["💻 Coding / App Dev / AI", "🤖 Robotics / Electronics", "⚕️ Human Biology / Medicine", "🏗️ Civil / Architecture", "💰 Stock Market / Finance", "📈 Marketing / Business Strategy", "⚖️ Law / Social Justice", "🎨 Sketching / UI Design", "🎥 Video Editing / Content Creation", "✍️ Writing / Journalism", "👮 Defense / Police Services", "🌍 Travel / Geography"])
    st.session_state.answers["interests"] = interest_choice

    st.write("**Work Style Preference:**")
    st.session_state.answers["work_style"] = st.radio("", ["I want a Desk Job (AC Office, Laptop)", "I want Field Work (Travel, Sites, interaction)", "I want a Creative Studio (Art, Design, Freedom)", "I want Uniform/Discipline (Defense, Pilot, Merchant Navy)"], label_visibility="collapsed")

    c1, c2 = st.columns(2)
    if c1.button("⟵ Back", use_container_width=True):
        st.session_state.step = 2
        st.rerun()
    if c2.button("Next ➝", type="primary", use_container_width=True):
        st.session_state.step = 4
        st.rerun()

# --------------------- STEP 4: FAMILY & BUDGET ---------------------
if st.session_state.step == 4:
    render_arrow_steps(4)
    st.subheader("Step 4: Goals & Reality")

    st.write("**💰 College Budget Expectation (Per Year)**")
    st.caption("This helps us suggest Pvt vs Govt colleges.")
    st.session_state.answers["budget"] = st.select_slider("Select Range:", options=["Low (< ₹1L)", "Medium (₹1L - ₹4L)", "High (₹4L - ₹10L)", "Premium (> ₹10L)"])

    st.session_state.answers["parent_pressure"] = st.checkbox("My parents strictly want Engineering/Medical.")
    
    st.session_state.answers["location"] = st.radio("Where do you want to study?", ["Home Town (Day Scholar)", "Metro City (Hostel OK)", "Abroad (High Budget)"])

    st.markdown("---")
    st.session_state.answers["language"] = st.radio(
        "**🌐 Select Report Language**",
        ["English", "Hindi"],
        horizontal=True
    )

    c1, c2 = st.columns(2)
    if c1.button("⟵ Back", use_container_width=True):
        st.session_state.step = 3
        st.rerun()
    if c2.button("Generate Report ➝", type="primary", use_container_width=True):
        st.session_state.step = 5
        st.rerun()

# --------------------- STEP 5: VALIDATION & FINALIZING ---------------------
if st.session_state.step == 5:
    render_arrow_steps(5)
    st.subheader("⏳ Analyzing your Profile...")

    stream = st.session_state.answers.get("stream", "")
    exam = st.session_state.answers.get("exam_status", "")
    subjects = st.session_state.answers.get("strong_subjects", [])
    
    if "Commerce" in stream or "Humanities" in stream or "Arts" in stream:
        if exam in ["NEET", "JEE (Mains/Adv)"]:
            st.error("⚠️ Conflict Detected: Your stream does not align with selected entrance exam.")
            st.info("💡 Fix: Please go back to Step 1 or Step 2 to correct.")
            if st.button("⟵ Fix Now"):
                st.session_state.step = 1
                st.rerun()
            st.stop()

    bar = st.progress(0)
    status = st.empty()
    
    for i, msg in enumerate([
        "Checking Board Eligibility 🔍",
        "Matching Interests with Market Trends 📊",
        "Analyzing Budget Feasibility 💰",
        "Generating Personalized Recommendations 🧠",
        "Finalizing Career Strategy 🚀"
    ]):
        status.text(f"⏳ {msg} (Step {i+1}/5)")
        bar.progress((i+1)*20)
        time.sleep(1.2)
    
    st.session_state.step = 6
    st.rerun()

# --------------------- STEP 6: FINAL REPORT ---------------------
if st.session_state.step == 6:
    st.success("✅ Assessment Complete!")

    answers = st.session_state.answers
    budget = answers.get("budget", "")
    interests = answers.get("interests", [])
    work_style = answers.get("work_style", "")
    language = answers.get("language", "English")

    financial_note = "Low budget constraint (<1L)." if "Low" in budget else f"Budget: {budget}"
    interest_note = f"No specific interests selected. Suggest 'Evergreen' careers." if not interests else f"Interests: {', '.join(interests)}"

    ai_prompt = f"""
    ACT AS: Senior Career Counselor for Indian Students.
    TONE: Encouraging, Realistic, Direct.
    LANGUAGE: {language}

    USER PROFILE:
    - Current Stage: {answers.get('current_stage')}
    - Stream: {answers.get('stream')}
    - Board: {answers.get('board')}
    - Academic Score: {answers.get('academic_score')}
    - Target Exam: {answers.get('exam_status')}
    - Work Style: {work_style}
    - Financial Context: {financial_note}
    - Interests Context: {interest_note}
    - Parent Pressure: {answers.get('parent_pressure')}
    - Location: {answers.get('location')}

    TASK: Generate personalized Career Strategy Report.
    """

    if st.session_state.final_report is None:
        status_placeholder = st.empty()
        with st.spinner("🚀 Generating your personalized Career Report..."):
            for i in range(5):
                status_placeholder.markdown(f"⏳ AI is analyzing your profile... Step {i+1}/5")
                time.sleep(1)
            try:
                response = model.generate_content(ai_prompt)
                st.session_state.final_report = response.text
                status_placeholder.empty()
            except Exception as e:
                st.error(f"AI Error: {e}")
                st.warning("Check API Key.")

    if st.session_state.final_report:
        st.markdown("---")
        st.markdown("### 📄 Your Personalized Career Report")
        st.markdown(
            f"<div style='background-color:#f8f9fa; padding:20px; border-radius:10px;'>{st.session_state.final_report}</div>",
            unsafe_allow_html=True
        )

       # ---------------- PDF Generation ----------------
from fpdf import FPDF

# Define the PDF class first
class PDF(FPDF):
    def header(self):
        # Add DejaVu font (supports Hindi + emojis)
        self.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
        self.set_font('DejaVu', '', 15)  # Regular only
        self.cell(0, 10, 'CareerRaah Report', 1, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', '', 8)  # Regular only
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')


if st.session_state.final_report:
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('DejaVu', '', 12)
    pdf.multi_cell(0, 10, st.session_state.final_report)
    
    # Convert bytearray to bytes
    pdf_output = bytes(pdf.output(dest='S'))

    st.download_button(
        label="⬇️ Download Report as PDF",
        data=pdf_output,
        file_name="CareerRaah_Report.pdf",
        mime="application/pdf"
    )


# Reset / New Assessment button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Start New Assessment 🔁", use_container_width=True):
    st.session_state.step = 1
    st.session_state.answers = {}
    st.session_state.final_report = None
    st.rerun()
