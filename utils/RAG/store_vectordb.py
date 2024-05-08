from ..Enums import VectorDB
from langchain.vectorstores.chroma import Chroma
from langchain.schema.document import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore
from langchain_community.embeddings.dashscope import DashScopeEmbeddings

def store_vectordb(chunks: list[Document], dbtype: str=VectorDB.Chroma, embedding_function: Embeddings=DashScopeEmbeddings()) -> VectorStore:
    if dbtype == VectorDB.Chroma:
        return Chroma.from_documents(chunks, embedding_function)
    else:
        raise NotImplementedError



