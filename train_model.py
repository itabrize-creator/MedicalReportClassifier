import pandas as pd
import numpy as np
import nltk
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

# ── Load Data ──────────────────────────────────────────
df = pd.read_csv("medical_data.csv")
print("Dataset loaded. Shape:", df.shape)

# ── Text Preprocessing ─────────────────────────────────
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    tokens = text.split()
    tokens = [w for w in tokens if w.isalpha() and w not in stop_words]
    return " ".join(tokens)

df["clean_text"] = df["report"].apply(preprocess)

# ── Feature Extraction (TF-IDF) ────────────────────────
vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df["clean_text"])
y = df["category"]

# ── Train/Test Split ───────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ── Train Multiple Models ──────────────────────────────
models = {
    "Naive Bayes": MultinomialNB(),
    "SVM": LinearSVC(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

results = {}
best_acc = 0
best_model = None
best_name = ""

print("\n📊 Model Comparison:")
print("-" * 40)

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    print(f"{name}: {acc*100:.2f}%")
    if acc > best_acc:
        best_acc = acc
        best_model = model
        best_name = name

print(f"\n🏆 Best Model: {best_name} ({best_acc*100:.2f}%)")

# ── Detailed Report for Best Model ────────────────────
y_pred_best = best_model.predict(X_test)
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred_best))

#print("✅ Model comparison chart saved as model_comparison.png")

# ── Save Best Model & Vectorizer ───────────────────────
joblib.dump(best_model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print(f"\n✅ Model saved as model.pkl")
print("✅ Vectorizer saved as vectorizer.pkl")