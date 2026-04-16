# 🚨 Digital Arrest Scam Detection System

An AI-powered web application that detects **Digital Arrest scams** using both **text and voice input**.  
Built using Machine Learning and deployed with an interactive UI for real-time fraud detection.

---

## 🔍 Overview

Digital arrest scams are increasing rapidly where attackers impersonate authorities (CBI, Police, etc.) and threaten victims.

This project detects such scams by analyzing:
- 📩 Text messages
- 🎤 Voice input (converted to text)

---

## ⚙️ Features

- 🧠 Machine Learning-based scam detection (Random Forest)
- 📊 Risk score calculation (0–100%)
- 📈 Graphical visualization (Gauge + Bar Chart)
- 🎤 Voice-to-text detection
- ⚠️ Suspicious keyword detection
- 🌐 Interactive Streamlit UI
- 🧾 Real-time analysis with confidence score

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit  
- **Machine Learning**: Scikit-learn (Random Forest)  
- **Text Processing**: TF-IDF Vectorizer  
- **Voice Processing**: SpeechRecognition  
- **Visualization**: Plotly  
- **Language**: Python  

---

## 📂 Dataset

- 📌 Spam dataset (spam.csv)
- 📌 Custom Digital Arrest dataset
- 📌 Hindi/Hinglish dataset

👉 Dataset includes scam-related phrases like:
- “CBI warrant issued”
- “Transfer money immediately”
- “Digital arrest notice”

---

## 🧠 Model Details

- Algorithm: Random Forest Classifier  
- Feature Extraction: TF-IDF  
- Output:
  - Risk Score (%)
  - Scam / Safe Prediction  
  - Confidence Level  

---

## 📊 Output Visualization

The system provides:

- 📉 Risk Score Progress Bar  
- 🎯 Gauge Chart (Risk Level)  
- 📊 Scam vs Safe Probability Chart  
- 🧠 Model Confidence  

---

## 🚀 How to Run

### 1. Clone Repository

```bash
git clone https://github.com/https-kanishk21/Digital-Arrest-Scam-Detection-System.git
cd Digital-Arrest-Scam-Detection-System