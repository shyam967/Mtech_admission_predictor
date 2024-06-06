import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

# Hide the Streamlit menu and footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load the saved scaler and model
with open("graduate_adm_scalar.pkl", "rb") as f:
    saved_scalar = pickle.load(f)
with open("graduate_adm_model.pkl", 'rb') as f:
    saved_model = pickle.load(f)

# Custom CSS to align buttons horizontally
st.markdown("""
    <style>
    .horizontal-buttons > button {
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Top Navigation Menu
st.markdown("<h1 style='text-align: center;'>Graduate Admission Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>This application predicts the chance of a student's admission to graduate school based on various parameters. Fill in the details below and click 'Predict' to see the results.</p>", unsafe_allow_html=True)

# Create a container for the navigation buttons
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        home = st.button("Home")
    with col2:
        project_details = st.button("Project Details")
    with col3:
        input_explanation = st.button("Input Explanation")
    with col4:
        about = st.button("About")

# Determine which button was clicked
if home:
    menu = "Home"
elif project_details:
    menu = "Project Details"
elif input_explanation:
    menu = "Input Explanation"
elif about:
    menu = "About"
else:
    menu = "Home"

# Home Page
if menu == "Home":
    #st.markdown("<p style='text-align: center;'>This application predicts the chance of a student's admission to graduate school based on various parameters. Fill in the details below and click 'Predict' to see the results.</p>", unsafe_allow_html=True)
    
    st.header('User Input Parameters')
    st.write("""
        Please input the following parameters:
    """)

    # Create input fields without predefined values
    gre = st.number_input('GRE Score (0 to 340)', min_value=0, max_value=340, step=1, value=0)
    toefl = st.number_input('TOEFL Score (0 to 120)', min_value=0, max_value=120, step=1, value=0)
    university_rating = st.selectbox('University Rating (1 to 5)', [1, 2, 3, 4, 5], index=0)
    sop = st.number_input('Statement of Purpose (1.0 to 5.0)', min_value=1.0, max_value=5.0, step=0.1, value=1.0)
    lor = st.number_input('Letter of Recommendation Strength (1.0 to 5.0)', min_value=1.0, max_value=5.0, step=0.1, value=1.0)
    cgpa = st.number_input('CGPA (1.00 to 10.00)', min_value=1.00, max_value=10.00, step=0.01, value=1.00)
    research = st.selectbox('Research Experience', ['No', 'Yes'])

    # Convert 'Yes'/'No' to 1/0
    research = 1 if research == 'Yes' else 0

    # Create a button for prediction
    if st.button('Predict'):
        # Placeholder for the loading message
        loading_message = st.empty()
        loading_message.info('Analyzing data and predicting...')

        # Simulate a delay for processing
        time.sleep(3)

        # Remove the loading message
        loading_message.empty()

        # Prepare the input data
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
        st.markdown(f"<div style='text-align: center;'>Your predicted admission chance is: **{np.round(prediction[0] * 100, 2)}%**</div>", unsafe_allow_html=True)

# Project Details Page
elif menu == "Project Details":
    st.header("Project Details")
    st.write("""
        This project aims to predict the chances of a student being admitted to a graduate program based on various input parameters such as GRE score, TOEFL score, university rating, statement of purpose, letter of recommendation strength, CGPA, and research experience. The prediction model is built using machine learning techniques.
    """)

# Input Explanation Page
elif menu == "Input Explanation":
    st.header("Input Explanation")
    st.write("""
        Here are the details of the inputs required for the prediction:
        
        - **GRE Score**: Graduate Record Examinations score (0 to 340).
        - **TOEFL Score**: Test of English as a Foreign Language score (0 to 120).
        - **University Rating**: Rating of the university (1 to 5).
        - **Statement of Purpose (SOP)**: Strength of the statement of purpose (1.0 to 5.0).
        - **Letter of Recommendation (LOR)**: Strength of the letter of recommendation (1.0 to 5.0).
        - **CGPA**: Cumulative Grade Point Average (1.00 to 10.00).
        - **Research**: Research experience (Yes or No).
    """)

# About Page
elif menu == "About":
    st.header("About")
    st.write("""
        This application was developed to assist students in predicting their chances of being admitted to a graduate program. The model was trained on historical data and provides an estimated probability based on the input parameters.
    """)

    # Developer Details
    st.header("Developers")
    st.write("""
        **Developer 1**:
        - Name: Developer One
        - Role: Data Scientist
        - LinkedIn: [Developer One](https://www.linkedin.com/in/developerone)
        - GitHub: [developerone](https://github.com/developerone)

        **Developer 2**:
        - Name: Developer Two
        - Role: Machine Learning Engineer
        - LinkedIn: [Developer Two](https://www.linkedin.com/in/developertwo)
        - GitHub: [developertwo](https://github.com/developertwo)
    """)
