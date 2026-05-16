from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# 1. Create the model
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add it to your environment and retry."
    )


model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9, api_key=api_key)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful teacher. Explain in simple English."),
    ("human", "Explain {topic} with a simple example.")
])
parser = StrOutputParser()


chain = prompt | model | parser


result = chain.invoke({"topic": "Python programming"})
print(result)