from abc import ABC, abstractmethod

class WorkFile(ABC):

    @abstractmethod
    def save_to_file(self, *args, **kwargs):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass