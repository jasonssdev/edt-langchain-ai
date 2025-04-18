from src.config import settings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)

class AgentState(BaseModel):
    user_message: str = ''
    agent_reponse: str = ''
    greeting: bool = False

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

graph = StateGraph(AgentState)
graph.add_node(greeting_node)
graph.add_node(response_node)

graph.add_edge(START, "greeting_node")
graph.add_edge("greeting_node", "response_node")
graph.add_edge("response_node", END)

compiled_graph = graph.compile()

initial_state = AgentState(user_message='Hello')
response = compiled_graph.invoke(initial_state)

print(response["agent_reponse"])
