import requests
import streamlit as st

from backend.config import get_api_base_url


def show_api_error(response):
    try:
        error_body = response.json()
        st.error(error_body.get("detail", "The API returned an error."))
    except ValueError:
        st.error("The API returned an error.")


st.title("Login")
st.write("Register first if you are new. Then log in to open the dashboard and chat pages.")

api_base_url = get_api_base_url()

login_tab, register_tab = st.tabs(["Login", "Register"])

with login_tab:
    st.subheader("Existing user")

    with st.form("login_form"):
        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input("Password", type="password", key="login_password")
        login_submitted = st.form_submit_button("Log in")

    if login_submitted:
        try:
            response = requests.post(
                f"{api_base_url}/api/auth/login",
                json={
                    "username": login_username,
                    "password": login_password,
                },
                timeout=10,
            )

            if response.status_code == 200:
                response_data = response.json()
                user = response_data["user"]

                st.session_state["is_authenticated"] = True
                st.session_state["user"] = user

                st.success("Login successful. You can now open the dashboard.")
            else:
                show_api_error(response)
        except requests.RequestException as error:
            st.error("Login failed because the FastAPI server could not be reached.")
            st.caption("Make sure the API is running with `uvicorn backend.main:app --reload`.")
            st.code(str(error))

with register_tab:
    st.subheader("New user")

    with st.form("register_form"):
        register_username = st.text_input("Username", key="register_username")
        register_password = st.text_input(
            "Password",
            type="password",
            key="register_password",
        )
        first_name = st.text_input("First name", key="register_first_name")
        last_name = st.text_input("Last name", key="register_last_name")
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        gender = st.selectbox(
            "Gender",
            ["Female", "Male", "Non-binary", "Prefer not to say"],
        )
        email = st.text_input("Email", key="register_email")
        register_submitted = st.form_submit_button("Create account")

    if register_submitted:
        try:
            response = requests.post(
                f"{api_base_url}/api/auth/register",
                json={
                    "username": register_username,
                    "password": register_password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "age": age,
                    "gender": gender,
                    "email": email,
                },
                timeout=10,
            )

            if response.status_code == 201:
                st.success("Registration successful. You can now log in.")
            else:
                show_api_error(response)
        except requests.RequestException as error:
            st.error("Registration failed because the FastAPI server could not be reached.")
            st.caption("Make sure the API is running with `uvicorn backend.main:app --reload`.")
            st.code(str(error))
