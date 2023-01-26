from ex1 import Human


class Student(Human):
    def __init__(self, name, age, weight, height, animal_hair, legs_count, color, intelligence, course, speciality,
                 count_homeworks):
        super().__init__(name, age, weight, height, animal_hair, legs_count, color, intelligence)
        self.course = course
        self.speciality = speciality
        self.count_homeworks = count_homeworks

    def __lt__(self, other):
        a = self.count_homeworks
        b = other.count_homeworks
        return a < b

    def __le__(self, other):
        a = self.count_homeworks
        b = other.count_homeworks
        return a <= b

    def __eq__(self, other):
        a = self.count_homeworks
        b = other.count_homeworks
        return a == b

    def __ne__(self, other):
        a = self.count_homeworks
        b = other.count_homeworks
        return a != b

    def __gt__(self, other):
        a = self.count_homeworks
        b = other.count_homeworks
        return a > b

    def __ge__(self, other):
        a = self.count_homeworks
        b = other.count_homeworks
        return a >= b
