import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved scaler and model
with open("graduate_adm_scalar.pkl", "rb") as f:
    saved_scalar = pickle.load(f)
with open("graduate_adm_model.pkl", 'rb') as f:
    saved_model = pickle.load(f)

st.title('Graduate Admission Predictor')
st.write("""
    This application predicts the chance of a student's admission to graduate school based on various parameters.
    Fill in the details below and click 'Predict' to see the results.
""")

st.sidebar.header('User Input Parameters')
st.sidebar.write("""
    Please input the following parameters:
""")

# Create input fields without predefined values
gre = st.sidebar.number_input('GRE Score (0 to 340)', min_value=0, max_value=340, step=1, value=0)
toefl = st.sidebar.number_input('TOEFL Score (0 to 120)', min_value=0, max_value=120, step=1, value=0)
university_rating = st.sidebar.selectbox('University Rating (1 to 5)', [1, 2, 3, 4, 5], index=0)
sop = st.sidebar.number_input('Statement of Purpose (1.0 to 5.0)', min_value=1.0, max_value=5.0, step=0.1, value=1.0)
lor = st.sidebar.number_input('Letter of Recommendation Strength (1.0 to 5.0)', min_value=1.0, max_value=5.0, step=0.1, value=1.0)
cgpa = st.sidebar.number_input('CGPA (1.00 to 10.00)', min_value=1.00, max_value=10.00, step=0.01, value=1.00)
research = st.sidebar.selectbox('Research Experience', ['No', 'Yes'])

# Convert 'Yes'/'No' to 1/0
research = 1 if research == 'Yes' else 0

# Create a button for prediction
if st.sidebar.button('Predict'):
    data = {
        'GRE Score': gre,
        'TOEFL Score': toefl,
        'University Rating': university_rating,
        'SOP': sop,
        'LOR ': lor,
        'CGPA': cgpa,
        'Research': research
    }

    user_input = pd.DataFrame(data, index=[0])
    scaled_input = saved_scalar.transform(user_input)
    prediction = saved_model.predict(scaled_input)

    # Display the prediction
    st.subheader('Prediction')
    st.write(f'Your predicted admission chance is: **{np.round(prediction[0] * 100, 2)}%**')
