from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# ── STEP 1: Load the document ─────────────────────
loader = TextLoader("company_info.txt")
documents = loader.load()

print(f"Loaded {len(documents)} document")
print(f"Total characters: {len(documents[0].page_content)}")
print()

# ── STEP 2: Split into chunks ─────────────────────
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=30
)

chunks = splitter.split_documents(documents)

print(f"Split into {len(chunks)} chunks")
print()

# ── STEP 3: See the chunks ────────────────────────
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk.page_content)
    print()