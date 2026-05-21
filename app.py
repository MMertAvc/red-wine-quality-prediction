
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')

st.title("Wine Quality Prediction")
st.write("Enter the chemical properties of wine to predict its quality score (0–10).")

features = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
    'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'
]

user_input = []
for feature in features:
    val = st.number_input(f"{feature}", value=0.0, format="%.3f")
    user_input.append(val)

if st.button("Predict"):
    input_array = np.array(user_input).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    st.subheader(f"Predicted Wine Quality: {round(prediction, 2)} / 10")
