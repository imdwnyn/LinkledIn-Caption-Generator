from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()

def get_caption_chain():
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama3-70b-8192"
    )

    prompt = PromptTemplate.from_template("""
You are a professional LinkedIn content creator.

Project Title: {title}
Description: {description}
Tech Stack: {tech}
Outcome: {outcome}
Reflection: {reflection}
Tone: {tone}

Add emojis, relevant hashtags, and keep it inspiring and clear.
""")

    chain = prompt | llm
    return chain