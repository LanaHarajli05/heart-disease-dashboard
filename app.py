
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Heart Disease Dashboard")

df = pd.read_csv("CVD_cleaned.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Heart Disease by Age Category")
age_counts = df[df["Heart_Disease"] == "Yes"]["Age_Category"].value_counts()
st.bar_chart(age_counts)

st.subheader("Heart Disease by Gender")
gender_counts = df[df["Heart_Disease"] == "Yes"]["Sex"].value_counts()
st.bar_chart(gender_counts)
