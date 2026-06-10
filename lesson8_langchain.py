from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# ── STEP 1: Create the AI model ──────────────────
# Groq has an OpenAI-compatible API, so we point langchain-openai at Groq
llm = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# ── STEP 2: Create a prompt template ─────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that explains things simply."),
    ("human", "{question}")
])

# ── STEP 3: Chain them together ───────────────────
chain = prompt | llm

# ── STEP 4: Run the chain ─────────────────────────
response = chain.invoke({"question": "What is artificial intelligence in 2 sentences?"})

print(response.content)