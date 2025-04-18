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

class Answer(BaseModel):
    number_of_words: int

# Template
prompt_template = PromptTemplate.from_template("""
    I will give a text and you will return the number of words in it.
    Text: {text}
""")
#prompt
prompt = prompt_template.invoke({
    'text': 'This is an example with langchain'
})
# structured output
llm_structured = llm.with_structured_output(Answer)

# print
# llm_result = llm_structured.invoke(prompt)
# print(llm_result)

# all of that could be resolved with chain

chain = prompt_template | llm_structured
chain_result = chain.invoke({
    'text': 'This is an example with langchain'
})
print(chain_result)