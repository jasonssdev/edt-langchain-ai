from src.config import settings
from src.paths import PRODUCTS_PDF_PATH
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter, TokenTextSplitter

api_key = settings['openai']
model = 'gpt-4o-mini'
llm = ChatOpenAI(api_key=api_key, model=model)

loader = PyPDFLoader(str(PRODUCTS_PDF_PATH))
content = loader.lazy_load()
text = ""

for page in content:
    text += page.page_content + "\n"

# # Using CharacterTextSplitter
# text_splitter = CharacterTextSplitter(
#     separator="\n",
#     chunk_size=1000,
#     chunk_overlap=200,
#     )

# # Using RecursiveCharacterTextSplitter
# text_splitter = RecursiveCharacterTextSplitter(
#     separators=['\n\n', '\n', '.', ' ', ''],
#     chunk_size=1000,
#     chunk_overlap=200,
#     )

# Using TokenTextSplitter
text_splitter = TokenTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
    model_name=model
    )

texts = text_splitter.split_text(text)

print(type(texts))
print(len(texts))
print(texts[0])
