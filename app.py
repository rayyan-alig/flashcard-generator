import streamlit as st
import csv
import io
from hf_flashcard_api import generate_flashcards
from utils import extract_text_from_file

st.set_page_config(page_title="📚 ShelfEx Flashcard Generator", layout="wide")

st.markdown("""
    <style>
        .flashcard {
            background-color: #f9f9fc;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
        }
        .question {
            font-weight: bold;
            color: #003366;
            font-size: 18px;
        }
        .answer {
            color: #333333;
            font-size: 16px;
            margin-top: 8px;
        }
        .section-title {
            font-size: 24px;
            margin-top: 30px;
            margin-bottom: 10px;
            color: #2e7bcf;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📚 ShelfEx - AI Flashcard Generator")
st.write("Turn any educational text or PDF into beautifully structured flashcards.")

uploaded_file = st.file_uploader("📎 Upload a .txt or .pdf file", type=["txt", "pdf"])
subject = st.selectbox("📘 Select Subject ", ["General", "Biology", "History", "Computer Science", "Medicine"])

if uploaded_file:
    raw_text = extract_text_from_file(uploaded_file)

    if st.button("🧠 Generate Flashcards"):
        with st.spinner("Generating flashcards..."):
            flashcards = generate_flashcards(raw_text, subject)

        st.markdown('<div class="section-title">📝 Generated Flashcards</div>', unsafe_allow_html=True)

        if flashcards and not flashcards[0].startswith("Error"):
            csv_buffer = io.StringIO()
            csv_writer = csv.writer(csv_buffer)
            csv_writer.writerow(["Question", "Answer"])

            for i in range(0, len(flashcards), 2):
                if i + 1 < len(flashcards):
                    question = flashcards[i][3:]
                    answer = flashcards[i+1][3:]
                    csv_writer.writerow([question, answer])

                    st.markdown(f"""
                        <div class="flashcard">
                            <div class="question">Q{i//2 + 1}: {question}</div>
                            <div class="answer">{answer}</div>
                        </div>
                    """, unsafe_allow_html=True)

            st.download_button(
                label="📥 Download Flashcards as CSV",
                data=csv_buffer.getvalue(),
                file_name="flashcards.csv",
                mime="text/csv"
            )
        else:
            st.error(flashcards[0] if flashcards else "❌ Unknown error occurred")




