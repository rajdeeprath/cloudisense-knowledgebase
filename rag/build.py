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
knowledgebase = os.path.join(parent_path, "docs", "markdown", "knowledge")
dbpath = os.path.join(parent_path, "knowledge_db")
dbname = "knowledge.db"


load_dotenv(dotenv_path=os.path.expanduser('~/.env'))

openai_api_key = os.getenv("OPENAI_API_KEY")

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

print("done")