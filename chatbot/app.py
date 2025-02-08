from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

from decouple import config
SECRET_KEY = config('OPEN_API_KEY')
chat = ChatOpenAI(openai_api_key = SECRET_KEY)

#os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")

## this is for Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant. Please response to the queries")
        ("user", "Question:{question}")

    ]
)

## Streamlit framework
st.title("Langchain Demo with OPEN AI")
input_text = st.text_input("Search the topic you want")

## OpenAI llm
llm = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
