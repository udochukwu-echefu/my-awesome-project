import streamlit as st

# ── Page title ────────────────────────────────────
st.title("🚀 My First Web App")

# ── Some text ─────────────────────────────────────
st.write("Hello! This is a website built entirely in Python.")

# ── A text input box ──────────────────────────────
name = st.text_input("What is your name?")

# ── A button ──────────────────────────────────────
if st.button("Greet me"):
    st.write(f"Welcome, {name}! 👋")

# ── A slider ──────────────────────────────────────
age = st.slider("How old are you?", 1, 100, 25)
st.write(f"You are {age} years old.")