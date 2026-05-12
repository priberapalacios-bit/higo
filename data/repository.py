from data.database import get_connection


def save_route_log(
    origin: str,
    destination: str,
) -> None:
    """
    Guarda trayectos generados para métricas demo.

    Errores:
        RuntimeError si SQLite falla.
    """
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS route_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origin TEXT NOT NULL,
                destination TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO route_logs (
                origin,
                destination
            )
            VALUES (?, ?)
            """,
            (origin, destination),
        )

        connection.commit()

    except Exception as error:
        raise RuntimeError(
            f"Error guardando trayecto: {error}"
        ) from error

    finally:
        connection.close()
