import streamlit as st

from external.support import build_support_message


def render_regulation_page() -> None:
    """Renderiza herramientas de regulación emocional."""
    st.subheader("Autorregulación rápida")

    if st.button("Ejercicio de respiración"):
        st.info(
            "Respira 4 segundos · Mantén 4 segundos · Exhala 6 segundos"
        )

    origin = st.text_input(
        "Ubicación actual",
        "Atocha",
        key="support_origin",
    )

    destination = st.text_input(
        "Destino previsto",
        "Nuevos Ministerios",
        key="support_destination",
    )

    if st.button("Generar mensaje de apoyo"):
        message = build_support_message(
            origin=origin,
            destination=destination,
        )

        st.code(message)
