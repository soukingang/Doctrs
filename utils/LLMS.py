from utils.Enums import LLM_MODEL
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.chat_models.ollama import ChatOllama

def SelectLLM(model: LLM_MODEL):
    if model == LLM_MODEL.ChatTongyi:
        return ChatTongyi(model="qwen-turbo")
    elif model == LLM_MODEL.ChatOllama:
        return ChatOllama(model="llama3")
    return ChatOpenAI(model="gpt-3.5-turbo")