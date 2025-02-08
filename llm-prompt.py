from langchain_openai import OpenAI
from decouple import config

SECRET_KEY = config('OPEN_API_KEY')
llm = OpenAI(openai_api_key = SECRET_KEY)

# LLM - Prompt Template
from langchain.prompts import PromptTemplate

'''
# Example 1 --> Prompt having No Input Variable
#no_Input_Prompt = PromptTemplate(input_variables=[], template="Tell me a Python Trick")
#print(no_Input_Prompt)

no_Input_Prompt = PromptTemplate.from_template(template="Tell me a Python Trick")
formatted_No_InputPrompt = no_Input_Prompt.format()
#print(formatted_No_InputPrompt)
respone = llm.invoke(formatted_No_InputPrompt)
print(respone)
'''


# Example 2 --> Prompt having One Input Variable
'''
one_Input_Prompt = PromptTemplate(input_variables=["language"],template="Tell me a {language} Trick")
# one_Input_Prompt = PromptTemplate.from_template("Tell me a {language} Trick")
# print(one_Input_Prompt)

formatted_One_InputPrompt = one_Input_Prompt.format(language = " Java")
respone = llm.invoke(formatted_One_InputPrompt)
print(respone)
'''

# Example 3 --> Prompt having Multiple Input Variable

multiple_Input_Prompt = PromptTemplate(input_variables=["language", "topic"],template="Tell me a {language} {topic} Trick")
# one_Input_Prompt = PromptTemplate.from_template("Tell me a {language} {topic} Trick")
# print(one_Input_Prompt)

formatted_Multiple_InputPrompt = multiple_Input_Prompt.format(language = "c++", topic = "function")
print (formatted_Multiple_InputPrompt)
respone = llm.invoke(formatted_Multiple_InputPrompt)
print(respone)

