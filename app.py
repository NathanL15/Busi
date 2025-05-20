import streamlit as st
from busi import generate_business_insight

st.title("🧠 Busi: Business Idea Analyzer")

user_input = st.text_area("Describe your business idea:")
if st.button("Analyze"):
    with st.spinner("Generating insights..."):
        output = generate_business_insight(user_input)
        st.markdown(output)
        st.success("Insights generated!")