import streamlit as st
from llama_chain import get_caption_chain

st.set_page_config(page_title="LinkedIn Caption Generator", layout="centered")
st.title("🔗 LinkedIn Project Caption Generator")

# Input fields
title = st.text_input("Project Title")
description = st.text_area("Project Description")
tech = st.text_input("Tech Stack")
outcome = st.text_area("Outcome")
reflection = st.text_area("Personal Reflection")
tone = st.selectbox("Tone", ["Professional", "Enthusiastic", "Humble", "Motivational"])

caption_chain = get_caption_chain()

# State management
if "input_data" not in st.session_state:
    st.session_state.input_data = {}

# Generate button
if st.button("Generate Caption"):
    inputs = {
        "title": title,
        "description": description,
        "tech": tech,
        "outcome": outcome,
        "reflection": reflection,
        "tone": tone
    }
    st.session_state.input_data = inputs
    result = caption_chain.invoke(inputs)
    st.session_state.last_caption = result.content
    st.session_state.pop("copied", None)

# Regenerate button
if st.button("🔄 Regenerate Caption") and st.session_state.get("input_data"):
    result = caption_chain.invoke(st.session_state.input_data)
    st.session_state.last_caption = result.content
    st.session_state.pop("copied", None)

# Show result
if "last_caption" in st.session_state:
    st.subheader("📣 Your LinkedIn Caption:")
    st.code(st.session_state.last_caption, language="markdown")

    def mark_as_copied():
        st.session_state["copied"] = True

    if st.button("📋 Copy Caption", on_click=mark_as_copied):
        st.toast("✅ Caption copied to clipboard!")

    if st.session_state.get("copied"):
        st.success("Caption copied!")
