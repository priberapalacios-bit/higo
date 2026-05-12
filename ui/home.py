import time

import streamlit as st

from config import (
    DEFAULT_CROWD_SENSITIVITY,
    DEFAULT_NOISE_SENSITIVITY,
    DEFAULT_UNCERTAINTY_TOLERANCE,
    EMPTY_ROUTE_MESSAGE,
    ERROR_INPUT_MESSAGE,
    HIGH_STRESS_LIMIT,
    INCIDENT_OPTIONS,
    SAFE_STRESS_LIMIT,
    SUCCESS_ROUTE_MESSAGE,
)
from data.repository import save_route_log
from logic.routes import build_route_plan
from logic.stress import calculate_stress_score
from logic.validation import validate_location_input


def render_home_page() -> None:
    """Renderiza el flujo principal del trayecto."""
    st.subheader("Planifica un trayecto con menos incertidumbre")

    st.write(
        "RutaCalma transforma incidencias genéricas en instrucciones concretas."
    )

    with st.form("route_form"):
        origin = st.text_input(
            "Origen",
            placeholder="Ejemplo: Atocha",
            help="Usa estaciones o zonas reconocibles.",
        )

        destination = st.text_input(
            "Destino",
            placeholder="Ejemplo: Nuevos Ministerios",
            help="El sistema propondrá alternativas paso a paso.",
        )

        incident = st.selectbox(
            "Situación actual",
            INCIDENT_OPTIONS,
            help="Simula cambios reales del entorno urbano.",
        )

        st.markdown("### Perfil sensorial")

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
            "Tolerancia a cambios inesperados",
            1,
            10,
            DEFAULT_UNCERTAINTY_TOLERANCE,
        )

        submitted = st.form_submit_button(
            "Generar plan alternativo"
        )

    placeholder = st.empty()

    if not submitted:
        placeholder.info(EMPTY_ROUTE_MESSAGE)
        return

    try:
        validate_location_input(origin)
        validate_location_input(destination)

    except ValueError:
        placeholder.error(ERROR_INPUT_MESSAGE)
        return

    with st.spinner("Analizando trayectos y carga sensorial..."):
        time.sleep(1)

        routes = build_route_plan(
            origin=origin,
            destination=destination,
            incident=incident,
        )

    save_route_log(
        origin=origin,
        destination=destination,
    )

    st.success(SUCCESS_ROUTE_MESSAGE)

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
                "Carga sensorial estimada",
                f"{stress_score}/100",
            )

            st.progress(stress_score / 100)

            if stress_score >= HIGH_STRESS_LIMIT:
                st.error(
                    "Esta ruta puede provocar saturación rápida."
                )

            elif stress_score >= SAFE_STRESS_LIMIT:
                st.warning(
                    "La ruta es funcional, pero requiere pausas."
                )

            else:
                st.success(
                    "La ruta prioriza estabilidad y previsibilidad."
                )
