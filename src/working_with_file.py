from abc import ABC, abstractmethod

class WorkFile(ABC):

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def del_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, *args, **kwargs):
        pass