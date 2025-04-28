# Cloudisense knowledgebase

All technical documentation related to cloudisense can be found here.


## Retrieval-Augmented Generation (RAG) System for CloudiSENSE SmartAssistant

---

## 📊 Overview

This project implements a simple, production-ready **Retrieval-Augmented Generation (RAG)** system that:

- **Embeds Markdown documents** into vector space.
- **Stores embeddings** in a local **FAISS vector database**.
- **Retrieves** the most relevant document chunks based on user queries.
- **Generates answers** using OpenAI's ChatCompletion API, enhanced by retrieved knowledge.

It specifically generates the vector database for **CloudiSENSE SmartAssistant**.
It uses **OpenAI Embeddings** and a collection of **Markdown documents about various CloudiSENSE topics** to build the knowledge base.

The **vector database file generated here is distributed along with CloudiSENSE** to activate the **SmartAssistant** feature.

---

## 💡 Technologies Used

- **FAISS** (Facebook AI Similarity Search)
- **OpenAI API** (Embeddings + ChatCompletion)
- **LangChain** framework (integration layer)
- **LangChain-OpenAI** package
- **LangChain-Community** package
- **Python-Dotenv** (manage API keys securely)

---

## 📖 Workflow

1. **Load Documents**
   - Markdown files (`.md`) are loaded from a specified folder.

2. **Split Documents**
   - Large documents are split into smaller, manageable chunks using recursive splitting.

3. **Embed Chunks**
   - Each chunk is converted into a vector using OpenAI's embedding model (`text-embedding-ada-002`).

4. **Build FAISS Database**
   - Embeddings are stored into a FAISS index.
   - Text chunks and ID mappings are saved manually alongside.

5. **Save FAISS Database**
   - Three files are saved:
     - `knowledge.db` (formerly `index.faiss`)
     - `docstore.pkl`
     - `index_to_docstore_id.pkl`

6. **Load FAISS Database in Application**
   - FAISS index, document store, and mappings are loaded at runtime.

7. **Querying**
   - User's question is embedded using the same embedding model.
   - Top-k similar document chunks are retrieved.
   - Retrieved chunks + original question are passed to OpenAI GPT to generate a final answer.

---

## 📁 Project Structure

```plaintext
knowledge/               # Folder containing Markdown files
knowledge_vector_db/      # Folder containing saved FAISS database
    ├── knowledge.db          # FAISS index file
    ├── docstore.pkl
    └── index_to_docstore_id.pkl
.env                      # Contains OPENAI_API_KEY
rag/build.py              # Script to generate vector database from Markdown
rag/retrieve.py           # Script to load and retrieve data from the vector database
```

---

## 🔧 Installation

```bash
pip install langchain faiss-cpu openai python-dotenv langchain-openai langchain-community
```

---

## 🔗 Setting Up Environment Variables

Create a `.env` file in your home directory on the development system:

```dotenv
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxx
```

- `.env` is located in the development system's **home directory**.
- It securely contains your **OpenAI API key**.

---

## 💬 Preparing and Using the Vector Database

1. **Run `rag/build.py`** to generate the vector database and accompanying files.
2. **Run `rag/retrieve.py`** to load the database and execute a test search on it.

---

## 💬 Querying and Generating Answers

```python
import openai

query = "How do I install CloudiSENSE?"
retrieved_docs = vectorstore.similarity_search(query, k=3)
context = "\n\n".join(doc.page_content for doc in retrieved_docs)

full_prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question: {query}

Answer:
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": full_prompt}
    ],
    temperature=0.2
)

final_answer = response['choices'][0]['message']['content']
print(final_answer)
```

---

## 🔓 Key Best Practices

- Always **use the same embedding model** during vector creation and query time.
- Use **lower temperature** in OpenAI ChatCompletion for factual answers.
- Set up **environment variables** securely for API keys.
- **Save and organize** your FAISS files properly.
- If large corpus, increase FAISS `k` search value to find more relevant documents.

---

# 🚀 Conclusion

This RAG system efficiently combines vector search (FAISS) and language generation (OpenAI) to build a powerful knowledge retrieval assistant.
It can be easily extended to larger datasets, production APIs, or embedded inside applications!

---


