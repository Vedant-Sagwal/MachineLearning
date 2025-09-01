from warnings import catch_warnings
import pandas as pd
import streamlit as st

st.title("Streamlit text Input!")

name = st.text_input("Enter Your Name : ")

age = st.slider("Enter Your age", 1,100, 25)

options = ["Python", "Java", "C++", "Go", "Rust"]
choices = st.selectbox("Choose Your Favourite Lang : ", options)
st.write("You Chose : ", choices)

if name:
    st.write("Your Name is : ", name)
    st.write("Your Age is : ", age)

uploaded_file = st.file_uploader("Choose a CSV file", type = "csv")
if uploaded_file is not None : 
    df = pd.read_csv(uploaded_file)
    st.write(df)