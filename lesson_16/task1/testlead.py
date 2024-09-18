from PY_homework_hillel.lesson_16.task1.developer import Developer
from PY_homework_hillel.lesson_16.task1.manager import Manager

class TeamLead(Manager, Developer):

    __team_size: int

    def __init__(self, name:str, salary:int, department:int, team_size:int):
       super().__init__(name,salary,department)
       self.__team_size = team_size
