import sqlite3

from config import DATABASE_PATH


def get_connection() -> sqlite3.Connection:
    """
    Crea conexión SQLite resiliente.

    Errores:
        RuntimeError si la conexión falla.
    """
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        return connection
    except sqlite3.Error as error:
        raise RuntimeError(
            f"Error conectando SQLite: {error}"
        ) from error
