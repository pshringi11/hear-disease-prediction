import streamlit as st
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler,OrdinalEncoder

model = joblib.load('heart_model_pipeline.pkl')
st.sidebar.title("Model Settings ⚙️")
model_choice = st.sidebar.radio(
    "Choose Prediction Model:",
    ("Random Forest", "XGBoost"))
  @st.cache_resource
def load_selected_model(choice):
    if choice == "Random Forest":
        return joblib.load('heart_model_pipeline.pkl') 
    else:
        return joblib.load('xgb_model.pkl')
st.title("Heart Disease Prediction App ({model_choice}) ❤️")
st.sidebar.info(f"Currently using: {model_choice}")
st.write("Enter the patient's information to predict heart disease.")
age = st.number_input("Age", min_value=1, max_value=120, value=30)
bp = st.number_input("Blood Pressure", min_value=50, max_value=250, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
hr = st.number_input("Max Heart Rate", min_value=50, max_value=220, value=150)
gender = st.selectbox("Gender", ["Male", "Female"])
thal = st.selectbox("Thallium Test Result", [3, 6, 7], help="3: Normal, 6: Fixed defect, 7: Reversible defect")
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3, 4], help="0: Typical, 1: Atypical, 2: Non-anginal, 3: Asymptomatic, 4: Other")

feature_cols = ['Age', 'Sex', 'Chest pain type', 'BP', 'Cholesterol', 
                'FBS over 120', 'EKG results', 'Max HR', 'Exercise angina', 
                'ST depression', 'Slope of ST', 'Number of vessels fluro', 'Thallium']

if st.button("Predict"):
  input_data = pd.DataFrame([{
        'Age': age,
        'Sex': 1 if gender == "Male" else 0,
        'Chest pain type': cp,
        'BP': bp,
        'Cholesterol': chol,
        'FBS over 120': 0,
        'EKG results': 2,
        'Max HR': hr,
        'Exercise angina': 0,
        'ST depression': 1.0,
        'Slope of ST': 2,
        'Number of vessels fluro': 0,
        'Thallium': thal
    }])
  input_data = input_data[feature_cols]
  prediction = model.predict(input_data)
  if str(prediction[0]) == '1' or str(prediction[0]).lower() == 'presence':
        st.error(f"Prediction by {model_choice}: High Risk! ⚠️")
  else:
        st.success(f"Prediction by {model_choice}: Low Risk! ✅")
