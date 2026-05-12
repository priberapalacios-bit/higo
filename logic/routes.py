from data.models import RouteOption


def build_route_plan(
    origin: str,
    destination: str,
    incident: str,
) -> list[RouteOption]:
    """
    Construye rutas adaptadas al contexto actual.

    Inputs:
        origin: punto de origen.
        destination: punto de destino.
        incident: estado actual del transporte.

    Outputs:
        Lista de rutas disponibles.
    """
    routes = [
        RouteOption(
            name="Ruta tranquila",
            description=(
                f"Camina 5 minutos desde "
                f"{origin} y toma Cercanías hasta {destination}."
            ),
            crowd_density=30,
        ),
        RouteOption(
            name="Ruta alternativa",
            description=(
                f"Usa EMT evitando transbordos hacia {destination}."
            ),
            crowd_density=50,
        ),
    ]

    if incident == "Metro cerrado":
        routes[0].crowd_density += 20

    if incident == "Alta ocupación":
        for route in routes:
            route.crowd_density += 25

    return routes
