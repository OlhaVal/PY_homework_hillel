from PY_homework_hillel.lesson_16.task1.employee import Employee


class Manager(Employee):

    __department: str
    
    def __init__(self, name:str, salary:int, department:int):
       super().__init__(name,salary)
       self.__department = department
