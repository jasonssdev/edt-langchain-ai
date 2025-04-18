from langchain_openai import ChatOpenAI
from config import settings

llm = ChatOpenAI(api_key=settings['openai'], model='gpt-4o-mini')

llm_response = llm.invoke('What is the capital of Panama?')
print(llm_response.content)