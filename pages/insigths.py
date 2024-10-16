import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset (assuming it's already cleaned and processed)
@st.cache
def load_data():
    df = pd.read_csv("projectdata.csv")
    return df

df = load_data()

def app():
    st.title("Customer Churn Insights")

    # Insight 1: Churn Distribution by Internet Service
    st.subheader("Churn Distribution by Internet Service")
    color_map = {"Yes": "#FF97FF", "No": "#AB63FA"}
    fig = px.histogram(df, x="Churn", color="InternetService", barmode="group", 
                       title="<b>Churn by Internet Service</b>", color_discrete_map=color_map)
    fig.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig)

    # Insight 2: Churn by Gender and Internet Service
    st.subheader("Churn by Gender and Internet Service")
    fig = px.histogram(df, x="gender", color="Churn", facet_col="InternetService", barmode="group",
                       title="<b>Churn by Gender and Internet Service</b>", color_discrete_map=color_map)
    fig.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig)

    # Insight 3: Monthly Charges Distribution by Churn
    st.subheader("Distribution of Monthly Charges by Churn")
    plt.figure(figsize=(8,4))
    ax = sns.kdeplot(df.MonthlyCharges[df["Churn"] == 'No'], color="Red", shade=True)
    ax = sns.kdeplot(df.MonthlyCharges[df["Churn"] == 'Yes'], color="Blue", shade=True)
    ax.set_title('Monthly Charges Distribution (Churn vs No Churn)')
    ax.set_xlabel('Monthly Charges')
    ax.set_ylabel('Density')
    st.pyplot(plt)

    # Insight 4: Tenure vs Churn
    st.subheader("Box Plot of Tenure vs Churn")
    fig = px.box(df, x='Churn', y='tenure', title="<b>Tenure vs Churn</b>")
    fig.update_layout(autosize=True, width=700, height=500)
    st.plotly_chart(fig)

    # Insight 5: Heatmap of Correlations
    st.subheader("Heatmap of Correlations")
    corr = df.apply(lambda x: pd.factorize(x)[0]).corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    plt.figure(figsize=(12,8))
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap')
    st.pyplot(plt)
