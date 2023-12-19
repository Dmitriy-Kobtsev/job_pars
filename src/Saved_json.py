from src.working_with_file import WorkFile
from src.vacancies import Vacancy
import json


class SaveJson(WorkFile):

    def add_vacancy(self, vacancy, file_name):
        json_data = {
            'ID': vacancy.id,
            'Title': vacancy.title,
            'Company': vacancy.company,
            'URL': vacancy.url,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'about': vacancy.about,
            'requirement': vacancy.requirement
        }
        try:
            with open(file_name+'.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                data.append(json_data)
        except FileNotFoundError:
            data = []
            data.append(json_data)
        with open(file_name+'.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary, file_name):
        select_vacancies = []
        try:
            from_salary, to_salary = salary.split('-')
        except ValueError:
            from_salary = salary

        with open(file_name+'.json', 'r', encoding='utf-8') as file:
            vacancies = json.load(file)

        for vacancy in vacancies:
            try:
                from_salary_in_vacancy = vacancy['salary_from']
                to_salary_in_vacancy = vacancy['salary_to']
                if int(to_salary_in_vacancy) != 0:
                    if int(from_salary) >= int(from_salary_in_vacancy) and int(from_salary) <= int(to_salary_in_vacancy):
                        select_vacancies.append(vacancy)
                elif int(from_salary) >= int(from_salary_in_vacancy):
                    select_vacancies.append(vacancy)
            except AttributeError:
                pass
            except ValueError:
                pass
        return select_vacancies

    def del_vacancy(self, vacancy):

        with open('vacancies.json', 'r') as file:
            vacancies = json.load(file)
        for vac in vacancies:
            if vac['ID'] == vacancy.id:
                vacancies.remove(vac)

        with open('vacancies.json', 'w') as file:
            json.dump(vacancies, file, indent=2)
