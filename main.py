from src.HeadHunter import HeadHanterAPI
from src.vacancies import Vacancy
from src.Saved_json import SaveJson
from src.SuperJob import SuperJobAPI
import json


def filter_vacancies(hh_vacancies, filter_words):
    data_vacavnies = []
    for hh_vacancy in hh_vacancies:
        for word in filter_words:
            try:
                if word.lower() in hh_vacancy['requirement'].lower().split() or \
                        word in hh_vacancy['about'].lower().split():
                    data_vacavnies.append(hh_vacancy)
            except AttributeError:
                pass
    return data_vacavnies


if __name__ == '__main__':
    sj = SuperJobAPI()

    hh = HeadHanterAPI()
    json_saver = SaveJson()
    search_query = input('Введите поисковый запрос: ')
    vacancies = sj.get_vacancies(search_query)
    for data in vacancies:
        print(data)
        vacancy = Vacancy(
            data.get('id'),
            data.get('profession'),
            data.get('link'),
            f'{data.get("payment_from")}-{data.get("payment_to")}',
            data.get('firm_name'),
            data.get('vacancyRichText'),
            data.get('candidat'),
        )
        json_saver.add_vacancy(vacancy, "sj_vacancies")

    N_need_vacancies = int(input('Введите необходимое количество вакансий: '))
    vacancies = hh.get_vacancies(search_query, N_need_vacancies)
    for data in vacancies:
        if data.get('salary') == None:
            vacancy_salary = None
        else:
            vacancy_salary = f"{data.get('salary')['from']}-{data.get('salary')['to']}"

        vacancy = Vacancy(
            data.get("id"),
            data.get("name"),
            data.get("alternate_url"),
            vacancy_salary,
            data.get("employer", {}).get("name"),
            data.get("snippet", {}).get("responsibility"),
            data.get("snippet", {}).get("requirement")
        )
        json_saver.add_vacancy(vacancy, "hh_vacancies")
    print('Файлы с вакансиями сформирован!')
    with open('hh_vacancies.json', 'r', encoding='utf-8') as file:
        hh_vacancies = json.load(file)
    print(type(hh_vacancies))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    top_n = int(input('Введите количество вакансий для вывода в топ N: '))
    filtered_vacancies = filter_vacancies(hh_vacancies, filter_words)
    if not filtered_vacancies:
        print('Нет вакансий, соответствующих заданным критериям.')
    else:
        for i in range(top_n):
            print(f'Company: {filtered_vacancies[i]["Company"]}\nURL: {filtered_vacancies[i]["URL"]}')

    my_salary = input('Введите ожидаемую зарплату: ')

    json_saver.get_vacancies_by_salary(my_salary, 'hh_vacancies')