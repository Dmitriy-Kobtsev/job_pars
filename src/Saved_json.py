from src.working_with_file import WorkFile
import json


class SaveJson(WorkFile):

    def save_to_file(self, ID, Title, Company, URL):
        data = {'ID': ID, 'Title': Title, 'Company': Company, 'URL': URL}

        with open('vacancies.json', 'w') as file:
            json.dump(data, file)

    def get_vacancies_by_salary(self, salary):
        from_salary, to_salary = salary.split('-')
        print(from_salary)
        print(to_salary)
        with open('vacancies.json', 'r') as file:
            vacancies = json.load(file)
        print(vacancies['ID'])

    def del_vacancy(self):
        with open('vacancies.json', 'r') as file:
            vacancies = json.load(file)
