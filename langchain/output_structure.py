from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

# 1. Create the model
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add it to your environment and retry."
    )

model = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=api_key,
)

class output_structure(BaseModel):
    names: str = Field(description="The name of the person.")
    email: str = Field(description="The email of the person.")


structured_model = model.with_output_structure(output_structure)

result = structured_model.invoke({
    "messages": "My Name is John Doe, and email is john.doe@example.com. Provide my details."
})
print(result)






