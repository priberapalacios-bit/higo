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
