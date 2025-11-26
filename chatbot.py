from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

#load environment variables from .env file
load_dotenv()

#streamlit page configuration
st.set_page_config(
    page_title="Gerative AI  Chatbot ", 
    page_icon="🤖",
    layout="centered",
)
st.title("🤖 Gerative AI  Chatbot ")

#iitialize chat history 
#chat_history=[]
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#show chat messages from history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#llm initialization
llm=ChatGroq(
    model="moonshotai/kimi-k2-instruct-0905", 
    temperature=0.0,
    )

user_prompt=st.chat_input("Type your message here...")

if user_prompt : 
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt}
    )

    response=llm.invoke(
        input=[{"role": "system", "content": "You are a helpful assistant."},*st.session_state.chat_history]
    )
    Assistat_response=response.content
    st.session_state.chat_history.append({"role": "assistant", "content": Assistat_response})

    with st.chat_message("assistant"):
        st.markdown(Assistat_response)