from ex2 import Student

student1 = Student('Danil', 24, 80, 195, True, 2, 'white', 140, 4, 'Mathematic', 8)
student2 = Student('Grisha', 24, 80, 175, True, 2, 'black', 140, 4, 'Informatic Techonologies', 9)

print(f'Количество дз Кирилла > Количество дз Андрея : {student1 > student2}')
print(f'Количество дз Кирилла < Количество дз Андрея : {student1 < student2}')
print(f'Количество дз Кирилла == Количество дз Андрея : {student1 == student2}')
print(f'Количество дз Кирилла != Количество дз Андрея : {student1 != student2}')
print(f'Количество дз Кирилла >= Количество дз Андрея : {student1 >= student2}')
print(f'Количество дз Кирилла <=  Количество дз Андрея : {student1 <= student2}')
