from config import settings
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables import Runnable
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from pydantic import BaseModel

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)