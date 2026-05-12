# /app.py

```python
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
            st.metric("Carga sensorial estimada", f"{stress_score}/100")

            if stress_score > 70:
                st.warning(
                    "Nivel alto de estrés previsto. Busca un espacio tranquilo antes de continuar."
                )
            elif stress_score > 45:
                st.info("Ruta moderada. Mantén pausas cortas y revisa tu respiración.")
            else:
                st.success("Ruta estable y predecible.")

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
        "Respira 4 segundos · Mantén 4 segundos · Exhala 6 segundos · Repite 5 veces"
    )

if st.session_state.get("support"):
    st.code(emergency_message(origin, destination))
```

---

# /requirements.txt

```text
streamlit==1.39.0
plotly==5.24.1
pydantic==2.9.2
requests==2.32.3
streamlit-folium==0.23.1
folium==0.17.0
```

---

# /runtime.txt

```text
python-3.11
```

---

# /services/state.py

```python
import streamlit as st


def init_state():
    defaults = {
        "exercise": False,
        "support": False,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
```

---

# /services/routes.py

```python
from typing import List


def get_route_options(origin: str, destination: str, incident: str) -> List[dict]:
    base_routes = [
        {
            "name": "Ruta tranquila",
            "description": f"Camina 5 minutos desde {origin}, toma Cercanías y baja en {destination}.",
            "crowd_level": 30,
        },
        {
            "name": "Ruta alternativa",
            "description": f"Usa autobús EMT y evita el transbordo principal hacia {destination}.",
            "crowd_level": 50,
        },
    ]

    if incident == "Metro cerrado":
        base_routes[0]["crowd_level"] += 20
        base_routes[0]["description"] += " El metro está cerrado. Sigue señalización exterior."

    if incident == "Alta ocupación":
        for route in base_routes:
            route["crowd_level"] += 25

    return base_routes
```

---

# /services/stress.py

```python

def estimate_stress(
    crowd_level: int,
    noise_sensitivity: int,
    crowd_sensitivity: int,
    uncertainty_tolerance: int,
    incident: str,
):
    score = crowd_level

    score += noise_sensitivity * 2
    score += crowd_sensitivity * 3
    score += (10 - uncertainty_tolerance) * 2

    if incident != "Sin incidencias":
        score += 15

    return min(score, 100)
```

---

# /services/support.py

```python

def emergency_message(origin: str, destination: str) -> str:
    return f"""
Hola. Estoy teniendo una sobrecarga durante mi trayecto.

Ubicación aproximada: {origin}
Destino previsto: {destination}

Necesito ayuda para reorganizar el trayecto o un punto seguro.
"""
```

---

# /README.md

```markdown
# RutaCalma Madrid

Asistente de movilidad urbana para personas con autismo nivel 1.

## Features MVP

- Plan B contextual ante incidencias
- Estimación de carga sensorial
- Autorregulación rápida
- Mensaje instantáneo para red de apoyo

## Deploy

1. Subir repo a GitHub
2. Abrir Streamlit Community Cloud
3. Seleccionar repo
4. App file: app.py
5. Deploy
```

---

# ESTRUCTURA FINAL

```text
/app.py
/runtime.txt
/requirements.txt
/README.md
/services
    state.py
    routes.py
    stress.py
    support.py
```
