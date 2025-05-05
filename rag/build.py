import os
import sys
import json
import pickle

import faiss
from dotenv import load_dotenv

from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


def load_openai_key():
    dotenv_path = os.getenv("ENV_OPENAI_DOT_ENV_FILE")
    if dotenv_path and os.path.isfile(dotenv_path):
        load_dotenv(dotenv_path=dotenv_path)
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            return api_key

    api_key = os.getenv("ENV_OPENAI_API_KEY")
    if api_key:
        return api_key

    default_env = os.path.expanduser("~/.env")
    if os.path.isfile(default_env):
        load_dotenv(dotenv_path=default_env)
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            return api_key

    print("Could not find OpenAI API key from any source.")
    sys.exit(1)



dir_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(dir_path)
config_path = os.path.join(parent_path, "config.json")
with open(config_path, "r") as f:
    config = json.load(f)

knowledgebase = os.path.join(parent_path, config["paths"]["knowledge_base"])
dbpath = os.path.join(parent_path, config["paths"]["database_path"])
dbname = config["paths"]["database_name"]

openai_api_key = load_openai_key()

loader = DirectoryLoader(
    knowledgebase,
    glob="**/*.md", 
    show_progress=True,
    loader_cls=TextLoader
)

documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, 
    chunk_overlap=50,
)

docs = splitter.split_documents(documents)

embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)

os.makedirs(dbpath, exist_ok=True)

vectorstore = FAISS.from_documents(docs, embedding_function)

faiss.write_index(vectorstore.index, os.path.join(dbpath, dbname))

with open(os.path.join(dbpath, "docstore.pkl"), "wb") as f:
    pickle.dump(vectorstore.docstore, f)

with open(os.path.join(dbpath, "index_to_docstore_id.pkl"), "wb") as f:
    pickle.dump(vectorstore.index_to_docstore_id, f)
