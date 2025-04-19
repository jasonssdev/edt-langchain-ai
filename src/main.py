from src.config import settings
from src.paths import PRODUCTS_PDF_PATH
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter
from src.chromadb_manager import ChromaDBManager
from uuid import uuid4
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate



api_key = settings['openai']
model = 'gpt-4o-mini'
llm = ChatOpenAI(api_key=api_key, model=model)

loader = PyPDFLoader(str(PRODUCTS_PDF_PATH))
content = loader.lazy_load()
text = ""

for page in content:
    text += page.page_content + "\n"

# Using TokenTextSplitter
text_splitter = TokenTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
    model_name=model
    )

texts = text_splitter.split_text(text)

chromadb_manager = ChromaDBManager()

uuids = [str(uuid4()) for _ in range(len(texts))]
metadatas = [{'filename': str(PRODUCTS_PDF_PATH)} for _ in range(len(texts))]

query = "cual es el precio de la silla ergonomica hernan miller"

result = chromadb_manager.query(
    query=query,
    metadata={'filename': str(PRODUCTS_PDF_PATH)},
    k=2
)

context = "\n".join([row.page_content for row in result])

prompt_template = PromptTemplate.from_template("""
    You an agent who is able to answer questions about a product catalog.
    You will be given a context and an user query.
    Context: {context}
    Query: {query}
""")

chain = prompt_template | llm
chain_result = chain.invoke({
    'context': context,
    'query': query
})
print(chain_result.content)