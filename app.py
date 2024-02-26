import streamlit as st
from Query import get_response
st.title("SHAMSTARK'S Chatbot")

with st.form("form1"):
    query = st.text_area("Ask me anything I'm here to help you")
    submit = st.form_submit_button("Submit")
    if submit :
        response = get_response(query)
        st.info(response)
