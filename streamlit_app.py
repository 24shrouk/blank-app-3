

import streamlit as st
import pandas as pd
import pickle
from pages import insights  # Make sure your insights page is correctly imported
from pages import dashboard_homepage  # Ensure this page is correctly imported

# Set page title and layout
st.set_page_config(page_title="Telco Customer Churn Dashboard", layout="wide")

# Sidebar for navigation
st.sidebar.title("Telco Customer Churn")
page = st.sidebar.selectbox("Select a Page", ["Dashboard_homepage", "Insights"])

# Navigation logic

if page == "Insights":
    insights.app()  # Ensure insights has an app() method that renders content
else:
    dashboard_homepage.app()  #

# Prediction Model Loading
model_path = 'project_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Prediction Function
def predict(model, input_data):
    return model.predict(pd.DataFrame([input_data]))[0]  # Assuming your model takes a DataFrame
