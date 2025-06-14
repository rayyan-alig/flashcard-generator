# 📚 Flashcard Generator with Gemini API

This is a Streamlit-based web app that generates 12 high-quality flashcards from any educational text using Google's Gemini 2.0 API.

## Features

- Converts educational text into concise Q&A flashcards
- Clean and interactive UI built with Streamlit
- Deployed on Streamlit Cloud

## Tech Stack

- Python 3.12+
- Streamlit
- Google Generative AI (Gemini 2.0)
- Regex for flashcard parsing
- Environment management via `secrets.toml`

---

## Project Structure

┣ 📜app.py				# Streamlit app main file
┣ 📜hf_flashcard_api.py			# Handles Gemini API interaction and flashcard generation
- 📜utils.py				# Handles pdf and text files to upload
┣ 📂.streamlit
┃ ┗ 📜secrets.toml			# Store API key
┣ 📜README.md


## Setup Instructions (Local)

1. **Clone the repository**

```bash
git clone https://github.com/your-username/flashcard-generator.git
cd flashcard-generator



##  Add your Gemini API key

Create a file at:

.streamlit/secrets.toml
Add the following:

GEMINI_API_KEY = "your-gemini-api-key-here"



## Before running the project, ensure you have the following Python packages installed:

streamlit
google-generativeai
and maybe few more



## Run the app

streamlit run app.py