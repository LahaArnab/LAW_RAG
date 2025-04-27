
#setup to upload pdf 


import streamlit as st

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"]
                                 , accept_multiple_files=False)


user_query = st.text_input("Enter your query:" )
ask_question = st.button("Ask Question")

if ask_question:
    st.chat_massage("user", user_query)

    #rag pipeline

    fixed_response = "This is a fixed response"
    st.chat_massage("assistant", fixed_response)

else:
    st.error("Please upload a PDF and enter a query.")

st.chat_massage("assistant", "Hello! How can I help you today?")