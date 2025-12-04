import streamlit as st
import time
import google.generativeai as genai

# --- 0. PAGE CONFIG ---
st.set_page_config(
    page_title="CareerRaah",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 1. AI CONFIGURATION (SECURE) ---
api_key = None
try:
    # Try loading from Streamlit Secrets (Best Practice)
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]

    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
    else:
        st.error("❌ Google API Key not found!")
        st.warning("Please add your GOOGLE_API_KEY to the .streamlit/secrets.toml file.")
        st.stop()

except Exception as e:
    st.error(f"❌ AI Config Error: {e}")
    st.stop()

# --- 2. CSS & UI SETUP ---
st.markdown("""
<style>
    /* Base font and layout */
    html, body, [class*="st-"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    }
    /* Main app container */
    .block-container {
        padding: 1rem 1rem 3rem 1rem; /* Less padding on sides, more at bottom */
    }
    /* Hide Streamlit's default header and footer */
    header, footer {
        visibility: hidden;
    }
    /* Card layout for welcome screen */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
        justify-content: center;
    }
    .card {
        border: 1px solid #ddd;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        background-color: #f9f9f9;
    }
    .card b {
        font-size: 1.1rem;
        display: block;
        margin-bottom: 0.5rem;
    }
    /* Progress steps */
    .step-wrapper { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px; margin-bottom: 20px; }
    .step-item { display: flex; align-items: center; font-size: 14px; padding: 8px 12px; background: #f5f5f5; border-radius: 6px; white-space: nowrap; border: 1px solid #ddd; color: #555; }
    .step-item.active { background: #FF6B00; color: white; font-weight: 600; border-color: #FF6B00; }
    .arrow { font-size: 18px; font-weight: bold; padding: 0 4px; color: #ccc; }
    @media (max-width: 600px) { 
        .step-item { font-size: 12px; padding: 6px 8px; } 
        .arrow { font-size: 14px; padding: 0 2px; } 
        .block-container { padding: 1rem 1rem 2rem 1rem; }
    }
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
if st.session_state.step == 1 and st.session_state.final_report is None:
    st.markdown("""
    <div style='text-align:center; padding:30px 10px; background:#1A3C8D; color:white; border-radius:12px;'>
        <h1 style='margin-bottom:10px;'>🚀 Welcome to CareerRaah!</h1>
        <p style='font-size:16px;'>Discover your ideal career path with our AI-powered assessment. Quick, personal, and actionable!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🚀 Why Choose CareerRaah?")
    st.markdown("""
    <div class='card-grid'>
        <div class='card' style='background:#FFF8E1;'><b>🤖 AI Report</b><p>Tailored roadmap in 5 mins.</p></div>
        <div class='card' style='background:#E8F5E9;'><b>🎯 Realistic</b><p>Aligned with grades & budget.</p></div>
        <div class='card' style='background:#F3E5F5;'><b>📱 Mobile</b><p>Works on any device.</p></div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

# --------------------- STEP 1: PROFILE ---------------------
if st.session_state.step == 1:
    render_arrow_steps(1)
    st.subheader("Step 1: Academic Profile")
    current_stage = st.radio(
        "Which class/academic stage are you in?", 
        ["Class 8-10 (High School)", "Class 11-12 (Higher Secondary)", "College / Graduate", "Post Graduate", "Gap Year"], 
        horizontal=True
    )
    st.session_state.answers["current_stage"] = current_stage

    # --- Conditional Questions based on Academic Stage ---
    if current_stage in ["College / Graduate", "Post Graduate"]:
        university = st.text_input("Which University/College?")
        st.session_state.answers["university"] = university

        stream = st.text_input("Which stream are you pursuing?")
        st.session_state.answers["stream"] = stream

        # New: Ask about current goal
        goal = st.radio(
            "What is your current primary goal?",
            ["Get a Job", "Pursue Higher Studies", "Entrepreneurship / Startup", "Skill Development / Certification", "Other"]
        )
        st.session_state.answers["current_goal"] = goal

        # Optional: Industry or field preference
        industry = st.text_input("If applicable, which industry or field interests you the most?")
        st.session_state.answers["industry_preference"] = industry

        # Optional: Time horizon for goal
        time_horizon = st.selectbox(
            "What is your expected timeline to achieve this goal?",
            ["0-6 months", "6-12 months", "1-3 years", "3-5 years", "5+ years"]
        )
        st.session_state.answers["goal_timeline"] = time_horizon

    elif current_stage == "Gap Year":
        st.info("Understanding your gap year helps us tailor recommendations.")
        gap_degree = st.text_input("Which degree did you complete before the gap?")
        st.session_state.answers["gap_degree"] = gap_degree
        
        gap_year_completed = st.text_input("When did you complete it (Year)?")
        st.session_state.answers["gap_year_completed"] = gap_year_completed

        gap_duration = st.number_input("How many years is your gap?", min_value=1, max_value=10, step=1)
        st.session_state.answers["gap_duration"] = gap_duration

        gap_aspiration = st.text_area(
            "What is your main aspiration now? (e.g., prepare for an exam, explore a new field, get a job, etc.)"
        )
        st.session_state.answers["gap_aspiration"] = gap_aspiration

    elif current_stage == "Class 11-12 (Higher Secondary)":
        board = st.selectbox("Which Education Board?", ["CBSE (Central Board)", "ICSE / ISC (CISCE)", "State Board (HSC/SSC)", "IB / IGCSE (International)", "Open School (NIOS)"])
        st.session_state.answers["board"] = board
        stream = st.selectbox("Select your Stream:", ["Science (PCM) - Engineering Focus", "Science (PCB) - Medical Focus", "Science (PCMB) - General", "Commerce with Maths", "Commerce without Maths", "Humanities / Arts", "Diploma / Vocational"])
        st.session_state.answers["stream"] = stream

    else:  # Class 8-10 (High School)
        board = st.selectbox("Which Education Board?", ["CBSE (Central Board)", "ICSE / ISC (CISCE)", "State Board (HSC/SSC)", "IB / IGCSE (International)", "Open School (NIOS)"])
        st.session_state.answers["board"] = board
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
    
    st.session_state.answers["exam_status"] = st.multiselect(
        "Are you preparing for any entrance exams? (Select one or more)",
        [
            "No, focusing on Boards",
            "JEE (Main/Advanced)",
            "NEET (Medical)",
            "BITSAT",
            "VITEEE / SRMJEEE / Other Pvt Engineering",
            "CUET (Central Universities)",
            "IPMAT (IIM Indore/Rohtak)",
            "CLAT (Law)",
            "AILET (NLU Delhi)",
            "NDA (Defence)",
            "CDS (Graduates, Defence)",
            "CA Foundation",
            "CS Foundation",
            "CMA Foundation",
            "Banking Exams (SBI/IBPS)",
            "UPSC (CSE)",
            "State PSC",
            "SSC (CGL/CHSL)",
            "RRB (Railways)",
            "Design (NID/NIFT/UCEED/CEED)",
            "Hotel Management (NCHM-JEE)",
            "Architecture (NATA)",
            "Agriculture (ICAR AIEEA)",
            "Pharmacy (GPAT)",
            "Aviation (CPL / AME)",
            "Mass Communication (IIMC/JMI)",
            "Fine Arts (BFA Entrance)",
            "Paramedical Entrance",
            "BBA/BMS Entrance",
            "MCA Entrance (NIMCET/State CET)",
            "Cybersecurity / Skill-Based Certifications",
            "Foreign Exams (SAT/IELTS/TOEFL)"
        ]
    )

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
    st.session_state.answers["work_style"] = st.radio("", ["No Preference","I want a Desk Job (AC Office, Laptop)", "I want Field Work (Travel, Sites, interaction)", "I want a Creative Studio (Art, Design, Freedom)", "I want Uniform/Discipline (Defense, Pilot, Merchant Navy)"], label_visibility="collapsed")

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
    
    st.session_state.answers["location"] = st.radio("Where do you want to study?", ["No Preference","Home Town (Day Scholar)", "Metro City (Hostel OK)", "Abroad (High Budget)"])

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

    # --- VALIDATION ---
    stream = st.session_state.answers.get("stream", "")
    exam = st.session_state.answers.get("exam_status", "")
    if "Commerce" in stream or "Humanities" in stream or "Arts" in stream:
        if exam in ["NEET", "JEE (Mains/Adv)"]:
            st.error("⚠️ Conflict Detected: Your stream does not align with selected entrance exam.")
            if st.button("⟵ Fix Now"):
                st.session_state.step = 1
                st.rerun()
            st.stop()

    bar = st.progress(0)
    status = st.empty()
    for i, msg in enumerate(["Checking Board Eligibility 🔍", "Matching Interests with Market Trends 📊", "Analyzing Budget Feasibility 💰", "Generating Personalized Recommendations 🧠", "Finalizing Career Strategy 🚀"]):
        status.text(f"⏳ {msg} (Step {i+1}/5)")
        bar.progress((i+1)*20)
        time.sleep(0.8)
    
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

    # Set language instruction for the AI
    if language == "Hindi":
        output_language_instruction = (
            "Write the response in Hinglish. Hindi must be written in Devanagari script, "
            "and English words must remain in English script. The style should match this example: "
            "'कल मेरा exam है, so मुझे पढ़ना है।' "
            "Use natural Hindi sentence structure with smooth English mixing. "
            "Do NOT translate English words into Hindi. Keep it conversational, modern, and easy to read."
            "Use Hinglish/English as specified. Maintain professional yet student-friendly tone."
        )
    else:
        output_language_instruction = language

    financial_note = "Low budget constraint (<1L)." if "Low" in budget else f"Budget: {budget}"
    interest_note = f"No specific interests selected." if not interests else f"Interests: {', '.join(interests)}"

    ai_prompt = f"""
    ACT AS: Senior Career Counselor & Education Strategist for Indian Students.
    You deeply understand Indian boards (CBSE/ICSE/State), competitive exams (JEE/NEET/CLAT), budgets, job-market realities, and modern skill demands.

    TONE:
    Encouraging, Motivational, Practical, Structured, and Realistic — like a mentor who pushes students but guides them safely.

    OUTPUT LANGUAGE:
    Use {output_language_instruction}.

    USER PROFILE CONTEXT:
    - Current Stage: {answers.get('current_stage')}
    - Stream: {answers.get('stream')}
    - Academics: {answers.get('academic_score')} (Adjust difficulty of advice based on this).
    - Financial: {financial_note} (CRITICAL: Strictly adhere to this budget).
    - Interests: {interest_note}
    - Location Preference: {answers.get('location')}
    - Current Goal: {answers.get('current_goal', 'Not specified')}
    - Industry Preference: {answers.get('industry_preference', 'Not specified')}
    - Goal Timeline: {answers.get('goal_timeline', 'Not specified')}
    - Gap Year Aspiration: {answers.get('gap_aspiration', 'Not specified')}
    - Full Profile: {answers}

    TASK:
    Generate a highly personalized **Career Strategy Report**.
    Tailor advice to the user's **current goal**, **industry preference**, and **timeline**.
    Include step-by-step actionable guidance, milestone planning, and resource recommendations.


    THE REPORT MUST INCLUDE:

    ### 1. 📝 Executive Summary
    * Who you are (Profile Snapshot)
    * Your Core Strengths
    * Recommended Career Clusters (Primary & Secondary)

    ### 2. 🏆 Top 3 Best-Fit Career Paths
    (For each path, provide):
    * **Why it fits:** (Connect to their specific interests/strengths)
    * **The Path:** (Entrance Exams -> Degree -> Job Role)
    * **Reality Check:** Difficulty Level (Easy/Medium/Hard) & Success Rate
    * **Financials:** Approx College Fees vs Starting Salary (India)

    ### 3. 🗺️ Year-by-Year Roadmap
    (Create a timeline from *Current Stage* to *First Job*)
    * **Immediate (Next 3 Months):** Specific chapters/skills to focus on.
    * **Short Term (1 Year):** Exams to target.
    * **Long Term (3-4 Years):** Internships & Specializations.

    ### 4. 🛠️ Skill Development (Zero to Hero)
    * **Tech Stack:** (Languages/Tools specific to their path)
    * **Soft Skills:** (Communication/Leadership)
    * **Free Resources:** (Specific YouTube Channels, NPTEL, Coursera links)

    ### 5. 🏫 College & Exam Strategy (Budget Aligned)
    | Category | College/Exam Option | Est. Fees | ROI (Placement) |
    | :--- | :--- | :--- | :--- |
    | **Dream** | (Top Tier option) | ... | ... |
    | **Realistic** | (Good Tier-2 option) | ... | ... |
    | **Safety** | (Local/Govt option) | ... | ... |

    ### 6. 💼 Job Market Reality (2025-2030)
    * **Trending Roles:** What will be hot when they graduate?
    * **Threats:** Is AI impacting this field? How to stay safe.
    * **Salary Growth:** Expected salary curve (Fresher -> 5 Years Exp).

    ### 7. 👨‍👩‍👧 Family & Plan B (Crucial)
    * **The Backup Plan:** If the primary goal fails, what is the safe fallback?
    * **For Parents:** A dedicated note explaining the ROI and safety of this path.

    ### 8. ✅ Final Action Checklist
    * [ ] Task 1 (Do this today)
    * [ ] Task 2 (Do this week)
    * [ ] Task 3 (Do this month)

    STYLE RULES:
    - Use Markdown tables for comparisons.
    - Use bullet points for readability.
    - NO generic advice ("Work hard"). Give specific advice ("Solve HC Verma Chapter 1").
    - Strictly respect the User's Budget constraint in college recommendations.

    END WITH:
    A short, punchy motivational quote specific to their journey.

    NOTE: Depending on the current goal, prioritize sections accordingly:
    - Job: Skills, Internships, Job Market Reality
    - Higher Studies: College & Exam Strategy, Roadmap
    - Skill/Certifications: Skill Development, Projects, Free Resources
    """

    if st.session_state.final_report is None:
        with st.spinner("🚀 Generating your personalized Career Report..."):
            try:
                response = model.generate_content(ai_prompt)
                st.session_state.final_report = response.text
            except Exception as e:
                st.error(f"AI Error: {e}")
                st.warning("Check API Key.")

    if st.session_state.final_report:
        st.markdown("---")
        st.markdown("### 📄 Your Personalized Career Report")
        st.markdown(f"<div style='background-color:#f8f9fa; padding:20px; border-radius:10px;'>{st.session_state.final_report}</div>", unsafe_allow_html=True)

        # ---------------- TEXT FILE DOWNLOAD (Robust Alternative) ----------------
        report_text = st.session_state.final_report
        
        col_d1, col_d2 = st.columns(2)
        
        with col_d1:
            st.download_button(
                label="⬇️ Download as Text File",
                data=report_text,
                file_name="CareerRaah_Report.txt",
                mime="text/plain",
                use_container_width=True
            )
            
        with col_d2:
            st.download_button(
                label="⬇️ Download as Markdown",
                data=report_text,
                file_name="CareerRaah_Report.md",
                mime="text/markdown",
                use_container_width=True
            )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start New Assessment 🔁", use_container_width=True):
        st.session_state.step = 1
        st.session_state.answers = {}
        st.session_state.final_report = None
        st.rerun()