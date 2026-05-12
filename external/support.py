def build_support_message(
    origin: str,
    destination: str,
) -> str:
    """
    Construye mensaje para red de apoyo.

    Outputs:
        Texto listo para copiar.
    """
    return (
        "Estoy teniendo una sobrecarga durante el trayecto.\n\n"
        f"Ubicación actual: {origin}\n"
        f"Destino previsto: {destination}\n\n"
        "Necesito ayuda para reorganizar el trayecto."
    )
