from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
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


@tool
def sum(a, b):
    """Returns the sum of two numbers."""
    return a + b


mathAgent = create_agent(
    model = model,
    tools = [sum],
    system_prompt="You are a helpful assistant that can perform mathematical operations. Use the provided tools to answer questions."
)


result = mathAgent.invoke({
    "messages": "What is the sum of 5 and 7?"
})
print(result["messages"][-1].content)






