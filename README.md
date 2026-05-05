# Medical Report Classification using Machine Learning

---

## Team Members
- Syeda Ina Tabrize
- Vaishnavi Sharma  
- Surbhi Sagar  
- Arham Nabeel  
- Taufique Raza  

---

## Guided By
Mr. Vinay Priy Mishra  

---

## Description
This project classifies medical reports into different medical specialties using Natural Language Processing (NLP) and Machine Learning.

The system analyzes the text of a medical report and predicts the appropriate department such as:
- Cardiology  
- Neurology  
- Orthopedics  
- Radiology  
- Pathology  
- General Medicine  

The model uses text preprocessing and vectorization techniques to understand the input and provide accurate classification.

---

## Algorithm Used
- Machine Learning Classification Model (TF-IDF + ML Model)
- Natural Language Processing (NLP)

---

## Dataset
- Medical report dataset containing labeled categories  
- Includes reports related to different medical specialties  

---

## Technologies Used
- Python  
- Streamlit  
- Scikit-learn  
- NLTK  
- Joblib  

---

## How to Run the Project

### Step 1: Install Required Libraries

pip install streamlit scikit-learn nltk joblib

### Step 2: Run web app

py -m streamlit run app/app.py

### Step 3: Open in Browser

After running, open the link shown in terminal (usually http://localhost:8501)

---

## Output

• Predicts the medical department from report text  
• Displays classification result on web interface  

---

## Example Input

Patient reports chest pain, shortness of breath, and abnormal ECG.

---

## Example Output

Predicted Category: Cardiology
---
## Deployment  
The project can be deployed using Streamlit Cloud.

---

##  Note  
This is a Machine Learning model and predictions depend on training data. Accuracy may vary for different inputs.
