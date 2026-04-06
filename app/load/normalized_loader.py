from app.db.connection import get_connection


def save_normalized_vacancy(vacancy: dict, skills: list):
    query_vacancy = """
    INSERT INTO normalized_vacancies
    (hh_id, search_query, name, employer_name, area_name, salary_from, salary_to,
     salary_currency, published_at, url)
    VALUES (%(hh_id)s, %(search_query)s, %(name)s, %(employer_name)s, %(area_name)s,
            %(salary_from)s, %(salary_to)s, %(salary_currency)s, %(published_at)s, %(url)s)
    ON CONFLICT (hh_id) DO UPDATE SET
        name = EXCLUDED.name,
        employer_name = EXCLUDED.employer_name,
        area_name = EXCLUDED.area_name,
        salary_from = EXCLUDED.salary_from,
        salary_to = EXCLUDED.salary_to,
        salary_currency = EXCLUDED.salary_currency,
        published_at = EXCLUDED.published_at,
        url = EXCLUDED.url;
    """

    query_skill = """
    INSERT INTO vacancy_skills (hh_id, skill)
    VALUES (%s, %s)
    ON CONFLICT (hh_id, skill) DO NOTHING;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query_vacancy, vacancy)
            for skill in skills:
                cur.execute(query_skill, (vacancy["hh_id"], skill))
        conn.commit()
