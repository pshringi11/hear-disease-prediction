❤️ Heart Disease Prediction Web App
A Machine Learning-powered web application that predicts the likelihood of heart disease in patients based on clinical parameters. This project demonstrates a production-ready approach to machine learning by utilizing modular pipelines and an interactive Streamlit interface.

🚀 [Live Demo Link](https://hear-disease-prediction-8nvusbumgbqthq2hw7re75.streamlit.app/)

📌 Project Overview
Heart disease is a leading cause of mortality globally. This project leverages predictive analytics to provide an early warning system. By processing clinical data such as Blood Pressure, Cholesterol, and Thallium test results, the model provides an immediate assessment of heart disease risk, showcasing how data-driven tools can enhance clinical decision-making.

🛠️ Technical Methodology
The core of this application is a Random Forest Classifier. This model was selected for several key reasons:

Handling Non-Linearity: Clinical health data often involves complex, non-linear relationships between features (e.g., the combined effect of age and cholesterol) which Random Forests capture effectively via ensemble decision trees.

Feature Importance: It allows for the identification of which clinical markers (like Thallium or Chest Pain type) are the strongest predictors of heart disease.

Robustness: Random Forests are less prone to overfitting compared to individual decision trees, ensuring better generalization on unseen patient data.

⚙️ Data Preprocessing & Pipeline
This project implements advanced Scikit-Learn workflows to ensure data integrity and prevent data leakage:

ColumnTransformer: Used to apply targeted transformations to different data types—specifically One-Hot Encoding for categorical variables (like Gender and Chest Pain type) and Standard Scaling for numerical features (like Age and Max Heart Rate).

Scikit-Learn Pipeline: All preprocessing steps and the model are encapsulated into a single Pipeline object. This ensures that the exact same transformations applied during training are executed during real-time inference in the Streamlit app, maintaining a "clean" and reproducible codebase.

📂 Project Structure

├── app.py                     # Main Streamlit application & UI logic
├── heart_model_pipeline.pkl    # Serialized Scikit-Learn Pipeline (Preprocessing + Model)
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

🚀 Installation & Setup
1. Clone the repository:
  git clone https://github.com/pshringi11/heart-disease-prediction.git
  cd heart-disease-prediction

2. Install dependencies:
   pip install -r requirements.txt
   
3. Run the app:
   streamlit run app.py

📊 Model Performance
Accuracy: ~88%

Key Predictors: Thallium, Chest Pain Type, and Max Heart Rate were identified as the most significant clinical features.

Disclaimer: This application is for educational and demonstrative purposes only. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment.
