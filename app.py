import streamlit as st

from config import APP_NAME
from ui._brand import inject_brand
from ui.home import render_home_page
from ui.regulation import render_regulation_page

st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
)

inject_brand()

st.title("RutaCalma Madrid")

st.caption(
    "Movilidad urbana diseñada para reducir incertidumbre y carga sensorial."
)

tab_home, tab_regulation = st.tabs(
    [
        "Planificador de trayectos",
        "Autorregulación",
    ]
)

with tab_home:
    render_home_page()

with tab_regulation:
    render_regulation_page()
    
