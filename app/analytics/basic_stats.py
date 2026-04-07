from app.db.connection import get_connection


def print_top_skills(limit: int = 10):
    query = """
    SELECT skill, COUNT(*) AS cnt
    FROM vacancy_skills
    GROUP BY skill
    ORDER BY cnt DESC
    LIMIT %s;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (limit,))
            rows = cur.fetchall()

    print("\nTop skills:")
    for skill, cnt in rows:
        print(f"- {skill}: {cnt}")


def print_top_cities(limit: int = 10):
    query = """
    SELECT area_name, COUNT(*) AS cnt
    FROM normalized_vacancies
    GROUP BY area_name
    ORDER BY cnt DESC
    LIMIT %s;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (limit,))
            rows = cur.fetchall()

    print("\nTop cities:")
    for area, cnt in rows:
        print(f"- {area}: {cnt}")


def print_median_salary():
    query = """
    SELECT
      PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary_from) AS median_salary_from
    FROM normalized_vacancies
    WHERE salary_from IS NOT NULL;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            row = cur.fetchone()

    print("\nMedian salary_from:")
    print(row[0])


def main():
    print_top_skills()
    print_top_cities()
    print_median_salary()


if __name__ == "__main__":
    main()
