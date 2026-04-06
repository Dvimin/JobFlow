from app.db.connection import get_connection


def init_db():
    query = """
    CREATE TABLE IF NOT EXISTS raw_vacancies (
        id SERIAL PRIMARY KEY,
        hh_id VARCHAR(32) UNIQUE NOT NULL,
        search_query TEXT NOT NULL,
        vacancy_json JSONB NOT NULL,
        fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()


if __name__ == "__main__":
    init_db()
    print("Database initialized")
