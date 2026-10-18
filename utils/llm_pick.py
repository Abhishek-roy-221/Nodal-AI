
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def pick_llm(level: str):
    """
    Select an LLM for Nodal based on task complexity.

    Args:
        level: "low", "medium", or "high".

    Returns:
        An initialized LangChain chat model.
    """
    level = level.strip().lower()

    if level == "low":
        # Fast, lightweight tasks: routing, intent detection, simple tool selection
        return ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY"),
        )

    elif level == "medium":
        # Moderate tasks: query rewriting, schema understanding, basic analysis
        return ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )

    elif level == "high":
        # Complex tasks: SQL generation, ETL planning, debugging, result evaluation
        return ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )

    else:
        raise ValueError(
            f"Unsupported level: {level!r}. Choose 'low', 'medium', or 'high'."
        )



if __name__ == "__main__":
    llm_obj = pick_llm("low")  
    print(llm_obj.invoke("What is the capital of France?"))