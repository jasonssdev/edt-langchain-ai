# from typing import Literal
from src.config import settings
# from pydantic import BaseModel
from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langgraph.graph import StateGraph, START, END 

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)
# from langchain_community.document_loaders import PyPDFLoader

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)

print("working")

# loader = PyPDFLoader("./../data/raw/file.pdf")
# content = loader.load()
# print(content[0].page_content)
