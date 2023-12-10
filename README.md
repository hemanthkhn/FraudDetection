# Fraud Detection Classification

This repository contains the code to test a machine learning model deployed locally for fraud detection. The project structure includes a Streamlit web app in the 'Fraud' directory and additional files for data analysis, data cleaning, and model predictions to be executed on a local machine.

## Package Requirements

Make sure you have the following packages installed:

- Python 3.10
- numpy==1.24.4
- pandas==2.0.3
- pyspark==3.5.0
- pytest==6.2.3
- streamlit==1.29.0

## 1. Exporting the Model

- Save the trained fraud detection model as 'trained_model.sav'.

## 2. Hosting the Model Locally

- Use Streamlit to host the model locally.
- Update the 'Fraud_ml.py' file with the path to the locally saved 'trained_model.sav'.

## Configuration in 'Fraud_ml.py'

Update the 'Fraud_ml.py' file with the following configurations:

```python
# Local model path
MODEL_PATH = 'path/to/your/local/trained_model.sav'
# To run the webapp
# Go to terminal and enter the below line
streamlit run fraud_prediction_app.py




