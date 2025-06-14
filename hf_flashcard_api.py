import google.generativeai as genai
import streamlit as st
import os
import re

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found. Set it in environment variables or Streamlit Secrets.")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_flashcards(text, subject=None):
    prompt = f"""
Generate 10 to 12 high-quality flashcards from the following educational text.
Each flashcard should have:
Q: A concise question
A: A correct and informative answer

Format exactly like:
Q: [question]
A: [answer]

{"Subject: " + subject if subject else ""}
Text:
{text}
"""
    try:
        response = model.generate_content(prompt)
        generated_text = response.text.strip()

        flashcards = []
        matches = re.findall(r"Q:\s*(.*?)\s*A:\s*(.*?)(?=\nQ:|\Z)", generated_text, re.DOTALL)

        for q, a in matches:
            q = q.strip()
            a = a.strip()
            if q and a:
                flashcards.append(f"Q: {q}")
                flashcards.append(f"A: {a}")

        if not flashcards:
            return ["No flashcards could be parsed from the response."]
        return flashcards[:24] 

    except Exception as e:
        print("Error:", e)
        return [f"Error: {str(e)}"]




