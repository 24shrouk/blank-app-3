


import streamlit as st
#from model import load_model, predict  # Import your model functions
import pandas as pd
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from pages import insights



st.title(" Telco Customer Churn")

# Load your model



# Sidebar for navigation
st.sidebar.title(" Telco Customer Churn")
page = st.sidebar.selectbox("Select a Page", ["Insights"])

# Load the page based on selection
#if page == "Page 1":
  #  page1.app()
#elif page == "Page 2":
 #   page2.app()
#elif page == "Page 3":
 #   page3.app()
if page == "Insights":
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

# Sidebar for navigation
''''st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ("Home", "Data Overview", "Prediction", "Visualizations"))

if page == "Home":
    st.title("Welcome to the Telco Customer Churn Dashboard")
    st.image("images/telecom.jpeg")  # Add your welcome image here
    st.write("Explore customer churn data and predictions.")
    
elif page == "Data Overview":
    st.title("Data Overview")
    data = pd.read_csv("projectdata.csv")  # Load your dataset
    st.write(data.head())
    st.write("Number of records:", data.shape[0])

elif page == "Prediction":
    st.title("Churn Prediction")
    
    # User inputs for prediction
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    # Add more input fields as per your model's requirements...

    if st.button("Predict"):
        # Prepare input for the model
        input_data = {
            "gender": gender,
            "senior_citizen": senior_citizen,
            "partner": partner,
            # Include other inputs...
        }
        prediction = predict(model, input_data)  # Call your prediction function
        st.write("Predicted Churn:", "Yes" if prediction else "No")

elif page == "Visualizations":
    st.title("Data Visualizations")
    # Create your visualizations using seaborn/matplotlib

    
    # Example: distribution of churn
    churn_counts = data['Churn'].value_counts()
    sns.barplot(x=churn_counts.index, y=churn_counts.values)
    plt.title("Churn Distribution")
    st.pyplot(plt)'''







