from src.HeadHunter import HeadHanterAPI
from src.vacancies import Vacancy
from src.Saved_json import SaveJson
from src.SuperJob import SuperJobAPI
from src.sj_pars_candidat import pars_candidat_sj
import json


def filter_vacancies(vacancies, filter_words):
    """
    Функция фильтрации списка вакансий по ключевым словам
    :param vacancies: список вакансий
    :param filter_words: список ключевых слов
    :return: список вакансий отобранных по ключевым словам
    """
    data_vacavnies = []
    for vacancy in vacancies:
        for word in filter_words:
            try:
                if word.lower() in vacancy['requirement'].lower() or \
                        word.lower() in vacancy['about'].lower():
                    data_vacavnies.append(vacancy)
            except AttributeError:
                pass
    return data_vacavnies


def sort_vacancies(vacancies):
    """
    Функция сортировки списка вакансий по заработной плате.
    :param vacancies: список вакансий
    :return: отсортированный список вакансий
    """
    return sorted(vacancies, key=lambda x: int(x['salary_from']), reverse=True)


def print_vacansies(vacancies, top_N):
    """
    Функция вывода в консоль списка вакансий
    :param vacancies: список вакансий
    :param top_N: размер списка
    :return:
    """
    if top_N > len(vacancies):
        print('Нашлось вакансий меньше нужного')
        for i in range(len(vacancies)):
            print(f'Company: {vacancies[i]["Company"]}\nURL: {vacancies[i]["URL"]}')
            print(f'salary_from: {vacancies[i]["salary_from"]}\nsalary_to: {vacancies[i]["salary_to"]}')
    else:
        for i in range(top_N):
            print(f'Company: {vacancies[i]["Company"]}\nURL: {vacancies[i]["URL"]}')
            print(f'salary_from: {vacancies[i]["salary_from"]}\nsalary_to: {vacancies[i]["salary_to"]}')


if __name__ == '__main__':
    sj = SuperJobAPI()
    hh = HeadHanterAPI()
    json_saver = SaveJson()
    user_email = input('Введите свой email: ')
    search_query = input('Введите поисковый запрос: ')
    vacancies = sj.get_vacancies(search_query)
    for data in vacancies:
        about, requirements = pars_candidat_sj(data.get('vacancyRichText'))
        vacancy = Vacancy(
            data.get('id'),
            data.get('profession'),
            data.get('link'),
            str(data.get("payment_from")),
            str(data.get("payment_to")),
            data.get('firm_name'),
            about,
            requirements,
        )
        json_saver.add_vacancy(vacancy, "sj_vacancies")

    vacancies = hh.get_vacancies(search_query, user_email)
    for data in vacancies:
        if data.get('salary') == None:
            vacancy_salary_from = '0'
            vacancy_salary_to = '0'
        else:
            if data.get('salary')['from'] == None and data.get('salary')['to'] != None:
                vacancy_salary_from = '0'
                vacancy_salary_to = f"{data.get('salary')['to']}"
            elif data.get('salary')['from'] != None and data.get('salary')['to'] == None:
                vacancy_salary_to = '0'
                vacancy_salary_from = f"{data.get('salary')['from']}"
            else:
                vacancy_salary_from = f"{data.get('salary')['from']}"
                vacancy_salary_to = f"{data.get('salary')['to']}"

        vacancy = Vacancy(
            data.get("id"),
            data.get("name"),
            data.get("alternate_url"),
            vacancy_salary_from,
            vacancy_salary_to,
            data.get("employer", {}).get("name"),
            data.get("snippet", {}).get("responsibility"),
            data.get("snippet", {}).get("requirement")
        )
        json_saver.add_vacancy(vacancy, "hh_vacancies")
    print('Файлы с вакансиями сформирован!')
    with open('hh_vacancies.json', 'r', encoding='utf-8') as file:
        hh_vacancies = json.load(file)
    with open('sj_vacancies.json', 'r', encoding='utf-8') as file:
        sj_vacancies = json.load(file)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    top_n = int(input('Введите количество вакансий для вывода в топ N: '))
    filtered_vacancies_hh = sort_vacancies(filter_vacancies(hh_vacancies, filter_words))
    filtered_vacancies_sj = sort_vacancies(filter_vacancies(sj_vacancies, filter_words))

    sorted_vacancies = sort_vacancies(filtered_vacancies_hh)

    if not filtered_vacancies_hh:
        print('На HeadHunter нет вакансий, соответствующих заданным критериям.')
    else:
        print(f'По ключевым словам нашлось {len(filtered_vacancies_hh)} из {top_n} вакансий на HeadHunter:')
        print_vacansies(filtered_vacancies_hh, top_n)


    if not filtered_vacancies_sj:
        print('На SuperJob нет вакансий, соответствующих заданным критериям.')
    else:
        print(f'По ключевым словам нашлось {len(filtered_vacancies_sj)} из {top_n} вакансии на SuperJob:')
        print_vacansies(filtered_vacancies_sj, top_n)


    my_salary = input('Введите ожидаемую зарплату: ')

    select_vacancies_hh = json_saver.get_vacancies_by_salary(my_salary, 'hh_vacancies')

    select_vacancies_sj = json_saver.get_vacancies_by_salary(my_salary, 'sj_vacancies')
    print('Вакансии на HeadHunter с заданной ЗП: ')
    print_vacansies(sort_vacancies(select_vacancies_hh), top_n)
    print('Вакансии на SuperJob с заданной ЗП: ')
    print_vacansies(sort_vacancies(select_vacancies_sj), top_n)