class Student:
    def __init__(self, name, age, average_score):
        self.name = name
        self.age = age
        self.average_score = average_score

    def change_average_score(self, average_score):
        self.average_score = average_score
