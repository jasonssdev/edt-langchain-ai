from typing import Iterator
from config import settings
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)

messages = [
    SystemMessage(
        content="You are a helpful assistant! Your name is Bob."
    ),
    HumanMessage(
        content="What is your name and what is python?"
    )
]

for chunk in llm.stream(input=messages):
    print(chunk.content, end='', flush=True)
