import streamlit as st
from services.state import init_state
from services.routes import get_route_options
from services.stress import estimate_stress
from services.support import emergency_message

st.set_page_config(page_title="RutaCalma Madrid", layout="wide")

init_state()

st.title("🧠 RutaCalma Madrid")
st.caption("Asistente de movilidad urbana para personas con autismo nivel 1")

with st.sidebar:
    st.header("Perfil sensorial")
    noise = st.slider("Sensibilidad al ruido", 1, 10, 7)
    crowd = st.slider("Sensibilidad a aglomeraciones", 1, 10, 8)
    uncertainty = st.slider("Tolerancia a imprevistos", 1, 10, 3)

st.subheader("Planifica tu trayecto")

origin = st.text_input("Origen", "Atocha")
destination = st.text_input("Destino", "Nuevos Ministerios")

incident = st.selectbox(
    "Estado del transporte",
    [
        "Sin incidencias",
        "Metro cerrado",
        "Retraso severo",
        "Alta ocupación",
    ],
)

if st.button("Generar plan seguro"):
    routes = get_route_options(origin, destination, incident)

    for idx, route in enumerate(routes):
        stress_score = estimate_stress(
            route["crowd_level"],
            noise,
            crowd,
            uncertainty,
            incident,
        )

        with st.container(border=True):
            st.markdown(f"### Ruta {idx + 1}: {route['name']}")
            st.write(route["description"])

            st.progress(min(stress_score / 100, 1.0))
            st.metric(
                "Carga sensorial estimada",
                f"{stress_score}/100"
            )

            if stress_score > 70:
                st.warning(
                    "Nivel alto de estrés previsto."
                )
            elif stress_score > 45:
                st.info(
                    "Ruta moderada."
                )
            else:
                st.success(
                    "Ruta estable y predecible."
                )

st.divider()

st.subheader("Autorregulación rápida")

col1, col2 = st.columns(2)

with col1:
    if st.button("Ejercicio de respiración"):
        st.session_state.exercise = True

with col2:
    if st.button("Contactar red de apoyo"):
        st.session_state.support = True

if st.session_state.get("exercise"):
    st.info(
        "Respira 4 segundos · Mantén 4 segundos · Exhala 6 segundos"
    )

if st.session_state.get("support"):
    st.code(
        emergency_message(origin, destination)
    )
