
#setup to upload pdf 
from rag_pipeline import answer_query, retrieve_docs, llm_model


import streamlit as st

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"]
                                 , accept_multiple_files=False)


user_query = st.text_input("Enter your query:" )
ask_question = st.button("Ask Question")




if ask_question:
    st.chat_message("user").text(user_query)

    # RAG pipeline
    retrieved_docs = retrieve_docs(user_query)
    response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)

    st.chat_message("assistant").text(response)
else:
    st.error("Please upload a PDF and enter a query.")

st.chat_message("assistant").text("Hello! How can I help you today?")

