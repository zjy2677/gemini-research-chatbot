import requests
import streamlit as st

from backend.config import get_api_base_url


if not st.session_state.get("is_authenticated"):
    st.warning("Please log in before opening the chat page.")
    st.stop()

if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []

st.title("Chat")

st.write(
    "This page now sends normal chat messages to Gemini through the FastAPI backend."
)

chat_modes = [
    "chat",
    "sources",
    "research",
    "report",
]

chat_mode = st.selectbox(
    "Choose a mode",
    chat_modes,
    index=0,
)

gemini_models = {
    "Gemini 3.5 Flash": "gemini-3.5-flash",
    "Gemini 2.5 Pro": "gemini-2.5-pro",
    "Gemini 2.5 Flash": "gemini-2.5-flash",
    "Gemini 2.0 Flash": "gemini-2.0-flash",
    "Gemini 2.0 Flash Lite": "gemini-2.0-flash-lite",
}

model_name = st.selectbox(
    "Choose a model",
    list(gemini_models.keys()),
)

model_id = gemini_models[model_name]

st.caption(f"Selected mode: {chat_mode}")
st.caption(f"Selected model: {model_name} ({model_id})")

if chat_mode != "chat":
    st.info("Only normal chat mode is connected to Gemini in this step.")

st.subheader("Messages")

for message in st.session_state["chat_messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_message = st.chat_input("Ask Gemini something...")

if user_message:
    st.session_state["chat_messages"].append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    with st.chat_message("user"):
        st.write(user_message)

    if chat_mode != "chat":
        assistant_message = "This mode is not implemented yet. Switch to chat mode to talk with Gemini."
        st.session_state["chat_messages"].append(
            {
                "role": "assistant",
                "content": assistant_message,
            }
        )

        with st.chat_message("assistant"):
            st.write(assistant_message)
    else:
        try:
            response = requests.post(
                f"{get_api_base_url()}/api/agent/chat",
                json={
                    "message": user_message,
                    "model": model_id,
                },
                timeout=60,
            )

            if response.status_code == 200:
                assistant_message = response.json()["message"]
            else:
                error_body = response.json()
                assistant_message = error_body.get("detail", "Gemini request failed.")
        except requests.RequestException as error:
            assistant_message = "The FastAPI server could not be reached."
            st.caption("Make sure the API is running with `python3 -m uvicorn backend.main:app --reload`.")
            st.code(str(error))

        st.session_state["chat_messages"].append(
            {
                "role": "assistant",
                "content": assistant_message,
            }
        )

        with st.chat_message("assistant"):
            st.write(assistant_message)

if st.button("Clear chat"):
    st.session_state["chat_messages"] = []
    st.rerun()
