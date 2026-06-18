import streamlit as st

st.title("Chat")

st.write(
    "This page will eventually support normal chat, deep research, "
    "image generation, and coding assistance."
)

chat_modes = [
    "chat",
    "deep research",
    "pictures generation",
    "coding assistant",
]

chat_mode = st.selectbox(
    "Choose a mode",
    chat_modes,
    index=0,
)

text_models = [
    "Gemini 2.5 Pro",
    "Gemini 2.5 Flash",
    "Gemini 2.5 Flash Lite",
    "Gemini 2 Flash",
    "Gemini 2 Flash Lite",
    "Gemini 3 Flash",
    "Gemini 3.5 Flash",
    "Gemini 3.1 Pro",
    "Gemini 3.1 Flash Lite",
]

image_models = [
    "Nano Banana (Gemini 2.5 Flash Preview Image)",
    "Nano Banana Pro (Gemini 3 Pro Image)",
    "Nano Banana 2 (Gemini 3.1 Flash Image)",
    "Imagen 4 Fast Generate",
    "Imagen 4 Generate",
    "Imagen 4 Ultra Generate",
]

agent_models = [
    "Deep Research Pro Preview",
    "Antigravity",
    "Computer Use Preview",
]

if chat_mode == "pictures generation":
    model_options = image_models
elif chat_mode == "deep research":
    model_options = agent_models
else:
    model_options = text_models

model_name = st.selectbox(
    "Choose a model",
    model_options,
)

st.caption(f"Selected mode: {chat_mode}")
st.caption(f"Selected model: {model_name}")

user_message = st.chat_input("Ask something...")

st.subheader("Messages")

if user_message:
    st.info("Message sending is not implemented yet.")
    st.write(f"You typed: {user_message}")
else:
    st.write("No messages yet.")

st.markdown(
    """
    **Mode plan for later phases**

    - chat: normal Gemini conversation
    - deep research: use a research agent workflow
    - pictures generation: generate images from prompts
    - coding assistant: help write, debug, and explain code
    """
)