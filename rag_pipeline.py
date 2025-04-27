
from dotenv import load_dotenv
load_dotenv()  # Ensure this is uncommented


from langchain_groq import ChatGroq
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate


# Setup LLM  with Groq
llm_model=ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# Retrieve Docs

def retrieve_docs(query):
    return faiss_db.similarity_search(query)



def get_context(documents):  #to get the particular context 
    context = "\n\n".join([doc.page_content for doc in documents])  # only keep relavent context
    return context

#Step3: Answer Question

custom_prompt_template = """
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context
Question: {question} 
Context: {context} 
Answer:
"""

def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    return chain.invoke({"question": query, "context": context})




###   Ask Quesrion 
question="If a government forbids the right to assemble peacefully which articles are violated and why?"
retrieved_docs=retrieve_docs(question)
print("AI Lawyer: ",answer_query(documents=retrieved_docs, model=llm_model, query=question))