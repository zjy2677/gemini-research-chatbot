# Phase 1 instructions for app.py
#
# Purpose:
# app.py is the main Streamlit entry point.
# When you run "streamlit run app.py", Streamlit starts here first.
# In this project, app.py should act as a simple landing page.
#
# Minimal Phase 1 behavior:
# The landing page should:
# 1. Set the browser tab title.
# 2. Show a main title for the project.
# 3. Explain that this is a learning-focused chatbot app.
# 4. Tell the user to use the sidebar to open Login, Dashboard, or Chat.
#
# Important:
# Streamlit automatically discovers files inside the pages/ folder.
# Because this project has:
#
#     pages/1_Login.py
#     pages/2_Dashboard.py
#     pages/3_Chat.py
#
# Streamlit will show those pages in the sidebar when the app runs.
#
# Step-by-step code to type manually:
#
# 1. Import Streamlit.
#
# import streamlit as st
#
# Explanation:
# "st" is the common nickname for the Streamlit library.
# Every visible Streamlit UI element will be created through st.something.
#
# 2. Configure the page.
#
# st.set_page_config(
#     page_title="Gemini Research Chatbot",
#     page_icon="💬",
#     layout="wide",
# )
#
# Explanation:
# page_title controls the browser tab title.
# page_icon controls the small icon in the browser tab.
# layout="wide" gives the app more horizontal space, which will help later
# when we build a chat layout and source panels.
#
# 3. Add the landing page title.
#
# st.title("Gemini Research Chatbot")
#
# Explanation:
# st.title creates a large page heading.
# This is the first thing users see on the landing page.
#
# 4. Add a short explanation.
#
# st.write(
#     "A learning-focused Streamlit app for chat, web research, source review, "
#     "and PDF report generation."
# )
#
# Explanation:
# st.write is a flexible Streamlit function for showing text.
# This description keeps the landing page simple and honest.
#
# 5. Add a Phase 1 note.
#
# st.info(
#     "Phase 1 only builds the app shell. Authentication, database storage, "
#     "Gemini calls, and React components will come later."
# )
#
# Explanation:
# st.info shows a highlighted message box.
# This reminds you that the current version is intentionally incomplete.
#
# 6. Add navigation guidance.
#
# st.subheader("Navigation")
# st.write("Use the sidebar to open Login, Dashboard, or Chat.")
#
# Explanation:
# st.subheader creates a smaller heading.
# The sidebar navigation is handled automatically by Streamlit because of
# the files in the pages/ folder.
#
# How to test this file:
# 1. Make sure requirements.txt has streamlit uncommented and installed.
# 2. Run this from the project root:
#
#        streamlit run app.py
#
# 3. The browser should open the landing page.
# 4. You should see the project title and the sidebar page links.
#
# Learning note:
# app.py is not a backend server file in this Streamlit version.
# It is the UI entry point. Later, app.py can call backend service modules,
# but it should not contain database or Gemini logic directly.

import streamlit as st


def show_home_page():
    st.title("Gemini Chatbot")

    st.write(
        "A learning-focused Streamlit app for chat, web research, "
        "source review, and PDF report generation."
    )

    st.info(
        "Phase 1 only builds the app shell. Authentication, database storage, "
        "Gemini calls, and React components will come later."
    )

    st.subheader("Navigation")
    st.write("Use the sidebar to open Login, Dashboard, or Chat.")


st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="💬",
    layout="wide",
)

home_page = st.Page(show_home_page, title="Home")
login_page = st.Page("pages/1_Login.py", title="Login")
dashboard_page = st.Page("pages/2_Dashboard.py", title="Dashboard")
chat_page = st.Page("pages/3_Chat.py", title="Chat")

selected_page = st.navigation(
    [
        home_page,
        login_page,
        dashboard_page,
        chat_page,
    ]
)

selected_page.run()
