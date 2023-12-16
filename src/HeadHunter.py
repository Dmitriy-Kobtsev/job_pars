from src.API_job_site import ApiJob
import requests

class HeadHanterAPI(ApiJob):
    url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):
        params = {
            "text": keyword,
            "area": 1,  # Specify the desired area ID (1 is Moscow)
            "per_page": 2,  # Number of vacancies per page
        }
        headers = {
            "User-Agent": "kdm007@mail.ru",
        }

        response = requests.get(self.url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(data)
            print('____')
            vacancies = data.get("items", [])
            for vacancy in vacancies:
                print(vacancy)
                self.vacancy_id = vacancy.get("id")
                self.vacancy_title = vacancy.get("name")

                self.vacancy_url = vacancy.get("alternate_url")
                self.company_name = vacancy.get("employer", {}).get("name")
                if vacancy.get('salary') == None :
                    self.vacancy_salary = None
                else:
                    self.vacancy_salary = f"{vacancy.get('salary')['from']}-{vacancy.get('salary')['to']}"
                #print(f"ID: {self.vacancy_id}\nTitle: {self.vacancy_title}\nCompany: {self.company_name}\nURL: {self.vacancy_url}\n")
                print('salary: ', self.vacancy_salary)
        else:
            print(f"Request failed with status code: {response.status_code}")