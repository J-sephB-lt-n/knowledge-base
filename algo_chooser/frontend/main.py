
import streamlit as st

st.title("Algorithm Evaluator")

base_url = st.text_input("Base URL", value="http://localhost:11434")
api_key = st.text_input("API Key", type="password")
model = st.text_input("Specify your model name")
business_problem = st.text_area("Describe your business problem")

if st.button("Evaluate"):
    if not all([base_url, model, api_key, business_problem]):
        st.warning("Please fill all fields.")
    else:
        st.text("working")
