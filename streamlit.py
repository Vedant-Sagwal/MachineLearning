import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello StreamLit")
st.write("Simple Text")

df = pd.DataFrame({
    'name' : ["Vedant", "Sagwal", "SunrakuDexHan"],
    'age' : [18, 19, 25]
})

st.write("Here is the DataFrame : ")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a','b','c']
)
st.line_chart(chart_data)