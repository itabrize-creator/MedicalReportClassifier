import streamlit as st
import joblib
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# ── Load model and vectorizer ──────────────────────────
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ── Preprocessing function ─────────────────────────────
def preprocess(text):
    text = text.lower()
    tokens = text.split()
    tokens = [w for w in tokens if w.isalpha() and w not in stop_words]
    return " ".join(tokens)

# ── UI ─────────────────────────────────────────────────
st.set_page_config(page_title="Medical Report Classifier", page_icon="🏥")

st.title("🏥 Automated Medical Report Classification")
st.markdown("**IILM University | BTP2CSE312 | CSE (Data Science)**")
st.markdown("---")

st.subheader("📄 Enter Medical Report Text")
user_input = st.text_area(
    "Paste or type medical report content here:",
    height=200,
    placeholder="e.g. Patient presents with chest pain and shortness of breath. ECG shows abnormal rhythm..."
)

if st.button("🔍 Classify Report"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text before classifying.")
    else:
        clean = preprocess(user_input)
        vector = vectorizer.transform([clean])
        prediction = model.predict(vector)[0]

        # Color-coded result
        color_map = {
            "Cardiology": "🔴",
            "Neurology": "🟣",
            "Orthopedics": "🟠",
            "Radiology": "🔵",
            "Pathology": "🟡",
            "General Medicine": "🟢"
        }
        emoji = color_map.get(prediction, "⚪")

        st.success(f"### {emoji} Predicted Category: **{prediction}**")
        st.markdown("---")
        st.info("This classification was performed using an NLP-based Machine Learning model trained on medical report data.")

st.markdown("---")
st.markdown("**Team Members:** Syeda Ina Tabizza | Vaishnavi Sharma | Surbhi Sagar | Arham Nabeel | Toufique Raza")
st.markdown("**Guide:** Mr. Vinay Pratap Mishra")