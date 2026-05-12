from data.database import get_connection


def initialize_database() -> None:
    """
    Inicializa tablas SQLite.

    Errores:
        RuntimeError si la migración falla.
    """
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS route_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origin TEXT NOT NULL,
                destination TEXT NOT NULL
            )
            '''
        )

        connection.commit()

    except Exception as error:
        raise RuntimeError(
            f"Error creando tablas: {error}"
        ) from error

    finally:
        connection.close()
