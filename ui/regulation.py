import time

import streamlit as st

from external.support import build_support_message


def render_regulation_page() -> None:
    """Renderiza herramientas de regulación y soporte."""
    st.subheader("Herramientas de regulación rápida")

    st.write(
        "Estas acciones ayudan a recuperar control antes de una sobrecarga."
    )

    breathing_placeholder = st.empty()

    if st.button("Iniciar respiración guiada"):
        with st.spinner("Preparando ejercicio..."):
            time.sleep(1)

        breathing_placeholder.success(
            "Respira 4 segundos · Mantén 4 segundos · Exhala 6 segundos"
        )

    st.divider()

    st.markdown("### Red de apoyo")

    origin = st.text_input(
        "Ubicación actual",
        placeholder="Ejemplo: Sol",
    )

    destination = st.text_input(
        "Destino previsto",
        placeholder="Ejemplo: Chamartín",
    )

    if st.button("Generar mensaje"):
        if not origin or not destination:
            st.error(
                "Completa ubicación actual y destino previsto."
            )
            return

        with st.spinner("Preparando mensaje claro y directo..."):
            time.sleep(1)

            message = build_support_message(
                origin=origin,
                destination=destination,
            )

        st.success(
            "Mensaje listo para compartir con tu red de apoyo."
        )

        st.code(message)
