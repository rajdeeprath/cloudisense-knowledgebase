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

os.makedirs(dbpath, exist_ok=True)


# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.expanduser('~/.env'))

# Now you can access your OpenAI key
openai_api_key = os.getenv("OPENAI_API_KEY")


loader = DirectoryLoader(
    knowledgebase,
    glob="**/*.md",      # Only load .md files recursively
    show_progress=True,  # Optional: show progress while loading
    loader_cls=TextLoader # Use TextLoader internally
)

documents = loader.load()


# Initialize splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Size of each chunk
    chunk_overlap=50,    # How much chunks should overlap (helps in smooth reading)
)

# Split the documents
docs = splitter.split_documents(documents)

# 1. Initialize the embedding function
embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Create FAISS vector database
vectorstore = FAISS.from_documents(docs, embedding_function)


faiss.write_index(vectorstore.index, os.path.join(dbpath, dbname))

with open(os.path.join(dbpath, "docstore.pkl"), "wb") as f:
    pickle.dump(vectorstore.docstore, f)

with open(os.path.join(dbpath, "index_to_docstore_id.pkl"), "wb") as f:
    pickle.dump(vectorstore.index_to_docstore_id, f)

print("done")