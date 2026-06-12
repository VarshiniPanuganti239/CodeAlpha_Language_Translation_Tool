import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect
import pandas as pd

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Language Translation Tool")

st.write("Translate text between multiple languages")

languages = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter Text",
    height=150
)

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Translate"):

    if text:

        detected = detect(text)

        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Completed")

        st.subheader("Translated Text")

        st.write(translated)

        st.write(f"Detected Language Code: {detected}")

        st.session_state.history.append({
            "Original": text,
            "Translated": translated
        })

if st.session_state.history:

    st.subheader("Translation History")

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(history_df)

    csv = history_df.to_csv(index=False)

    st.download_button(
        "Download History",
        csv,
        "translation_history.csv",
        "text/csv"
    )
