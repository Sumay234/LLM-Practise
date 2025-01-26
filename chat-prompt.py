from langchain_openai import ChatOpenAI
from decouple import config
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate, HumanMessagePromptTemplate, PromptTemplate


SECRET_KEY = config('OPEN_API_KEY')
chat = ChatOpenAI(openai_api_key = SECRET_KEY)

# Chat Model - Prompt Template
'''
# Example 1 -->  Message Prompt Template as Tuple
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
'''
'''
# Example 2 - Using Message Classes
sys_template  = "You are a helpful assistant that traanslate {input_language} to {output_language}. "
human_template = "{text}"

chat_Prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(sys_template),
    HumanMessagePromptTemplate.from_template(human_template)
])

formatted_ChatPrompt = chat_Prompt.format_messages(
    input_language = "English",
    output_language = "Hindi",
    text = "My name is Sumay and currently doing nothing"
)

respone = chat.invoke(formatted_ChatPrompt)
print(respone)
'''



## Example 3 --> Using Prompt Template


# systemPrompt = PromptTemplate(
#     input_variable = ["input_language", "output_language"],
#     template= "You are a helpful assistance that translate {input_language} , {output_language} . "
# )

systemPrompt = PromptTemplate.from_template(
    "You are a helpful assistance that translate {input_language} , {output_language} . "
)
humanPrompt = PromptTemplate.from_template(
    "{text}"
)

systemMessagePrompt = SystemMessagePromptTemplate(
    prompt=systemPrompt
)
humanMessagePrompt = SystemMessagePromptTemplate(
    prompt = humanPrompt
)

chatPrompt = ChatPromptTemplate.from_messages([
    systemMessagePrompt,humanMessagePrompt
])

formatted_ChatPrompt = chatPrompt.format_messages(
    input_language = "English",
    output_language = "English",
    text = "Tell me about elonk musk in 50 words"
)

response = chat.invoke(formatted_ChatPrompt)
print(response)
