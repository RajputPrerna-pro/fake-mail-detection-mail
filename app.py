import streamlit as st
import joblib

# ============================================================
# LOAD MODEL
# ============================================================
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AI MailGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 50%, #f8fafc 100%);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(135deg, #111827, #1e3a8a, #4f46e5);
    padding: 45px 30px;
    border-radius: 25px;
    text-align: center;
    color: white;
    box-shadow: 0 15px 35px rgba(30, 58, 138, 0.25);
    margin-bottom: 28px;
}

.hero-icon {
    font-size: 58px;
}

.hero-title {
    font-size: 44px;
    font-weight: 800;
    margin-top: 8px;
}

.hero-subtitle {
    font-size: 19px;
    margin-top: 8px;
    opacity: 0.92;
}

.hero-tech {
    margin-top: 18px;
    font-size: 14px;
    opacity: 0.85;
}

.stat-card {
    background: white;
    padding: 22px 12px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 22px rgba(0,0,0,0.06);
}

.stat-icon {
    font-size: 30px;
}

.stat-number {
    font-size: 27px;
    font-weight: 800;
    color: #1e3a8a;
    margin-top: 5px;
}

.stat-label {
    color: #64748b;
    font-size: 14px;
    margin-top: 4px;
}

.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #111827;
    margin-top: 18px;
}

.section-description {
    color: #64748b;
    margin-bottom: 18px;
}

.input-card {
    background: white;
    padding: 22px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 25px rgba(0,0,0,0.06);
}

