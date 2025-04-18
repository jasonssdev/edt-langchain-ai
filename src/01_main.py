from config import settings
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage

api_key = settings['anthropic']
model = 'claude-3-haiku-20240307'
llm = ChatAnthropic(api_key=api_key, model=model)

messages = [
    SystemMessage(
        content="You are a helpful assistant! Your name is Bob."
    ),
    HumanMessage(
        content="What is your name?"
    )
]

llm_response = llm.invoke(messages)
print(llm_response.content)