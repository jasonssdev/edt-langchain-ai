from typing import Literal
from src.config import settings
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langgraph.graph import StateGraph, START, END

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)

class GreetingOutput(BaseModel):
    greeting: bool

class LanguageOutput(BaseModel):
    language: Literal['en', 'es']

class AgentState(BaseModel):
    user_message: str = ''
    agent_response: str = ''
    greeting: bool = False

def greeting_node(agent_state: AgentState) -> AgentState:
    prompt_template = PromptTemplate.from_template("""
    You have to check if the user mesage is a greeting or not: {user_message}
    If it is a greeting, set the greeting to True, otherwise set it to False.
    """)
    
    llm_parsed = llm.with_structured_output(GreetingOutput)
    chain = prompt_template | llm_parsed
    chain_response: GreetingOutput = chain.invoke({
        "user_message": agent_state.user_message
    })
    agent_state.greeting = chain_response.greeting
    return agent_state
    

def response_node(agent_state: AgentState) -> AgentState:
    if agent_state.greeting:
        agent_state.agent_response = "Hello, how can I help you?"
    else:
        llm_response = llm.invoke(agent_state.user_message)
        agent_state.agent_response = llm_response.content
    return agent_state

def evaluate_language_node(agent_state: AgentState) -> Literal['english_response_node', 'spanish_response_node']:
    llm_parsed = llm.with_structured_output(LanguageOutput)
    llm_response: LanguageOutput = llm_parsed.invoke(f"""
    You have to check if the user message is in English or Spanish
    return a json with the language as 'en' if the language is in english or 'es' if the language is in spanish
    user_input: {agent_state.agent_response}
    """)
    if llm_response.language == 'en':
        return "english_response_node"
    else:
        return "spanish_response_node"

def english_response_node(agent_state: AgentState) -> AgentState:
    agent_state.agent_response += "\nLanguage: English"
    return agent_state

def spanish_response_node(agent_state: AgentState) -> AgentState:
    agent_state.agent_response += "\nLanguage: Spanish"
    return agent_state


graph = StateGraph(AgentState)
graph.add_node(greeting_node)
graph.add_node(response_node)

graph.add_node(english_response_node)
graph.add_node(spanish_response_node)



graph.add_edge(START, "greeting_node")
graph.add_edge("greeting_node", "response_node")
# graph.add_edge("response_node", END)

graph.add_conditional_edges("response_node", evaluate_language_node)
graph.add_edge("english_response_node", END)
graph.add_edge("spanish_response_node", END)

compiled_graph = graph.compile()

initial_state = AgentState(user_message='Hello')
agent_response = compiled_graph.invoke(initial_state)

print(agent_response["agent_response"])
