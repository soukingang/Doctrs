from langchain_core.vectorstores import VectorStoreRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever
from ..Enums import LLM_MODEL
from ..LLMS import SelectLLM
from .file_loader import FileLoader
from .chunks import get_chunks
from .store_vectordb import store_vectordb

def get_retriever(filewithpath: str) -> VectorStoreRetriever:
    loader = FileLoader(filewithpath).get_loader()
    chunks = get_chunks(loader)
    db = store_vectordb(chunks)
    return db.as_retriever()

def get_multi_retriever(filewithpath: list[str]) -> VectorStoreRetriever:
    return MultiQueryRetriever.from_llm(
                retriever=get_retriever(filewithpath), llm=SelectLLM(model=LLM_MODEL.ChatTongyi)
           )

