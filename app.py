import speech_recognition as sr
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Digital Arrest Detector",
    page_icon="🚨",
    layout="centered"
)

import base64

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

img_base64 = get_base64_image("image.png")

# Apply background
st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/png;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

.stApp::before {{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.75);
    z-index: -1;
}}
</style>
""", unsafe_allow_html=True)


# -------------------------
# KEYWORDS
# -------------------------
suspicious_keywords = [
    "arrest", "aadhaar", "cbi", "police", "legal",
    "warrant", "transfer", "money", "investigation",
    "cyber", "crime", "account", "urgent"
]

# -------------------------
# LOAD DATASET
# -------------------------
df = pd.read_csv("spam.csv", encoding="latin-1")

df = df[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# -------------------------
# ADD DIGITAL ARREST DATA
# -------------------------
custom_data = {
    "label": [1]*20,
    "message": [
        "Your Aadhaar is linked to illegal transactions.",
        "CBI has issued digital arrest warrant.",
        "Cyber Crime Department is investigating your account.",
        "Transfer money to avoid legal action.",
        "Video call verification required immediately.",
        "Your bank account will be frozen by police.",
        "Immediate payment required to avoid arrest.",
        "Police complaint filed against your Aadhaar.",
        "Your PAN is used in money laundering case.",
        "Income tax department investigation notice.",
        "Legal action will be taken against you.",
        "Your mobile number is under cyber crime investigation.",
        "Call immediately to avoid arrest.",
        "Supreme Court warrant issued in your name.",
        "Transfer funds for verification process.",
        "Your SIM card involved in illegal activity.",
        "National Crime Bureau has issued notice.",
        "Digital arrest order has been generated.",
        "Cyber cell requires immediate payment.",
        "Failure to respond will lead to legal action."
    ]
}

custom_df = pd.DataFrame(custom_data)
df = pd.concat([df, custom_df], ignore_index=True)
# Load Hindi dataset# Load Hindi dataset
hindi_df = pd.read_csv("digital_arrest_hindi_dataset.csv")

# Use Hinglish text
hindi_df = hindi_df[['text_hinglish', 'label']]

# Rename to match model
hindi_df.columns = ['message', 'label']

hindi_df = hindi_df.dropna()
df = pd.concat([df, hindi_df], ignore_index=True)


# -------------------------
# MODEL TRAINING
# -------------------------
vectorizer = TfidfVectorizer(stop_words='english', max_features=3000)
X = vectorizer.fit_transform(df['message'])
y = df['label']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# -------------------------
# UI DESIGN
# -------------------------
#Title
st.markdown("""
<h1 style='text-align: center; color: #ff4b4b; 
background-color: rgba(0,0,0,0.6); 
padding: 15px; border-radius: 10px;'>
🚨 Digital Arrest Scam Detector
</h1>
""", unsafe_allow_html=True)

#Subtitle
st.markdown("""
<h3 style='text-align: center; color: white;'>
⚡ AI Powered Cyber Fraud Detection System
</h3>
""", unsafe_allow_html=True)



st.markdown("### 🛡️ Enter message or use voice to detect scam")

user_input = st.text_area("✉️ Enter Message Here:")

col1, col2 = st.columns(2)

with col1:
    check_btn = st.button("🔍 Check Scam")

with col2:
    voice_btn = st.button("🎤 Use Voice Input")

# -------------------------
# TEXT INPUT DETECTION
# -------------------------
if check_btn:
    if user_input.strip() != "":
        with st.spinner("🔍 Analyzing with AI model..."):

            st.write("📥 Input received")

            # Step 1
            test_vector = vectorizer.transform([user_input])
            st.success("✔ Detecting if it is a Scam ")

            # Step 2
            probability = model.predict_proba(test_vector)
            st.success("✔ Prediction completed")

            risk_score = probability[0][1] * 100

        st.subheader(f"Risk Score: {risk_score:.2f}%")
        st.progress(int(risk_score))

        # -------------------------
        # 📊 GAUGE CHART
        # -------------------------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_score,
            title={'text': "Risk Level"},
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 30], 'color': "green"},
                    {'range': [30, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "red"},
                ],
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

        # -------------------------
        # 📈 BAR CHART
        # -------------------------
        data = {
            "Type": ["Safe", "Scam"],
            "Probability": [100 - risk_score, risk_score]
        }
        fig2 = px.bar(data, x="Type", y="Probability", color="Type")
        st.plotly_chart(fig2, use_container_width=True)

        # -------------------------
        # 🧠 CONFIDENCE
        # -------------------------
       

        # -------------------------
        # 🚨 ALERT SYSTEM
        # -------------------------
        if risk_score > 70:
            st.error("🚨 HIGH RISK SCAM")
        elif risk_score > 40:
            st.warning("⚠️ MEDIUM RISK")
        else:
            st.success("✅ LOW RISK - SAFE")

        # Keyword detection
        found_keywords = [
            word for word in suspicious_keywords
            if word in user_input.lower()
        ]

        if found_keywords:
            st.warning(f"⚠ Suspicious Keywords: {', '.join(found_keywords)}")

    else:
        st.warning("Please enter a message")
# -------------------------
# VOICE INPUT DETECTION
# -------------------------
if voice_btn:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎤 Listening... Speak for up to 1 minute")
        recognizer.pause_threshold = 1.5
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=60)

    try:
        voice_text = recognizer.recognize_google(audio, language="en-IN")
        st.success(f"You said: {voice_text}")
        st.success("✔ Speech converted to text")

        with st.spinner("🔍 Analyzing voice input..."):

            st.write("📥 Input received from microphone")

            # Step 1
            test_vector = vectorizer.transform([voice_text])
            st.success("✔ Detecting if it is a SCAM!")

            # Step 2
            probability = model.predict_proba(test_vector)
            st.success("✔ Prediction completed")

            risk_score = probability[0][1] * 100

        risk_score = probability[0][1] * 100

        st.subheader(f"Risk Score: {risk_score:.2f}%")
        st.progress(int(risk_score))

        # 📊 GAUGE
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_score,
            title={'text': "Risk Level"},
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 30], 'color': "green"},
                    {'range': [30, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "red"},
                ],
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

        # 📈 BAR
        data = {
            "Type": ["Safe", "Scam"],
            "Probability": [100 - risk_score, risk_score]
        }
        fig2 = px.bar(data, x="Type", y="Probability", color="Type")
        st.plotly_chart(fig2, use_container_width=True)

        

        # 🚨 ALERT
        if risk_score > 70:
            st.error("🚨 HIGH RISK SCAM")
        elif risk_score > 40:
            st.warning("⚠️ MEDIUM RISK")
        else:
            st.success("✅ LOW RISK - SAFE")

        # Keyword detection
        found_keywords = [
            word for word in suspicious_keywords
            if word in voice_text.lower()
        ]

        if found_keywords:
            st.warning(f"⚠ Suspicious Keywords: {', '.join(found_keywords)}")

    except:
        st.error("❌ Could not understand audio")

# -------------------------
# STYLING
# -------------------------
st.markdown("""
<style>
h1 {
    text-align: center;
    color: #ff4b4b;
}
.stTextArea textarea {
    background-color: #1e1e1e;
    color: white;
    border-radius: 10px;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)