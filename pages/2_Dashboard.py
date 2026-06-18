import streamlit as st

if not st.session_state.get("is_authenticated"):
    st.warning("Please log in before opening the dashboard.")
    st.stop()

current_user = st.session_state.get("user") or {}

st.title("Dashboard")
st.write("This page will eventually show your saved dialogues. For now, it only shows placeholders.")

first_name = current_user.get("first_name")
username = current_user.get("username")
display_name = first_name or username

st.success(f"Welcome, {display_name}.")

if st.button("Create new dialogue"):
    st.info("Dialogue creation is not implemented yet.")

st.subheader("Dialogue history")
st.write("No saved dialogues yet.")

st.caption("Later this page will read dialogues that belong to the current user.")
