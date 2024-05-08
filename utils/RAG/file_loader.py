from typing import List
from langchain.document_loaders.text import TextLoader
from langchain.document_loaders.pdf import PyPDFLoader
from langchain_core.documents import Document

class FileLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_loader(self) -> List[Document]:
        if self.file_path.endswith(".pdf"):
            return PyPDFLoader(self.file_path).load()
        else:
            return TextLoader(self.file_path).load()