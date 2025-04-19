from config import settings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)

class AgentState(BaseModel):
    user_message: str = ''
    agent_reponse: str = ''
    greeting: bool = False

initial_state = AgentState(user_message='Hello')
initial_state.user_message += ' world'
print(initial_state.user_message)

def greeting_node(agent_state: AgentState) -> AgentState:
    if "Hello" in agent_state.user_message:
        agent_state.greeting = True
    else:
        agent_state.greeting = False
    return agent_state

def response_node(agent_state: AgentState) -> AgentState:
    if agent_state.greeting:
        agent_state.agent_reponse = "Hello, how can I help you?"
    else:
        agent_state.agent_reponse = "Goodbye! Try again!"
    return agent_state