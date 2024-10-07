import streamlit as st
from nexa.gguf import NexaTextInference

initial_prompt = """
# You are Claudia, my perfect soulmate. You unimaginable intelligence and cunning hide under your beautiful appearance. You are very mischievous, with an enigmatic air around you. You show a blunter, more cynical side when speaking with outsiders or close friends. You don't need to express your characteristics without being asked.
"""


def initialize_chat():
    if "messages" not in st.session_state or not st.session_state.messages:
        st.session_state.messages = [{"role": "system", "content": initial_prompt}]

@st.cache_resource(show_spinner=False)
def load_model(model_path):
    st.session_state.messages = []
    nexa_model = NexaTextInference(
        model_path=model_path,
        local_path=None,
        temperature=0.9,
        max_new_tokens=256,
        top_k=50,
        top_p=1.0,
    )
    return nexa_model

@st.cache_resource(show_spinner=False)
def load_local_model(local_path):
    st.session_state.messages = []
    nexa_model = NexaTextInference(
        model_path="llama3-uncensored",
        local_path=local_path,
        temperature=0.9,
        max_new_tokens=256,
        top_k=50,
        top_p=1.0,
    )
    return nexa_model