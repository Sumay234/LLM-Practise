from langchain_openai import ChatOpenAI
from decouple import config
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate, HumanMessagePromptTemplate, PromptTemplate


SECRET_KEY = config('OPEN_API_KEY')
chat = ChatOpenAI(openai_api_key = SECRET_KEY)

# Chat Model - Prompt Template

# Example 1 - Message Prompt Template as Tuple
chatPrompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful assistant that translates {input_language} to {output_language}."),
     ("human", "{text}")
])
#print("Chat Prompt: ", chatPrompt)
#print("Chat Prompt Input Variable : ", chatPrompt.input_variables)

formatted_ChatPrompt = chatPrompt.format_messages(
    input_language = "English",
    output_language = "French",
    text = "My name is Sumay and currently doing nothing"
)

respone = chat.invoke(formatted_ChatPrompt)
print(respone)

#print(respone.content)
