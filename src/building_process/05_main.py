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

# Comma Parser
# llm_response = llm.invoke("""
#     Return a list of 3 electgronic music genres,
#     output format should be a comma separated list of genres.
#     Do not return any other text.
#     Example: House, Techno, Bigroom
# """)
# parser  = CommaSeparatedListOutputParser()
# parser_result = parser.invoke(llm_response.content)
# print(parser_result)

class AnswerWithJustification(BaseModel):
    """Answer with justification for the answer."""
    answer: str
    justification: str

llm_structured = llm.with_structured_output(AnswerWithJustification)
prompt = "How old I am if I was born in 1990/01/01?"
response = llm_structured.invoke(input=prompt)

print(response)
print(response.__class__)
print(response.answer)
print(response.justification)