from abc import ABC

class Employee(ABC):

    __name: str
    __salary: int

    def __init__(self, name:str, salary:int):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary
