import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Load model
model = joblib.load("model.pkl")

# Load dataset
df = pd.read_csv("data/winequality.csv")

# Sidebar Navigation
st.sidebar.title("🍷 Wine Quality App")
menu = st.sidebar.radio("Navigate", ["Home", "Data Exploration", "Prediction"])

# Home Page
if menu == "Home":
    st.title("🍷 Wine Quality Prediction")
    st.write("""
        This app predicts wine quality (Good or Bad) based on physicochemical properties.
        Use the **Prediction** page to test the model or **Data Exploration** to view the dataset.
    """)

# Data Exploration Page
elif menu == "Data Exploration":
    st.header("📊 Dataset Overview")
    st.write("Shape of dataset:", df.shape)
    st.write(df.head())

    # Select feature to plot
    feature = st.selectbox("Select feature to visualize", df.columns[:-1])
    fig = px.histogram(df, x=feature, color="quality", barmode="overlay")
    st.plotly_chart(fig)

# Prediction Page
elif menu == "Prediction":
    st.header("🔮 Predict Wine Quality")
    st.write("Move the sliders to set feature values:")

    fixed_acidity = st.slider("Fixed Acidity", 0.0, 20.0, 7.4)
    volatile_acidity = st.slider("Volatile Acidity", 0.0, 2.0, 0.7)
    citric_acid = st.slider("Citric Acid", 0.0, 1.0, 0.0)
    residual_sugar = st.slider("Residual Sugar", 0.0, 15.0, 2.0)
    chlorides = st.slider("Chlorides", 0.0, 1.0, 0.076)
    free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 0.0, 100.0, 11.0)
    total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 0.0, 300.0, 34.0)
    density = st.slider("Density", 0.9900, 1.0050, 0.9978)
    pH = st.slider("pH", 2.0, 5.0, 3.51)
    sulphates = st.slider("Sulphates", 0.0, 2.0, 0.56)
    alcohol = st.slider("Alcohol", 8.0, 15.0, 9.4)

    if st.button("Predict"):
        features = [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                    chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                    density, pH, sulphates, alcohol]]
        prediction = model.predict(features)[0]
        st.success("Good Quality 🍷" if prediction == 1 else "Bad Quality 🍷")
