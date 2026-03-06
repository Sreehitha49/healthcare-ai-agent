import streamlit as st

st.title("AI Healthcare Assistant")

st.write("Enter your symptoms to get basic health advice")

symptoms = st.text_input("Enter your symptoms")

if st.button("Get Advice"):
    if symptoms:
        st.write("You entered:", symptoms)
        st.write("Suggestion: Please consult a doctor if symptoms persist.")
    else:
        st.write("Please enter symptoms")
