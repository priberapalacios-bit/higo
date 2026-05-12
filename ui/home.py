import streamlit as st

from config import (
    DEFAULT_CROWD_SENSITIVITY,
    DEFAULT_NOISE_SENSITIVITY,
    DEFAULT_UNCERTAINTY_TOLERANCE,
    HIGH_STRESS_LIMIT,
    INCIDENT_OPTIONS,
    SAFE_STRESS_LIMIT,
)
from logic.routes import build_route_plan
from logic.stress import calculate_stress_score
from logic.validation import validate_location_input


def render_home_page() -> None:
    """Renderiza la página principal de trayectos."""
    st.subheader("Planifica un trayecto seguro")

    origin = st.text_input("Origen", "Atocha")
    destination = st.text_input(
        "Destino",
        "Nuevos Ministerios",
    )

    incident = st.selectbox(
        "Estado del transporte",
        INCIDENT_OPTIONS,
    )

    with st.sidebar:
        st.header("Perfil sensorial")

        noise_level = st.slider(
            "Sensibilidad al ruido",
            1,
            10,
            DEFAULT_NOISE_SENSITIVITY,
        )

        crowd_level = st.slider(
            "Sensibilidad a aglomeraciones",
            1,
            10,
            DEFAULT_CROWD_SENSITIVITY,
        )

        uncertainty_level = st.slider(
            "Tolerancia a imprevistos",
            1,
            10,
            DEFAULT_UNCERTAINTY_TOLERANCE,
        )

    if st.button("Generar plan"):
        validate_location_input(origin)
        validate_location_input(destination)

        routes = build_route_plan(
            origin=origin,
            destination=destination,
            incident=incident,
        )

        for route in routes:
            stress_score = calculate_stress_score(
                crowd_density=route.crowd_density,
                noise_sensitivity=noise_level,
                crowd_sensitivity=crowd_level,
                uncertainty_tolerance=uncertainty_level,
                incident=incident,
            )

            with st.container(border=True):
                st.markdown(f"### {route.name}")
                st.write(route.description)

                st.metric(
                    "Carga sensorial",
                    f"{stress_score}/100",
                )

                st.progress(stress_score / 100)

                if stress_score >= HIGH_STRESS_LIMIT:
                    st.error(
                        "Carga alta. Busca un espacio tranquilo."
                    )
                elif stress_score >= SAFE_STRESS_LIMIT:
                    st.warning(
                        "Carga moderada. Mantén pausas cortas."
                    )
                else:
                    st.success(
                        "Trayecto estable."
                    )
