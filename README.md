# 🍷 Wine Quality Prediction App

An end-to-end **Machine Learning project** that predicts wine quality based on its chemical properties.  
This project covers the full pipeline: **data exploration → model training → deployment** using **Streamlit**.

---

## 🌐 Live App
🔗 **[Try the App Here](https://wine-quality-app-app-psblyemq7ttohm34hrkaij.streamlit.app)**

---

## 📖 Overview
Wine quality is determined by various physicochemical tests. This app uses a **Random Forest Classifier** to predict whether a wine is **"Good"** or **"Bad"** based on 11 features.

Users can:
- Explore the dataset interactively
- Visualize data distributions and correlations
- Enter wine parameters via sliders
- Get instant quality predictions

---

## 📊 Dataset
- **Source:** [Kaggle – Wine Quality Dataset](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)
- **Features:** 11 numerical variables (e.g., acidity, alcohol, pH)
- **Target:** Binary classification  
  - `1` → Good (quality ≥ 7)  
  - `0` → Bad (quality < 7)  

---

## 🧠 Model Development
### Steps:
1. **Data Cleaning & EDA** – Checked missing values, visualized distributions, correlations
2. **Feature Selection** – Kept 11 main features matching the app sliders
3. **Model Training** – Compared:
   - Logistic Regression
   - Random Forest Classifier ✅ *(Selected best model)*
4. **Model Evaluation** – Accuracy & confusion matrix
5. **Deployment** – Saved model with `joblib` and built Streamlit UI

---

## 📂 Project Structure
