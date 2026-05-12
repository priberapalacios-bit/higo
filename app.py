import streamlit as st

from config import APP_NAME
from ui._brand import apply_branding
from ui.home import render_home_page
from ui.regulation import render_regulation_page

st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
)

apply_branding()

st.title(APP_NAME)

tab_home, tab_regulation = st.tabs(
    ["Planificador", "Autorregulación"]
)

with tab_home:
    render_home_page()

with tab_regulation:
    render_regulation_page()
