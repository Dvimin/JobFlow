from psycopg2.extras import Json

from app.db.connection import get_connection


def save_raw_vacancy(hh_id: str, search_query: str, vacancy_json: dict):
    query = """
    INSERT INTO raw_vacancies (hh_id, search_query, vacancy_json)
    VALUES (%s, %s, %s)
    ON CONFLICT (hh_id) DO NOTHING;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (hh_id, search_query, Json(vacancy_json)))
        conn.commit()
