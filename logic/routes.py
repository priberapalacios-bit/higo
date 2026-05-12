from data.models import RouteOption


def build_route_plan(
    origin: str,
    destination: str,
    incident: str,
) -> list[RouteOption]:
    """
    Construye rutas adaptadas según incidencias.

    Outputs:
        Lista ordenada por estabilidad.
    """
    routes = [
        RouteOption(
            name="Ruta estable",
            description=(
                f"Camina 5 minutos desde {origin}, "
                f"usa Cercanías y baja en {destination}."
            ),
            crowd_density=30,
        ),
        RouteOption(
            name="Ruta alternativa",
            description=(
                f"Toma EMT evitando transbordos hasta {destination}."
            ),
            crowd_density=50,
        ),
    ]

    if incident == "Metro cerrado":
        routes[0].description += (
            " El metro está cerrado; sigue señalización exterior."
        )
        routes[0].crowd_density += 20

    if incident == "Retraso severo":
        routes[1].description += (
            " Hay retrasos prolongados; considera salir antes."
        )
        routes[1].crowd_density += 15

    if incident == "Alta ocupación":
        for route in routes:
            route.crowd_density += 25

    return routes
