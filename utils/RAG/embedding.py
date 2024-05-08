from langchain_core.embeddings import Embeddings
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_openai.embeddings import OpenAIEmbeddings


def get_embedding_function(model_type: str) -> Embeddings:
    if model_type == "openai":
        embeddings = OpenAIEmbeddings()
    if model_type == "ollama":
        embeddings = OllamaEmbeddings(model="llama3")
    elif model_type == "bedrock":
        embeddings = BedrockEmbeddings(
            credentials_profile_name="default", region_name="us-east-1"
    )
    return embeddings