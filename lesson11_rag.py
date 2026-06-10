from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# ── STEP 1: Load, split & store the document ──────────
loader = TextLoader("company_info.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma.from_documents(chunks, embeddings)

print("Knowledge base ready!")

# ── STEP 2: Set up the AI model ───────────────────────
llm = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# ── STEP 3: Create a RAG prompt ───────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the question using ONLY the context below. If the answer isn't in the context, say you don't know.\n\nContext:\n{context}"),
    ("human", "{question}")
])

# ── STEP 4: The RAG function ──────────────────────────
def ask(question):
    # 4a. Search the vector DB for relevant chunks
    results = vectordb.similarity_search(question, k=3)

    # 4b. Combine the found chunks into one block of text
    context = "\n\n".join([doc.page_content for doc in results])

    # 4c. Fill the prompt and send to the AI
    chain = prompt | llm
    response = chain.invoke({"context": context, "question": question})

    return response.content

# ── STEP 5: Chat loop ─────────────────────────────────
print("Ask me anything about TechNova. Type 'quit' to exit.")
print("-" * 50)

while True:
    user_question = input("You: ")
    if user_question.lower() == "quit":
        print("Goodbye!")
        break

    answer = ask(user_question)
    print(f"AI: {answer}")
    print()