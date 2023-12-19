from abc import ABC, abstractmethod

class ApiJob(ABC):

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass
