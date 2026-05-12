import streamlit as st


def inject_brand() -> None:
    """Inyecta sistema visual global."""
    st.markdown(
        """
        <style>

        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=Inter:wght@400;500;600&family=Manrope:wght@600;700;800&display=swap');

        :root {

            --color-primary: #528DAB;
            --color-secondary: #CFE9F9;
            --color-accent: #87C39A;
            --color-bg: #F7FAFC;
            --color-surface: #FFFFFF;
            --color-text: #040F2D;

            --spacing-1: 4px;
            --spacing-2: 8px;
            --spacing-3: 12px;
            --spacing-4: 16px;
            --spacing-5: 24px;
            --spacing-6: 32px;
            --spacing-7: 48px;

            --radius-sm: 4px;
            --radius-md: 8px;
            --radius-lg: 16px;

            --shadow-sm:
                0 1px 2px rgba(4, 15, 45, 0.06);

            --shadow-md:
                0 6px 18px rgba(4, 15, 45, 0.08);

            --shadow-lg:
                0 12px 32px rgba(4, 15, 45, 0.12);
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: var(--color-text);
            background: var(--color-bg);
        }

        .stApp {
            background-color: var(--color-bg);
        }

        h1, h2, h3, h4 {
            font-family: 'Manrope', sans-serif;
            color: var(--color-text);
            letter-spacing: -0.02em;
            line-height: 1.1;
        }

        h1 {
            font-size: 3rem;
            font-weight: 800;
        }

        h2 {
            font-size: 2rem;
            font-weight: 700;
        }

        p, label, span {
            font-size: 1rem;
            line-height: 1.6;
        }

        section[data-testid="stSidebar"] {
            background: #EEF5FA;
            border-right: 1px solid rgba(82, 141, 171, 0.08);
        }

        .stButton button {

            background: var(--color-primary);
            color: white;

            border: none;
            border-radius: var(--radius-lg);

            padding:
                0.75rem
                1.25rem;

            font-weight: 600;

            box-shadow: var(--shadow-sm);

            transition:
                transform 120ms ease,
                box-shadow 120ms ease,
                background 120ms ease;
        }

        .stButton button:hover {

            background: #447992;

            transform: translateY(-1px);

            box-shadow: var(--shadow-md);
        }

        .stTextInput input,
        .stSelectbox div[data-baseweb="select"],
        .stTextArea textarea {

            background: var(--color-surface);

            border:
                1px solid
                rgba(82, 141, 171, 0.18);

            border-radius: var(--radius-lg);

            padding: 0.75rem;

            box-shadow: none;
        }

        .stTextInput input:focus,
        .stTextArea textarea:focus {

            border-color: var(--color-primary);

            box-shadow:
                0 0 0 3px rgba(82, 141, 171, 0.12);
        }

        .stForm {

            background: var(--color-surface);

            padding: 2rem;

            border-radius: var(--radius-lg);

            border:
                1px solid
                rgba(82, 141, 171, 0.08);

            box-shadow: var(--shadow-md);
        }

        div[data-testid="stMetric"] {

            background: var(--color-surface);

            border-radius: var(--radius-lg);

            padding: 1rem;

            box-shadow: var(--shadow-sm);
        }

        .stAlert {

            border-radius: var(--radius-lg);

            border: none;

            box-shadow: var(--shadow-sm);
        }

        code {
            font-family: 'IBM Plex Mono', monospace;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
