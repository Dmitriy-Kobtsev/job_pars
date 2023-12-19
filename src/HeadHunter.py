from src.API_job_site import ApiJob
import requests

class HeadHanterAPI(ApiJob):

    url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword, email):
        params = {
            "text": keyword,
            "area": 113,  # Specify the desired area ID (1 is Moscow)
        }
        headers = {
            "User-Agent": email,
        }

        response = requests.get(HeadHanterAPI.url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items", [])
            return vacancies
        else:
            print(f"Request failed with status code: {response.status_code}")