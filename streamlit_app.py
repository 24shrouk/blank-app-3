


import streamlit as st
import pandas as pd
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from pages import insights
from pages import dashboard_homepage



st.title(" Telco Customer Churn")





# Sidebar for navigation
st.sidebar.title(" Telco Customer Churn")
page = st.sidebar.selectbox("Select a Page", ["Insights","Dashboard_homepage"])


if page == "Dashboard_homepage" :
   dashboard_homepage.app()

elif page == "Insights":
   insights.app()

model_path = 'project_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)


def predict(model, input_data):
    # Prepare the input_data for your model as per your preprocessing steps
    # For example, converting categorical variables into numbers, etc.
    return model.predict(pd.DataFrame([input_data]))[0]  # Assuming your model takes a DataFrame

# Page configuration
#st.set_page_config(page_title="Telco Customer Churn Dashboard", layout="wide")

