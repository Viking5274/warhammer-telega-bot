from llama_index import VectorStoreIndex, SimpleDirectoryReader

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


class MyBigLlama:

    def __init__(self):
        documents = SimpleDirectoryReader('data').load_data()
        self.index = VectorStoreIndex.from_documents(documents)
        self.query_engine = self.index.as_query_engine()
        self.index.storage_context.persist()

    def send_question(self, question: str):

        print(question)
        response = self.query_engine.query(question)
        return response
