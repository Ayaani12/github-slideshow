import openai
import streamlit as st
from streamlit_chat import message
openai.api_key=st.secrets["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"]
def generate_response(prompt):
    completions=openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens = 1024,
        n =1 ,
        stope = None,
        temparature = 0.5,

    )
    message = completions.choices[0].text
    return message
st.title("Ayaan12: Streamlit + openai")