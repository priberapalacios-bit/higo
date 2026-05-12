def validate_location_input(value: str) -> None:
    """
    Valida entradas de ubicación.

    Errores:
        ValueError si el texto está vacío.
    """
    if not value.strip():
        raise ValueError(
            "La ubicación no puede estar vacía."
        )
