from decouple import config
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


SECRET_KEY = config('OPEN_API_KEY')

'''
llm = OpenAI(openai_api_key = SECRET_KEY)

respone = llm.invoke("Who is elon musk")
print(respone)

'''


# --> Chat Model

'''
model = ChatOpenAI(model="gpt-4o-mini",openai_api_key = SECRET_KEY)
respone = model.invoke("Tell me about the PM of India in 50 words")
print(respone)

'''
message = [
    SystemMessage(content="You are environmentalist"),
    HumanMessage(content="Tell me some deforestation issue in less than 60 words")
]


model = ChatOpenAI(model="gpt-4o-mini",openai_api_key = SECRET_KEY)
respone = model.invoke(message)
print(respone)


