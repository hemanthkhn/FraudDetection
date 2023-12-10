# Fraud Detection Classification

This repository contains the code to test a machine learning model deployed locally for fraud detection. The project structure includes a Streamlit web app in the 'Fraud' directory and additional files for data analysis, data cleaning, and model predictions to be executed on a local machine.

## Package Requirements

Make sure you have the following packages installed:

- Python 3.6+
- numpy==1.19.5
- pandas==1.2.5
- protobuf==3.19.1
- pytest==6.2.5
- requests==2.25.1
- streamlit==0.76.0

## 1. Storing the Model Locally

- Save the trained fraud detection model as 'model.pkl'.

## 2. Hosting the Model Locally

- Use Streamlit to host the model locally.
- Update the 'app.py' file with the path to the locally saved 'model.pkl'.

## Configuration in 'app.py'

Update the 'app.py' file with the following configurations:

```python
# Local model path
MODEL_PATH = 'path/to/your/local/model.pkl'

# Streamlit app configurations
# Add any additional configurations needed for the Streamlit app
