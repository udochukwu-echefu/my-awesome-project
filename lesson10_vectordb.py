from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

# ── STEP 1: Load & split the document (same as Lesson 9) ──
loader = TextLoader("company_info.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
chunks = splitter.split_documents(documents)

print(f"Split into {len(chunks)} chunks")

# ── STEP 2: Create the embedding model ──────────────────
# This turns text into numbers that capture meaning
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# ── STEP 3: Store chunks in a vector database ───────────
print("Creating vector database... (first run downloads the model)")
vectordb = Chroma.from_documents(chunks, embeddings)
print("Vector database ready!")

# ── STEP 4: Search by MEANING, not keywords ─────────────
question = "Who is the boss of the company?"
results = vectordb.similarity_search(question, k=2)

print(f"\nQuestion: {question}")
print("\nMost relevant chunks found:")
for i, doc in enumerate(results):
    print(f"\n--- Match {i+1} ---")
    print(doc.page_content)