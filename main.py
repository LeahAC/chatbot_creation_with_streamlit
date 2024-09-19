import streamlit as st

st.set_page_config(
    page_title="Welcome to Barcelona",
    page_icon="👋",
)

st.write("# Welcome to Barcelona Onboarding! 👋")

st.sidebar.success("Select a task above.")

st.markdown(
    """
   **👈 Select a task from the sidebar** to start the onboarding process.
"""
)