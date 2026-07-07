import streamlit as st
st.title("ML Model Predictions App")
st.write("Choose the right application from below to use it for free")

st.set_page_config(page_title="Assistant AI", layout="centered")

st.page_link("pages/page_1.py", label = "Page 1")
st.page_link("pages/page_2.py", label = "Page 2")