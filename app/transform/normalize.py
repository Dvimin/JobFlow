from datetime import datetime


def parse_published_at(value: str):
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        return None


def extract_salary(salary: dict):
    if not salary:
        return None, None, None
    return salary.get("from"), salary.get("to"), salary.get("currency")


def extract_employer_name(item: dict):
    employer = item.get("employer")
    if not employer:
        return None
    return employer.get("name")


def extract_area_name(item: dict):
    area = item.get("area")
    if not area:
        return None
    return area.get("name")


def extract_skills_from_text(text: str):
    if not text:
        return []

    text_lc = text.lower()
    skills = [
        "python", "sql", "postgresql", "fastapi", "django", "flask",
        "airflow", "docker", "kafka", "linux", "pandas", "spark"
    ]

    found = []
    for s in skills:
        if s in text_lc:
            found.append(s)
    return found


def normalize_vacancy(item: dict, search_query: str):
    salary_from, salary_to, currency = extract_salary(item.get("salary"))

    normalized = {
        "hh_id": item.get("id"),
        "search_query": search_query,
        "name": item.get("name"),
        "employer_name": extract_employer_name(item),
        "area_name": extract_area_name(item),
        "salary_from": salary_from,
        "salary_to": salary_to,
        "salary_currency": currency,
        "published_at": parse_published_at(item.get("published_at")),
        "url": item.get("alternate_url"),
    }

    description = (
        item.get("snippet", {}).get("requirement", "")
        + " "
        + item.get("snippet", {}).get("responsibility", "")
    )
    skills = extract_skills_from_text(description)

    return normalized, skills
