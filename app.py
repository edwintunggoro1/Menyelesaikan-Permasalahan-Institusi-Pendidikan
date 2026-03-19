import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model_dropout_rf.pkl", "rb"))

st.title("Student Dropout Prediction")

st.write("Input student information to predict dropout risk.")

# Input dari user
age = st.number_input("Age at Enrollment", min_value=17, max_value=70)
admission_grade = st.number_input("Admission Grade")
approved_1st = st.number_input("1st Semester Approved Units")
approved_2nd = st.number_input("2nd Semester Approved Units")

# tombol prediksi
if st.button("Predict"):

    features = np.array([[age, admission_grade, approved_1st, approved_2nd]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠ Student at Risk of Dropout")
    else:
        st.success("✅ Student Likely to Continue")