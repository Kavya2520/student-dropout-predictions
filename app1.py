import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎓 Student Dropout Analysis Dashboard")

# Load dataset
df = pd.read_csv("data/student-mat.csv", sep=';')

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Dataset Shape")
st.write(df.shape)

# Chart 1
st.subheader("Study Time Distribution")
fig, ax = plt.subplots()
df['studytime'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

# Chart 2
st.subheader("Absences Distribution")
fig, ax = plt.subplots()
df['absences'].plot(kind='hist', bins=20, ax=ax)
st.pyplot(fig)

# Simple prediction section
st.subheader("Predict Student Performance")

studytime = st.slider("Study Time (1-4)", 1, 4)
absences = st.slider("Absences", 0, 50)

if st.button("Predict"):
    if studytime >= 3 and absences < 10:
        st.success("Student likely to perform well")
    else:
        st.error("Student may be at risk of poor performance")