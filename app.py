import streamlit as st
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler,OrdinalEncoder
 

model = joblib.load('heart_model_pipeline.pkl')
st.title("Heart Disease Prediction App ❤️")
st.write("Enter the patient's information to predict heart disease.")
age = st.number_input("Age", min_value=1, max_value=120, value=30)
bp = st.number_input("Blood Pressure", min_value=50, max_value=250, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
hr = st.number_input("Max Heart Rate", min_value=50, max_value=220, value=150)
gender = st.selectbox("Gender", ["Male", "Female"])

if st.button("Predict"):
  input_dict = {
        'Age': age,
        'BP': bp,
        'Cholesterol': chol,
        'Max HR': hr,
        'Sex': 1 if gender == "Male" else 0,  
        'Chest pain type': 4,               
        'FBS over 120': 0,
        'EKG results': 2,
        'Exercise angina': 0,
        'ST depression': 1.0,
        'Slope of ST': 2,
        'Number of vessels fluro': 0,
        'Thallium': 3
    }
  input_df = pd.DataFrame([input_dict])
  prediction = model.predict(input_df)
  if prediction[0] == 'Presence': # Assuming the model predicts 'Presence' or 'Absence'
    st.error("Warning: Heart Disease ⚠️")
  else:
    st.success("You are fit and fine ✅")
