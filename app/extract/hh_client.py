import requests


HH_API_URL = "https://api.hh.ru/vacancies"


def fetch_vacancies(text: str, page: int = 0, per_page: int = 20):
    params = {
        "text": text,
        "page": page,
        "per_page": per_page,
    }
    response = requests.get(HH_API_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()