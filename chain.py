from utils.Enums import LLM_MODEL
from utils.LLMS import SelectLLM
from utils.ResponseFormat import corrent_parser, optim_parser
from utils.RAG.get_retriever import get_retriever, get_multi_retriever
from utils.PromptBase import CORRECT_PROMPT, SUMMARY_PROMPT, OPTIMIZATION_PROMPT
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain.pydantic_v1 import BaseModel, Field
from operator import itemgetter

class CommontPydantic(BaseModel):
    __root__: str

class SummaryPydantic(BaseModel):
    document: str
    question: str

LLM = SelectLLM(model=LLM_MODEL.ChatTongyi)

corrent_chain = (
                    {"document": RunnablePassthrough()} 
                    | CORRECT_PROMPT 
                    | LLM
                    | corrent_parser
                ).with_types(input_type=CommontPydantic)

summary_chain = (
                    {"document": itemgetter("document") 
                    | RunnableLambda(get_multi_retriever), "question": itemgetter("question")} 
                    | SUMMARY_PROMPT 
                    | LLM
                    | StrOutputParser()
                ).with_types(input_type=SummaryPydantic)

optimized_chain = (
                    {"document": RunnablePassthrough()}
                    | OPTIMIZATION_PROMPT
                    | LLM
                    | optim_parser
                  ).with_types(input_type=CommontPydantic)