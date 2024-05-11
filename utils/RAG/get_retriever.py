from typing import List
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.documents import Document
from ..Enums import LLM_MODEL
from ..LLMS import SelectLLM
from .file_loader import FileLoader
from .chunks import get_chunks
from .store_vectordb import store_vectordb

def format_docs(docs: List[Document]) -> str:
    return ", ".join([doc.page_content for doc in docs])

def _get_retriever(file_args: dict) -> VectorStoreRetriever:
    loader = FileLoader(file_args.get("document")).get_loader()
    chunks = get_chunks(loader)
    db = store_vectordb(chunks)
    return db.as_retriever()

def get_retrieve_context(file_args: dict) -> str:
    return format_docs(_get_retriever(file_args).invoke(file_args.get("question")))

def _get_multi_retriever(file_args: dict) -> MultiQueryRetriever:
    return MultiQueryRetriever.from_llm(
                retriever=_get_retriever(file_args), llm=SelectLLM(model=LLM_MODEL.ChatTongyi)
           )

def get_multi_retrieve_context(file_args: dict) -> str:
    return format_docs(_get_multi_retriever(file_args).invoke(file_args.get("question")))