import json
from langchain.document_loaders import TextLoader 

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import DirectoryLoader

import pickle
import faiss
import os
from dotenv import load_dotenv

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(dir_path)
config_path = os.path.join(parent_path, "config.json")
with open(config_path, "r") as f:
    config = json.load(f)

knowledgebase = os.path.join(parent_path, config["paths"]["knowledge_base"])
dbpath = os.path.join(parent_path, config["paths"]["database_path"])
dbname = config["paths"]["database_name"]


load_dotenv(dotenv_path=os.path.expanduser('~/.env'))

openai_api_key = os.getenv("OPENAI_API_KEY")

embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)

index = faiss.read_index(os.path.join(dbpath, dbname))

with open(os.path.join(dbpath, "docstore.pkl"), "rb") as f:
    docstore = pickle.load(f)

with open(os.path.join(dbpath, "index_to_docstore_id.pkl"), "rb") as f:
    index_to_docstore_id = pickle.load(f)

vectorstore = FAISS(
    embedding_function=embedding_function,
    index=index,
    docstore=docstore,
    index_to_docstore_id=index_to_docstore_id,
)

# Example
query = "How do I install CloudiSENSE on Linux?"
retrieved_docs = vectorstore.similarity_search(query, k=3)
context = "\n\n".join(doc.page_content for doc in retrieved_docs)
print(context)

