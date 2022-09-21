"""Database Utils Module"""

def generate_db_uri(user: str, password: str, database: str):
    """ Constructs DB uri From Args

    Args:
        user (str): db connection username
        password (str): db connection password
        database (str): db connection database

    Returns:
        str: constructed db uri
    """
    return f"asyncpg://{user}:{password}@postgres:5432/{database}"
