import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="KI‑Branding Generator (Gemini)", layout="centered")
st.title("🧠 KI‑Branding Generator – Gemini Version")

idee = st.text_input("Was machst du?")
zielgruppe = st.text_input("Wer ist deine Zielgruppe?")
stil = st.text_input("Wie soll deine Marke wirken?")
api_key = st.text_input("Gemini API-Key", type="password")

if st.button("Branding generieren"):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Du bist Branding-Experte. Erstelle für mich:
    Geschäftsidee: {idee}
    Zielgruppe: {zielgruppe}
    Stil: {stil}
    Bitte antworte auf Deutsch:
    Name:
    Slogan:
    Beschreibung:
    """
    with st.spinner("Generiere…"):
        response = model.generate_content(prompt)
    st.success("Fertig! 🎉")
    st.text_area("Dein Branding:", response.text, height=200)
