import streamlit as st
st.title("Dashboard")
st.write("This page will eventually show your saved dialogues. For Phase 1, it only shows placeholders.")

if st.button("Create new dialogue"):
    st.info("Dialogue creation is not implemented yet.")

st.subheader("Dialogue history")
st.write("No saved dialogues yet.")

st.caption("Later this page will read dialogues that belong to the current user.")