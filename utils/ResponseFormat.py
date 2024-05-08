from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

class CorrectResult(BaseModel):
    CorrectContent: str = Field(description="已修正后的文章内容")
    MistakeContent: str = Field(description="已发现的文章中的错误内容")
    AnalysisContent: List[str] = Field(description="已发现的错误内容的修改解释内容")

corrent_parser = JsonOutputParser(pydantic_object=CorrectResult)
corrent_format = corrent_parser.get_format_instructions()

class OPTIMResult(BaseModel):
    OPTIMSummary: str = Field(description="已优化后的文章内容")
    OPTIMAnalysis: List[str] = Field(description="对文章内容的优化分析")
    OPTIMAdvice: List[str] = Field(description="对文章内容的改进建议")

optim_parser = JsonOutputParser(pydantic_object=OPTIMResult)
optim_format = optim_parser.get_format_instructions()
