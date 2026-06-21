from datetime import datetime
from uuid import uuid4

import streamlit as st

if not st.session_state.get("is_authenticated"):
    st.warning("Please log in before opening the dashboard.")
    st.stop()

current_user = st.session_state.get("user") or {}


def get_user_history_key(user):
    user_key = user.get("id") or user.get("username") or "anonymous"

    return f"dialogue_history_{user_key}"


def create_dialogue():
    now = datetime.now().isoformat(timespec="seconds")

    dialogue = {
        "id": str(uuid4()),
        "title": "New dialogue",
        "messages": [],
        "created_at": now,
        "updated_at": now,
    }

    st.session_state[history_key].append(dialogue)
    st.session_state["active_dialogue_id"] = dialogue["id"]
    st.switch_page("pages/3_Chat.py")


def open_dialogue(dialogue_id):
    st.session_state["active_dialogue_id"] = dialogue_id
    st.switch_page("pages/3_Chat.py")


history_key = get_user_history_key(current_user)

if history_key not in st.session_state:
    st.session_state[history_key] = []

st.title("Dashboard")
st.write("Create a dialogue first, then open it to continue chatting.")

first_name = current_user.get("first_name")
username = current_user.get("username")
display_name = first_name or username

st.success(f"Welcome, {display_name}.")

if st.button("Create new dialogue"):
    create_dialogue()

st.subheader("Dialogue history")

if not st.session_state[history_key]:
    st.write("No saved dialogues yet.")
else:
    for dialogue in reversed(st.session_state[history_key]):
        with st.container(border=True):
            st.write(dialogue["title"])
            st.caption(
                f"{len(dialogue['messages'])} messages - Updated {dialogue['updated_at']}"
            )

            if st.button("Open dialogue", key=f"open_dialogue_{dialogue['id']}"):
                open_dialogue(dialogue["id"])

st.caption("Later this page will read dialogues that belong to the current user from Neon.")
