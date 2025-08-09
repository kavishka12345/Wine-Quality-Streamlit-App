# 🍷 Wine Quality Prediction with Streamlit

This project is an assignment to build a complete **machine learning pipeline**, from **data exploration** to **model deployment**.  
It uses the **Wine Quality Dataset** to train a classification model and deploys it as an **interactive web application** using **Streamlit** and **Streamlit Cloud**.

---

## 🌐 Live Demo
🔗 **[Click here to use the app](https://wine-quality-app-app-psblyemq7ttohm34hrkaij.streamlit.app)**

---

## 📊 Dataset
The dataset used for this project is the **Wine Quality Dataset** from Kaggle (`winequality-red.csv`).  
It contains **11 chemical properties** of wine (e.g., fixed acidity, alcohol, pH) and a **quality score**.

For this project:
- The `quality` score was converted into a **binary target**:
  - `good` → score >= 7
  - `bad` → score < 7

---

## 🤖 Model Training
Two algorithms were trained to predict wine quality:
1. **Logistic Regression**
2. **Random Forest Classifier**

**Random Forest Classifier** gave the best performance and was selected for deployment.  
The complete training process, evaluation, and model comparison are available in the [`notebooks/model_training.ipynb`](notebooks/model_training.ipynb) file.

---

## 📂 Project Structure
