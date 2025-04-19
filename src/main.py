from src.config import settings
from src.paths import RAW_PDF_PATH
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)
# from langchain_community.document_loaders import PyPDFLoader

api_key = settings['openai']
model = 'o4-mini-2025-04-16'
llm = ChatOpenAI(api_key=api_key, model=model)

print("working")

loader = PyPDFLoader(str(RAW_PDF_PATH))
content = loader.load()
print(content[0].page_content)
