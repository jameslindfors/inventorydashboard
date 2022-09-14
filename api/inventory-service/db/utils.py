def generate_db_uri(user: str, password: str, db: str):
    # "asyncpg://postgres:password@postgres:5432/dev"
    return f"asyncpg://{user}:{password}@postgres:5432/{db}"