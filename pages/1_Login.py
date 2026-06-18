import streamlit as st

st.title("Login")
st.write("This page will handle login and registration eventually. For phase 1 we will only show placeholder forms.")

st.subheader("Login placeholder")
with st.form("login_form"):
    login_email = st.text_input("Email")
    login_password = st.text_input("Password", type="password")
    login_submitted = st.form_submit_button("Log in")

    if login_submitted:
        st.info("Login is not implemented yet.")

st.subheader("Register placeholder")
with st.form("Register_form"):
    register_email = st.text_input("Email", key="register_email")
    display_name = st.text_input("Display name")
    register_password = st.text_input("Password", type="password", key="register_password")
    register_submitted = st.form_submit_button("Create account")

    if register_submitted:
        st.info("Registration is not implemented yet.")

