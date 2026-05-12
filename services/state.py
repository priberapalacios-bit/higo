import streamlit as st


def init_state():
    defaults = {
        "exercise": False,
        "support": False,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
