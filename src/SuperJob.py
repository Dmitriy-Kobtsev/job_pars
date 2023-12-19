from src.API_job_site import ApiJob
import requests
import os

class SuperJobAPI(ApiJob):
    """
    Класс для создания вакансий с сайта SuperJob
    """
    api_key = os.getenv('SJ_key')
    url = 'https://api.superjob.ru/2.0/vacancies'

    def get_vacancies(self, keyword):
        params = {
            "keyword": keyword,
        }

        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': SuperJobAPI.api_key,
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.get(SuperJobAPI.url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("objects", [])
            return vacancies
        else:
            print(f"Request failed with status code: {response.status_code}")
