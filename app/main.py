from app.extract.hh_client import fetch_vacancies
from app.load.raw_loader import save_raw_vacancy
from app.transform.normalize import normalize_vacancy
from app.load.normalized_loader import save_normalized_vacancy


def main():
    search_query = "Python Developer"
    data = fetch_vacancies(search_query)

    for item in data.get("items", []):
        save_raw_vacancy(
            hh_id=item["id"],
            search_query=search_query,
            vacancy_json=item,
        )
        
        normalized, skills = normalize_vacancy(item, search_query)
        save_normalized_vacancy(normalized, skills)

    print(f"Saved {len(data.get('items', []))} vacancies")


if __name__ == "__main__":
    main()