.fake-result {
    background: linear-gradient(135deg, #fff1f2, #ffe4e6);
    border-left: 7px solid #dc2626;
    padding: 24px;
    border-radius: 18px;
    margin-top: 18px;
}

.genuine-result {
    background: linear-gradient(135deg, #ecfdf5, #d1fae5);
    border-left: 7px solid #16a34a;
    padding: 24px;
    border-radius: 18px;
    margin-top: 18px;
}

.result-title {
    font-size: 25px;
    font-weight: 800;
}

.result-text {
    color: #475569;
    margin-top: 8px;
}

.process-card {
    background: white;
    padding: 23px 15px;
    border-radius: 18px;
    text-align: center;
    min-height: 175px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 7px 20px rgba(0,0,0,0.05);
}

.process-number {
    display: inline-block;
    background: #eef2ff;
    color: #3730a3;
    padding: 6px 12px;
    border-radius: 20px;
    font-weight: 700;
}

.process-icon {
    font-size: 32px;
    margin: 10px;
}

.footer {
    text-align: center;
    padding: 30px;
    color: #64748b;
    margin-top: 25px;
}

.footer-line {
    height: 1px;
    background: #dbe3ef;
    margin-bottom: 20px;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #1e293b);
}

[data-testid="stSidebar"] * {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:15px 0;">
        <div style="font-size:55px;">🛡️</div>
        <h2>AI MailGuard</h2>
        <p style="opacity:0.75;">Intelligent Email Security</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### 🤖 Machine Learning")
    st.write("**Algorithm:** Logistic Regression")
    st.write("**Feature Extraction:** TF-IDF")

    st.divider()

    st.markdown("### 📊 Dataset")
    st.write("**Total Emails:** 83,448")
    st.write("**Fake / Spam:** 43,910")
    st.write("**Genuine:** 39,538")

    st.divider()

    st.markdown("### 🎯 Model Performance")
    st.success("98.48% Test Accuracy")

    st.divider()

    st.info(
        "This application uses Natural Language Processing "
        "and Machine Learning to classify email messages."
    )

# ============================================================
# HERO
# ============================================================
st.html("""
<div class="hero">
    <div class="hero-icon">📧</div>
    <div class="hero-title">AI MailGuard</div>
    <div class="hero-subtitle">
        Intelligent Fake &amp; Spam Mail Detection System
    </div>
    <div class="hero-tech">
        🧠 NLP &nbsp; • &nbsp;
        🔤 TF-IDF &nbsp; • &nbsp;
        🤖 Logistic Regression &nbsp; • &nbsp;
        🌐 Streamlit
    </div>
</div>
""")

# ============================================================
# STATISTICS
# ============================================================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.html("""
    <div class="stat-card">
        <div class="stat-icon">🎯</div>
        <div class="stat-number">98.48%</div>
        <div class="stat-label">Model Accuracy</div>
    </div>
    """)

with c2:
    st.html("""
    <div class="stat-card">
        <div class="stat-icon">📧</div>
        <div class="stat-number">83,448</div>
        <div class="stat-label">Email Samples</div>
    </div>
    """)

with c3:
    st.html("""
    <div class="stat-card">
        <div class="stat-icon">🔤</div>
        <div class="stat-number">TF-IDF</div>
        <div class="stat-label">Text Features</div>
    </div>
    """)

with c4:
    st.html("""
    <div class="stat-card">
        <div class="stat-icon">🤖</div>
        <div class="stat-number">ML</div>
        <div class="stat-label">Detection Engine</div>
    </div>
    """)

# ============================================================
# EMAIL ANALYZER
# ============================================================
st.html("""
<div class="section-title">🔍 Analyze Your Email</div>
<div class="section-description">
    Paste an email or message below and let the AI model analyze it.
</div>
""")

left, right = st.columns([1.55, 0.85])

with left:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)

    email_text = st.text_area(
        "📨 Email / Message Content",
        height=280,
        placeholder="""Paste your email here...

Example:
Congratulations! You have won $1,000,000.
Click the link immediately to claim your reward."""
    )

    analyze = st.button(
        "🔍 ANALYZE EMAIL",
        use_container_width=True,
        type="primary"
    )

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.html("""
    <div class="section-title" style="font-size:22px;">
        🧪 Quick Test
    </div>
    <div class="section-description">
        Test the trained model with sample messages.
    </div>
    """)

    suspicious_mail = """Congratulations!
You have won $1,000,000.

You are our lucky winner.
Click the link immediately to claim your prize.
Send your bank details to receive your reward."""

    genuine_mail = """Hi John,

Thank you for your email.
I have received the project report.
I will review the document and get back to you tomorrow.

Regards,
Prerna"""

    if st.button("🚨 Test Suspicious Email", use_container_width=True):
        st.session_state["email_to_test"] = suspicious_mail
        st.session_state["run_prediction"] = True
        st.rerun()

    if st.button("✅ Test Genuine Email", use_container_width=True):
        st.session_state["email_to_test"] = genuine_mail
        st.session_state["run_prediction"] = True
        st.rerun()

    if st.button("🗑️ Clear Test", use_container_width=True):
        st.session_state.pop("email_to_test", None)
        st.session_state["run_prediction"] = False
        st.rerun()

# ============================================================
# USE SAMPLE EMAIL IF SELECTED
# ============================================================
if "email_to_test" in st.session_state:
    email_text = st.session_state["email_to_test"]
    st.text_area(
        "Selected Test Message",
        value=email_text,
        height=160,
        disabled=True
    )

run_prediction = analyze or st.session_state.get("run_prediction", False)
st.session_state["run_prediction"] = False

# ============================================================
# PREDICTION
# ============================================================
if run_prediction:
    if not email_text.strip():
        st.warning("⚠️ Please enter an email message first.")
    else:
        with st.spinner("🤖 AI is analyzing the email..."):
            email_vector = vectorizer.transform([email_text])
            prediction = model.predict(email_vector)[0]

            try:
                probabilities = model.predict_proba(email_vector)[0]
                genuine_probability = float(probabilities[0] * 100)
                fake_probability = float(probabilities[1] * 100)
            except Exception:
                genuine_probability = 0.0
                fake_probability = 0.0

        st.divider()

        st.html("""
        <div class="section-title">📊 AI Detection Result</div>
        """)

        if int(prediction) == 1:
            st.html(f"""
            <div class="fake-result">
                <div class="result-title">🚨 Fake / Spam Mail Detected</div>
                <div class="result-text">
                    The AI model has classified this email as suspicious.
                </div>
                <br>
                <b>AI Confidence: {fake_probability:.2f}%</b>
            </div>
            """)

            st.progress(min(fake_probability / 100, 1.0))

            st.error(
                "⚠️ Safety Alert: Do not click unknown links or share "
                "passwords, OTPs, bank details or other sensitive information."
            )
        else:
            st.html(f"""
            <div class="genuine-result">
                <div class="result-title">✅ Genuine Mail Detected</div>
                <div class="result-text">
                    The AI model has classified this email as genuine.
                </div>
                <br>
                <b>AI Confidence: {genuine_probability:.2f}%</b>
            </div>
            """)

            st.progress(min(genuine_probability / 100, 1.0))

            st.success(
                "The email appears genuine according to the trained "
                "machine learning model."
            )

        st.html("""
        <div class="section-title" style="font-size:22px;">
            📈 Prediction Probability
        </div>
        """)

        p1, p2 = st.columns(2)

        with p1:
            st.metric("🚨 Fake / Spam", f"{fake_probability:.2f}%")

        with p2:
            st.metric("✅ Genuine", f"{genuine_probability:.2f}%")

# ============================================================
# HOW IT WORKS
# ============================================================
st.divider()

st.html("""
<div class="section-title">🧠 How AI MailGuard Works</div>
<div class="section-description">
    The system follows a complete Natural Language Processing
    and Machine Learning pipeline.
</div>
""")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.html("""
    <div class="process-card">
        <div class="process-number">01</div>
        <div class="process-icon">📨</div>
        <h3>Email Input</h3>
        <p>User enters email content.</p>
    </div>
    """)

with s2:
    st.html("""
    <div class="process-card">
        <div class="process-number">02</div>
        <div class="process-icon">🔤</div>
        <h3>TF-IDF</h3>
        <p>Text is converted into numerical features.</p>
    </div>
    """)

with s3:
    st.html("""
    <div class="process-card">
        <div class="process-number">03</div>
        <div class="process-icon">🤖</div>
        <h3>ML Model</h3>
        <p>Logistic Regression analyzes the text.</p>
    </div>
    """)

with s4:
    st.html("""
    <div class="process-card">
        <div class="process-number">04</div>
        <div class="process-icon">🎯</div>
        <h3>Prediction</h3>
        <p>Fake/Spam or Genuine result is generated.</p>
    </div>
    """)

# ============================================================
# MODEL INFORMATION
# ============================================================
st.divider()

with st.expander("📚 About This Machine Learning Model"):
    st.markdown("""
### 🔬 Model Details

- **Problem:** Email Text Classification
- **Dataset:** 83,448 email samples
- **Feature Extraction:** TF-IDF Vectorization
- **Algorithm:** Logistic Regression
- **Test Accuracy:** 98.48%

### 🎯 Classes

- 🚨 Fake / Spam
- ✅ Genuine

### 🛠️ Technologies

Python • Pandas • Scikit-learn • TF-IDF • Logistic Regression • Joblib • Streamlit
""")


# ============================================================
# FOOTER
# ============================================================
st.html("""
<div class="footer">
    <div class="footer-line"></div>
    <h3>🛡️ AI MailGuard</h3>
    <p>AI-Based Fake &amp; Spam Mail Detection System</p>
    <p>Built with Python • Machine Learning • NLP • Streamlit</p>
    <p>Model: Logistic Regression &nbsp;|&nbsp; Features: TF-IDF</p>

    <p style="font-size:17px; font-weight:700; color:#1e3a8a;">
        👩‍💻 Developed by Prerna Rajput
    </p>

    <p>
        BCA Student • COER University, Roorkee
    </p>

    <p>© 2026 AI MailGuard</p>
</div>
""")