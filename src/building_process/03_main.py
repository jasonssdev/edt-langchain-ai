from typing import Iterator
from config import settings
import time
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables import Runnable

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

# Customer Runnable
class TextInverter(Runnable):
    def invoke(self, input_text: str) -> str:
        return input_text[::-1]
    
    def stream(self, input_text: str) -> Iterator[str]:
        inverted_text =  input_text[::-1]
        words = inverted_text.split()
        for word in words:
            yield word
    
test_runnable = TextInverter()
for chunk in  test_runnable.invoke("Hello, how are you today?"):
    time.sleep(0.1)
    print(chunk, end=' ', flush=True)

