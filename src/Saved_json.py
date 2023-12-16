from src.working_with_file import WorkFile
from src.vacancies import Vacancy
import json


class SaveJson(WorkFile):

    def add_vacancy(self, vacancy):
        print(vacancy.title)
        json_data = {
            'ID': vacancy.id,
            'Title': vacancy.title,
            'Company': vacancy.company,
            'URL': vacancy.url,
            'salary': vacancy.salary,
            'about': vacancy.about,
            'requirement': vacancy.requirement
        }
        try:
            with open('vacancies.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                data.append(json_data)
        except FileNotFoundError:
            data = []
            data.append(json_data)
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary):

        try:
            from_salary, to_salary = salary.split('-')
        except ValueError:
            from_salary = salary

        with open('vacancies.json', 'r') as file:
            vacancies = json.load(file)

        for vacancy in vacancies:
            if vacancy['salary'] == from_salary:
                print(vacancy['Title'])
                print(vacancy['URL'])
                print(vacancy['Company'])

    def del_vacancy(self, vacancy):

        with open('vacancies.json', 'r') as file:
            vacancies = json.load(file)
        for vac in vacancies:
            if vac['ID'] == vacancy.id:
                vacancies.remove(vac)

        with open('vacancies.json', 'w') as file:
            json.dump(vacancies, file, indent=2)
