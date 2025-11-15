import streamlit as st

st.title("BMI Calculator")
wt = st.number_input('Enter your weight in kgs:')
h = st.number_input('Enter your heights in M:')
if h == 0:
    bmi = 0
else:
    bmi = wt/(h**2)
st.success(f'Your BMI is {bmi} KG/M^2')
