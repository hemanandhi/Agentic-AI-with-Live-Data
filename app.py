import streamlit as st

st.set_page_config(page_title="Live Document Assistant")
st.title("📄 Live Document Assistant")
st.write("Ask questions from documents that update in real time.")

# Input box for question
question = st.text_input("Ask a question:")

if question:
    # Simple predefined Q&A
    if "python" in question.lower() and "creator" in question.lower():
        st.success("Answer: Python was created by Guido van Rossum.")
    elif "python" in question.lower() and "used" in question.lower():
        st.success("Answer: Python is widely used in AI, data science, and web development.")
    elif "language" in question.lower() and "level" in question.lower():
        st.success("Answer: Python is a high-level programming language.")
    else:
        st.warning("Sorry, I don't know the answer to that question.")
