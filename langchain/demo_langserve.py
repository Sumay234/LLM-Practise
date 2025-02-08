'''
LangServer help to deploy the LLM
'''
import os
import uvicorn

from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langserve import add_routes

from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 1. Create prompt template:
system_template = "Translate the following into {language} "


prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
model = ChatOpenAI(model="gpt-4o-mini" ,openai_api_key = OPENAI_API_KEY)


# 3. Create Parser
parser = StrOutputParser()

# 4. Create Chain 
chain = prompt_template | model | parser


app = FastAPI(
    title= "My LLM API",
    description= "My first LLM API",
    version= "1.0"
)


add_routes(
    app,
    chain,
    path = "/chain"
)

if __name__ == "__main__":
    uvicorn.run(app, host= "localhost", port=8000)