from ..Enums import EMBEDDING_MODEL
from langchain_core.embeddings import Embeddings
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.dashscope import DashScopeEmbeddings


def get_embedding_function(model_type: EMBEDDING_MODEL) -> Embeddings:
    if model_type == EMBEDDING_MODEL.OpenAI:
        return OpenAIEmbeddings()
    elif model_type == EMBEDDING_MODEL.Ollama:
        return OllamaEmbeddings(model="llama3")
    elif model_type == EMBEDDING_MODEL.DashScope:
        return DashScopeEmbeddings(model="text-embedding-v2")
    raise Exception("Invalid embedding model type")