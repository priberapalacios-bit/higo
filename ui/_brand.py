import streamlit as st


def apply_branding() -> None:
    """Aplica estilos globales de la aplicación."""
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #F7F7F7;
        }

        h1, h2, h3 {
            color: #1E293B;
        }

        .stButton button {
            border-radius: 10px;
            height: 48px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
