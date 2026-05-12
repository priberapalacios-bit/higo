from dataclasses import dataclass


@dataclass
class RouteOption:
    name: str
    description: str
    crowd_density: int
