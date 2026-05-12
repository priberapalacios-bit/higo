# higo
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

/app.py
/runtime.txt
/requirements.txt
/README.md
/services
    state.py
    routes.py
    stress.py
    support.py

/config.py — centraliza constantes, paths y límites del sistema.
/app.py — entry point; registra navegación y carga UI.

/ui/home.py — pantalla principal de planificación de trayectos.
/ui/regulation.py — herramientas de autorregulación y soporte.
/ui/_brand.py — inyección CSS y tokens visuales.

/logic/routes.py — calcula rutas y adapta planes ante incidencias.
/logic/stress.py — calcula carga sensorial de forma determinista.
/logic/validation.py — valida inputs de usuario y estados.

/data/models.py — modelos tipados para rutas y perfiles.
/data/repository.py — persistencia SQLite en /tmp únicamente.
/data/database.py — conexión SQLite resiliente y migraciones.

/external/transport_api.py — wrapper preparado para futuras APIs EMT/Metro.
/external/support.py — genera mensajes de emergencia seguros.

/.streamlit/config.toml — theme base Streamlit.

/requirements.txt — dependencias pineadas.
/runtime.txt — runtime Python soportado por Streamlit Cloud.
