# Importing necessary libraries
from pyexpat import model  # Assuming this is a typo and should be removed
import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

# Loading the pre-trained model from a saved file
pickle_in = open("trained_model.sav", "rb")
model = pickle.load(pickle_in)

# Function to display a welcome message
def welcome():
    return "Welcome All"

# Function to predict fraud based on transaction details
def predict_Fraud(Type, Amount, oldbalanceOrg, newbalanceOrig):
    # Using the loaded model to make predictions
    prediction = model.predict([[Type, Amount, oldbalanceOrg, newbalanceOrig]])
    print(prediction)  # Print the prediction for debugging purposes
    return prediction

# Main function for the Streamlit web application
def main():
    # HTML template for the web app interface
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Fraud Prediction System </h2>
    </div>
    """
    # Displaying the HTML template using Streamlit
    st.markdown(html_temp, unsafe_allow_html=True)

    # Taking user input for transaction details
    variance = st.text_input("Payment Type (1.CASH_OUT 2.PAYMENT 3.CASH_IN 4.TRANSFER 5.DEBIT)", "Type Here")
    skewness = st.text_input("Payment Amount", "Type Here")
    curtosis = st.text_input("Initial Balance of Sender", "Type Here")
    entropy = st.text_input("Final Balance of the Sender", "Type Here")

    result = ""
    # Checking if the prediction button is pressed
    if st.button("Predict"):
        # Calling the predict_Fraud function to make predictions
        result = predict_Fraud(variance, skewness, curtosis, entropy)
    st.success('The Transaction is {}'.format(result))

    # Displaying additional information when the "About" button is pressed
    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

# Checking if the script is run directly
if __name__ == '__main__':
    main()
