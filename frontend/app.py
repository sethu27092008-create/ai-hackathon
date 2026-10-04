import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/summarize"

st.title("AI Text Summarizer")

text = st.text_area("Paste your text here", height=250)
style = st.selectbox("Summary style", ["short", "detailed", "bullet points"])

if st.button("Summarize"):
    if len(text.strip()) < 20:
        st.warning("Please paste at least a few sentences.")
    else:
        with st.spinner("Thinking..."):
            try:
                res = requests.post(API_URL, json={"text": text, "style": style}, timeout=60)
                if res.status_code == 200:
                    st.subheader("Summary")
                    st.write(res.json()["summary"])
                else:
                    st.error(f"Error: {res.text}")
            except Exception as e:
                st.error(f"Could not reach the backend: {e}")