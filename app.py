import streamlit as st

st.title("Fake News Detector")

# Input box
news_text = st.text_area("Paste news article here:")

# Dummy classifier function
def classify_news(text):
    # This is just a placeholder
    fake_keywords = ["clickbait", "fake", "shocking", "unbelievable", "hoax"]
    for word in fake_keywords:
        if word in text.lower():
            return "Fake News"
    return "Real News"

# Button
if st.button("Check"):
    if news_text.strip() == "":
        st.warning("Please enter some text to check.")
    else:
        result = classify_news(news_text)
        st.success(f"Result: {result}")
