from src.API_job_site import ApiJob
import requests

class SuperJobAPI(ApiJob):
    Secret_key = 'v3.r.138036067.f7c4da8bc375450771803361c02af039635d085d.792e602f97376dc27b111bcc0ce5dae57e732092'
    url = 'https://api.superjob.ru/2.0/vacancies'

    def get_vacancies(self, keyword):
        params = {
            "keyword": keyword,
        }

        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': SuperJobAPI.Secret_key,
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
