import streamlit as st

st.title("First Streamlit app")

name = st.text_input("What is your name?")

age = st.slider("How old are you?", 1, 100, 25)

if name:
    st.write(f"Nice to meet you {name}")



import pandas as pd
data = {
    "Days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Cups of Coffee": [1, 2, 4, 3, 5]
}
coffee_table = pd.DataFrame(data)
st.write("Here is the data:")
st.dataframe(coffee_table)

st.write("Here is a chart of the data:")
st.bar_chart(coffee_table, x="Days", y="Cups of Coffee", color = "#CF17D2")

size = st.radio("Pick a size:", ["Small", "Medium", "Large"])
 
country = st.selectbox("Where are you from?", ["India", "Malaysia", "USA", "UK"])
 
skills = st.multiselect("Select your skills:", ["Python", "SQL", "Power BI", "AI"])

agree = st.checkbox("I agree to the terms and conditions")

dark_mode = st.checkbox("Enable dark mode")

show_password = st.toggle("Show password")
if show_password:
    st.write("Password")
else:
    st.write("Password hidden")

st.button("Click me!")

if st.button("Test System"):
    st.success("System is working fine!")

if st.button("Hurray"):
    st.balloons()