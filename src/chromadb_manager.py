from src.config import settings
from src.paths import CHROMA_DB_PATH
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma



api_key = settings['openai']
model = 'text-embedding-3-large'
llm_embedding = OpenAIEmbeddings(api_key=api_key, model=model)


class ChromaDBManager:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model=model, api_key=api_key)
        self.vectorstore = Chroma(
            collection_name = 'test',
            embedding_function=self.embeddings,
            persist_directory = str(CHROMA_DB_PATH),
        )
    
    def store(
            self,
            texts: list[str],
            ids: list[str],
            metadatas: list[dict],
    ):
        ...

    def find(
            self,
            metadata: dict,
    ):
        ...
    
    def query(
            self,
            query: str,
            metadata: dict,
            k: int = 2,
    ):
        ...

    def drop(
            self,
            metadata: dict,
    ):
        ...

