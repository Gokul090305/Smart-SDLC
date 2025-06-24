import streamlit as st
import requests

API_URL = "http://localhost:8000" # Or "http://127.0.0.1:8000"

st.set_page_config(page_title="SmartSDLC", layout="wide")
st.title("🧠 SmartSDLC - AI-Powered Software Development")

menu = ["Requirement Classification", "Code Generator", "Bug Fixer", "Test Case Generator", "Code Summarizer", "Chatbot"]
choice = st.sidebar.selectbox("Select Module", menu)

if choice == "Requirement Classification":
    st.subheader("📄 Upload Requirements Document")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file and st.button("Classify Requirements"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{API_URL}/classify", files=files)
        if response.ok:
            result = response.json()
            for phase, items in result.items():
                st.markdown(f"### {phase}")
                for item in items:
                    st.markdown(f"- {item}")
        else:
            st.error("Classification failed.")

elif choice == "Code Generator":
    st.subheader("💡 Generate Code from Prompt")
    prompt = st.text_area("Describe what you want to build")
    if st.button("Generate Code"):
        res = requests.post(f"{API_URL}/generate-code", json={"prompt": prompt})
        st.code(res.json().get("code"))

elif choice == "Bug Fixer":
    st.subheader("🐞 Fix Buggy Code")
    code = st.text_area("Paste buggy code here")
    if st.button("Fix Code"):
        res = requests.post(f"{API_URL}/bug-fix", json={"code": code})
        st.code(res.json().get("fixed_code"))

elif choice == "Test Case Generator":
    st.subheader("🧪 Generate Test Cases")
    code = st.text_area("Paste functional code here")
    if st.button("Generate Tests"):
        res = requests.post(f"{API_URL}/generate-test", json={"code": code})
        st.code(res.json().get("test_code"))

elif choice == "Code Summarizer":
    st.subheader("📘 Summarize Code")
    code = st.text_area("Paste code to summarize")
    if st.button("Summarize"):
        res = requests.post(f"{API_URL}/summarize", json={"code": code})
        st.success(res.json().get("summary"))

elif choice == "Chatbot":
    st.subheader("💬 Ask the AI Assistant")
    prompt = st.text_input("Ask something about SDLC")
    if st.button("Ask"):
        res = requests.post(f"{API_URL}/chat", json={"prompt": prompt})
        st.info(res.json().get("response"))
