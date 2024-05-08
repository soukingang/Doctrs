from enum import Enum

class LLM_MODEL(Enum):
    ChatTongyi = "ChatTongyi"
    ChatOllama = "ChatOllama"
    ChatOpenAI = "ChatOpenAI"

class VectorDB(Enum):
    Chroma = "Chroma"
    Milvus = "Milvus"
    Weaviate = "Weaviate"
    Qdrant = "Qdrant"
    Pinecone = "Pinecone"
    Supabase = "Supabase"
    OpenAI = "OpenAI"
    WeaviateFlat = "WeaviateFlat"