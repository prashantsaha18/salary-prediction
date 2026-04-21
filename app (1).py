
import streamlit as st
import pickle
import numpy as np

# Load the saved model
# Ensure 'best_model.pkl' is in the same directory as this app.py file
with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Salary Prediction App')
st.write('Enter the years of experience to predict the salary.')

# Input field for YearsExperience
years_experience = st.number_input('Years of Experience', min_value=0.0, max_value=50.0, value=5.0, step=0.1)

# Make prediction when button is clicked
if st.button('Predict Salary'):
    # Prepare the input for the model
    # The model expects a 2D array, even for a single feature
    input_data = np.array([[years_experience]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display the prediction
    st.success(f'Predicted Salary: ${prediction[0]:,.2f}')
