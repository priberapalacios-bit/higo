import requests


def check_transport_status() -> dict:
    """
    Wrapper preparado para futuras APIs externas.

    Outputs:
        Estado mock del sistema de transporte.

    Errores:
        RuntimeError si falla la llamada HTTP.
    """
    try:
        return {
            "status": "ok",
            "message": "Sin incidencias",
        }

    except requests.RequestException as error:
        raise RuntimeError(
            f"Error consultando transporte: {error}"
        ) from error
