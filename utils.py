import fitz  # PyMuPDF

def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    else:
        return uploaded_file.read().decode("utf-8", errors="ignore")




