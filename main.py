import streamlit as st
import pandas as pd

st.title("Stability Window RT for Client")
st.text('This is a test to show a RT stability Window')
st.markdown('## test in markdown')
uploaded_file = st.file_uploader('Ubload a file:')

if uploaded_file:
    st.header('Raw Data')
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.header('Data stadistics')
    st.write(df.describe())