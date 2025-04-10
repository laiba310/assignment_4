import streamlit as st


def calculate_bmi(weight, height):
 
    bmi = weight / (height ** 2)
    
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    
    return bmi, category

# Streamlit interface
st.title("BMI Calculator")

# User input for weight and height
weight = st.number_input("Enter your weight in kg:", min_value=1.0, step=0.1)
height = st.number_input("Enter your height in meters:", min_value=0.5, step=0.01)

# Calculate BMI when user clicks the button
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi, category = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")
        st.write(f"Category: {category}")
    else:
        st.write("Please enter valid values for both weight and height.")
