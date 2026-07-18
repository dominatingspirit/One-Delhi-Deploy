import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Elastic Client
ES_CLIENT = Elasticsearch(
    cloud_id=os.getenv("ES_CLOUD_ID"),
    api_key=os.getenv("ES_API_KEY")
)

# Gemini Client
from langchain_openai import ChatOpenAI


# Initialize the OpenAI model
LLM = ChatOpenAI(
    model="gpt-4o", # You can also use "gpt-4o-mini"
    temperature=0.7, 
)
