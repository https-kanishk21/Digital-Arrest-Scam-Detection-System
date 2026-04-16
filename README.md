# 🚨 Digital Arrest Scam Detection System

## 📌 Overview

This project is an AI-based system designed to detect **digital arrest scams** using Machine Learning and Natural Language Processing (NLP).
It analyzes both **text messages and voice input**, converts speech to text, and predicts whether the content is a scam.

---

## ⚡ Features

* 🔍 Detects scam messages using Machine Learning
* 🎤 Supports **voice input (speech-to-text)**
* 📊 Generates a **risk score (%)**
* ⚠ Highlights **suspicious keywords**
* 🌐 Interactive **web interface using Streamlit**
* 🖼 Cybercrime awareness UI with background visualization

---

## 🧠 Technologies Used

* Python
* Scikit-learn (Random Forest)
* TF-IDF Vectorization
* Streamlit (Web UI)
* SpeechRecognition (Voice input)
* Pandas

---

## ⚙️ How It Works

1. User inputs text or speaks
2. Voice is converted into text
3. Text is processed using TF-IDF
4. Random Forest model predicts scam probability
5. System outputs:

   * Risk Score
   * Scam / Safe result
   * Suspicious keywords

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Application

```bash
python -m streamlit run app.py
```

---

## 📁 Project Structure

```
Digital_arrest_project/
│
├── app.py
├── spam.csv
├── image.png
├── requirements.txt
└── README.md
```

---

## 🌍 Deployment

This project can be deployed using **Streamlit Cloud** to generate a public link accessible from anywhere.

---

## ⚠️ Note

* Voice feature works best on local system
* May have limitations on cloud deployment due to browser permissions

---

## 🎯 Conclusion

This system helps users identify and avoid **digital arrest scams** by analyzing suspicious communication patterns in real time.

---

## 👨‍💻 Author

Kanishk Verma
M.Sc Cyber Security
Amity University Rajasthan
