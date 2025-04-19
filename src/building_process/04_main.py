from typing import Iterator
from config import settings
import time
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables import Runnable
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)

messages = [
    ("system", "You are a translation assistant!"),
    ("user", "Translate the following word: {word} to {language}."),
]

#String Template - Option 1
# prompt_template = PromptTemplate.from_template("""
# Could you please translate to: {language}
# the following word: {word}?""")

# Structured Template - Option 2
template = ChatPromptTemplate.from_messages(messages)
prompt = template.invoke(input={
    "language": "Spanish",
    "word": "Desktop"
})

llm_response = llm.invoke(prompt)
print(llm_response.content)