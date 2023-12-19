from src.working_with_file import WorkFile
from src.vacancies import Vacancy
import json


class SaveJson(WorkFile):

    def add_vacancy(self, vacancy, file_name):
        """
        Медот для добавления вакансии в файл формата json
        :param vacancy: экземпляр класса вакансия
        :param file_name: название файла-json
        :return:
        """
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
        """
        Метод для отбора вакансий по уровню заработной платы.
        Если введеный уровень ЗП лежит в диапазоне от salary_from до salary_to, то добавляем вакансию в список.
        :param salary: требуемый уровень заработной планы
        :param file_name: название json-файла в котором проводи поиск вакансий
        :return: список отобранных вакансий
        """
        select_vacancies = []
        try:
            from_salary, to_salary = salary.split('-')
        except ValueError:
            from_salary = salary

        with open(file_name+'.json', 'r', encoding='utf-8') as file:
            vacancies = json.load(file)

        for vacancy in vacancies:
            # Проверяем есть ли необходимые ключи
            # и правильно ли заданы границы ЗП
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
        """
        Метод удаления выбранной вакансии
        :param vacancy: выбранная вакансия
        :return:
        """
        with open('vacancies.json', 'r') as file:
            vacancies = json.load(file)
        # Находим по id выбранную вакансию в списке
        for vac in vacancies:
            if vac['ID'] == vacancy.id:
                vacancies.remove(vac)
        #Перезаписываем новый список в фаил
        with open('vacancies.json', 'w') as file:
            json.dump(vacancies, file, indent=2)
