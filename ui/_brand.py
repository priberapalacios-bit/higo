import streamlit as st


def apply_branding() -> None:
    """Aplica estilos visuales globales."""
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #F8FAFC;
        }

        h1, h2, h3 {
            color: #0F172A;
            font-weight: 700;
        }

        .stButton button {
            border-radius: 12px;
            height: 48px;
            border: none;
            font-weight: 600;
        }

        .stAlert {
            border-radius: 12px;
        }

        [data-testid="stMetricValue"] {
            font-size: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
