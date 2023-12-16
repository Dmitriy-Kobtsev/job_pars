from src.HeadHunter import HeadHanterAPI
from src.vacancies import Vacancy
from src.Saved_json import SaveJson

if __name__ == '__main__':
    hh = HeadHanterAPI()
    json_saver = SaveJson()
    search_query = input('Введите поисковый запрос: ')
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
        print(vacancy)
        json_saver.add_vacancy(vacancy)


    top_n = int(input('Введите количество вакансий для вывода в топ N: '))