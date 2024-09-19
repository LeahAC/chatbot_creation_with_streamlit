import streamlit as st
from streamlit_chat import message
from database import get_user_details
from llm import run_llm

name = st.session_state.get("name", "")   

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True
   
st.button('Start chatting!', on_click=click_button)

if st.session_state.clicked:
        
    if ("messages" not in st.session_state
        and "chat_history" not in st.session_state
        ):

        st.session_state.messages = []
        st.session_state["chat_history"] = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"]) 

    user_details = get_user_details(name)

    if prompt := st.chat_input("Tell me your thoughts."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state["chat_history"].append(("human", prompt))    

    with st.chat_message("assistant"):
        stream = run_llm(query="", name = name, data = user_details , conversation_history = st.session_state["chat_history"])
        response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})        
        st.session_state["chat_history"].append(("ai", response))
    
          