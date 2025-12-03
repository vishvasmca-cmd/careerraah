import streamlit as st
from fpdf import FPDF
import time
import google.generativeai as genai

# --- 1. AI CONFIGURATION ---
# NOTE: Replace this with a valid API Key starting with 'AIza' if this one fails.
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

# --- PAGE HEADER ---
st.markdown("<h3 style='text-align:center; color:#1A3C8D;'>🚀 CareerRaah Assessment</h3>", unsafe_allow_html=True)
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

    # --- VALIDATION LOGIC GATE ---
    stream = st.session_state.answers.get("stream", "")
    exam = st.session_state.answers.get("exam_status", "")
    subjects = st.session_state.answers.get("strong_subjects", [])
    
    # Rule 1: Commerce/Arts cannot take NEET
    if "Commerce" in stream or "Humanities" in stream or "Arts" in stream:
        if exam == "NEET":
            st.error("⚠️ **Conflict Detected:** You selected 'NEET' (Medical) but your stream is Commerce/Arts.")
            st.info("💡 **Fix:** Please go back to Step 1 to change your Stream OR Step 2 to change your Exam.")
            if st.button("⟵ Fix Stream (Step 1)"):
                st.session_state.step = 1
                st.rerun()
            st.stop()

    # Rule 2: Commerce/Arts cannot take JEE
    if "Commerce" in stream or "Humanities" in stream or "Arts" in stream:
        if "JEE" in exam:
            st.error("⚠️ **Conflict Detected:** You selected 'JEE' (Engineering) but your stream is Commerce/Arts.")
            st.info("💡 **Fix:** Engineering requires Physics, Chemistry & Maths.")
            if st.button("⟵ Fix Stream (Step 1)"):
                st.session_state.step = 1
                st.rerun()
            st.stop()

    # Rule 3: Subject Match Logic
    if "PCB" in stream and "Mathematics" in subjects:
        st.warning("ℹ️ **Note:** You selected Biology stream but listed Maths as strong. We assume you took PCMB (Maths Optional).")

    # Fake loading steps
    bar = st.progress(0)
    status = st.empty()
    
    time.sleep(0.5)
    status.text("Checking Board Eligibility...")
    bar.progress(30)
    
    time.sleep(0.5)
    
    user_interests = st.session_state.answers.get('interests', [])
    if not user_interests:
        status.text("No specific interests found. Analyzing Market Trends...")
    else:
        status.text(f"Matching with {user_interests[0]} trends...")
    
    bar.progress(60)
    
    time.sleep(0.5)
    status.text("Calculating Budget Feasibility...")
    bar.progress(100)
    status.text("Report Generated!")
    
    time.sleep(0.5)
    st.session_state.step = 6
    st.rerun()

# --------------------- STEP 6: FINAL REPORT (With AI Generation) ---------------------
if st.session_state.step == 6:
    st.success("✅ **Assessment Complete!**")

    # 1. Prepare Data Context
    answers = st.session_state.answers
    budget = answers.get("budget", "")
    interests = answers.get("interests", [])
    work_style = answers.get("work_style", "")
    language = answers.get("language", "English")

    # 2. Financial & Interest Logic
    financial_note = ""
    if "Low" in budget:
        financial_note = "Constraint: Low Budget (<1L). Exclude private colleges like Manipal/VIT. Focus heavily on Govt Colleges, State CETs, and Fee Waiver Schemes (TFW)."
    else:
        financial_note = f"Budget: {budget}"

    interest_note = ""
    if not interests:
        interest_note = f"Constraint: No specific interests selected. Suggest 'Evergreen' high-growth careers relevant to {work_style}."
    else:
        interest_note = f"Interests: {', '.join(interests)}"

    # 3. Construct the AI Prompt
    ai_prompt = f"""
    ACT AS: Senior Career Counselor for Indian Students.
    TONE: Encouraging, Realistic, and Direct.
    LANGUAGE: Generate the entire report in {language}.

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

    TASK:
    Generate a personalized "Career Strategy Report" in Markdown format, following all instructions above.

    STRUCTURE:
    1. 🎯 **The Verdict**: A 2-line summary of the best path.
    2. 🛑 **Reality Check**: Honest feedback on their goals vs. academics/budget (e.g., if marks are low but goal is IIT, suggest Plan B).
    3. 🗺️ **The Roadmap**: 3 clear steps they must take in the next 6 months.
    4. 💡 **Pro Tip**: A specific hack (e.g., "Use Fee Waiver scheme" or "Focus on Chapter 4 of NCERT").
    """

    # 4. Call the AI (Only if not already generated)
    if st.session_state.final_report is None:
        with st.spinner("🤖 AI is writing your report... (This takes 5 seconds)"):
            try:
                response = model.generate_content(ai_prompt)
                st.session_state.final_report = response.text
            except Exception as e:
                st.error(f"AI Error: {e}")
                st.warning("Please check your API Key.")

    # 5. Display the Report
    if st.session_state.final_report:
        st.markdown("---")
        st.markdown("### 📄 Your Personalized Career Report")

        st.markdown(f"""
        <div style="background-color: #f8f9fa; border: 1px solid #ddd; padding: 20px; border-radius: 10px; color: #333;">
            {st.session_state.final_report}
        </div>
        """, unsafe_allow_html=True)

        # --- PDF Generation ---
        class PDF(FPDF):
            def header(self):
                self.set_font('Arial', 'B', 15)
                self.cell(0, 10, 'CareerRaah Report', 1, 0, 'C')
                self.ln(20)

            def footer(self):
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

        pdf = PDF()
        pdf.add_page()
        
        report_text = st.session_state.final_report
        
        # Set font based on language, with a fallback for Hindi.
        if language == "Hindi":
            try:
                # This requires the 'gargi.ttf' font file to be in the same directory or a standard font path.
                pdf.add_font('gargi', '', 'gargi.ttf', uni=True)
                pdf.set_font('gargi', '', 14)
            except FileNotFoundError:
                # Fallback to Arial if Hindi font is not found.
                st.warning("Could not find Hindi font ('gargi.ttf'). PDF will not render Hindi text correctly.")
                pdf.set_font('Arial', '', 12)
        else: # English
            pdf.set_font('Arial', '', 12)

        pdf.multi_cell(0, 10, report_text)
        
        pdf_output = bytes(pdf.output())

        st.download_button(
            label="⬇️ Download Report as PDF",
            data=pdf_output,
            file_name="CareerRaah_Report.pdf",
            mime="application/pdf"
        )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start New Assessment 🔁", use_container_width=True):
        st.session_state.step = 1
        st.session_state.answers = {}
        st.session_state.final_report = None
        st.rerun()