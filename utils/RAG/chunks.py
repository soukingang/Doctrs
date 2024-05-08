from typing import List
from langchain_core.document_loaders.base import BaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_chunks(documents: BaseLoader) -> List:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    return chunks