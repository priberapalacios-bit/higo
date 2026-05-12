def validate_location_input(value: str) -> None:
    """
    Valida ubicaciones ingresadas por el usuario.

    Errores:
        ValueError si el texto es inválido.
    """
    cleaned_value = value.strip()

    if not cleaned_value:
        raise ValueError(
            "La ubicación no puede estar vacía."
        )

    if len(cleaned_value) < 3:
        raise ValueError(
            "La ubicación necesita más detalle."
        )
