import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# ── Build the knowledge base (only ONCE, cached) ──────
@st.cache_resource
def load_knowledge_base():
    loader = TextLoader("company_info.txt")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(chunks, embeddings)
    return vectordb

# ── Set up the AI model ───────────────────────────────
llm = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the question using ONLY the context below. If the answer isn't in the context, say you don't know.\n\nContext:\n{context}"),
    ("human", "{question}")
])

# ── The RAG function ──────────────────────────────────
def ask(question, vectordb):
    results = vectordb.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in results])
    chain = prompt | llm
    response = chain.invoke({"context": context, "question": question})
    return response.content

# ── THE WEB INTERFACE ─────────────────────────────────
st.title("🏢 TechNova Assistant")
st.write("Ask me anything about TechNova Nigeria!")

# Load the knowledge base
vectordb = load_knowledge_base()

# Text input for the user's question
question = st.text_input("Your question:")

# When they ask, run RAG and show the answer
if question:
    with st.spinner("Thinking..."):
        answer = ask(question, vectordb)
    st.write("### Answer:")
    st.write(answer)