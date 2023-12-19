class Vacancy:
    """
    класс вакансии
    """
    def __init__(self, id_vacancy, title, url, salary_from, salary_to, company, about, requirement):
        self.id = id_vacancy
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.company = company
        self.about = about
        self.requirement = requirement

    def __le__(self, other):
        return self.salary < other.salary

    def __str__(self):
        return f'"Title": {self.title}, "Company": {self.company}, "URL": {self.url}, "salary": {self.salary}, ' \
               f'"about": {self.about}, ' \
               f'"requirement": {self.requirement}'
