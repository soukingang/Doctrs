from ..Enums import VectorDB
from ..Enums import EMBEDDING_MODEL
from .embedding import get_embedding_function
from langchain_community.vectorstores import Chroma
from langchain.schema.document import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore
from langchain_community.embeddings.dashscope import DashScopeEmbeddings

def store_vectordb(chunks: list[Document],
                   docId: str="1781251691062235136:332223",
                   dbtype: VectorDB=VectorDB.Chroma,
                   embedding: EMBEDDING_MODEL=EMBEDDING_MODEL.DashScope) -> VectorStore:
    doc_to_store = [Document(page_content=chunk.page_content, metadata={'attr': docId}) for chunk in chunks if chunk]
    if dbtype == VectorDB.Chroma:
        vectorstore = Chroma(embedding_function=get_embedding_function(embedding))
    else:
        raise NotImplementedError

    if not vectorstore.get(where={"attr": {"$eq": docId}})["documents"]:
        vectorstore.add_documents(doc_to_store)
    return vectorstore