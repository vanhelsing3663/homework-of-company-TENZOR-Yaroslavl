class Animals:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class Mammals(Animals):
    def __init__(self,  name, age, weight, height, animal_hair, number_of_paws, color):
        super().__init__(name, age, weight, height)
        self.animal_hair = animal_hair
        self.number_of_paws = number_of_paws
        self.color = color


class Human(Mammals):
    def __init__(self, name, age, weight, height, hair, number_of_paws, color, intelligence):
        super().__init__(name, age, weight, height, hair, number_of_paws, color)
        self.intelligence = intelligence

    def say(self):
        print(f'Hello,my friend my name is {self.name}.I am human.')


class Cat(Mammals):
    def __init__(self, name, age, weight, height, animal_hair, number_of_paws, color):
        super().__init__(name, age, weight, height, animal_hair, number_of_paws, color)

    def say(self):
        print('Mяy-Mяy-Mяy-Mяy')


class Dog(Mammals):
    def __init__(self, name, age, weight, height, animal_hair, number_of_paws, color):
        super().__init__(name, age, weight, height, animal_hair, number_of_paws, color)

    def say(self):
        print('ГАВ-ГАВ-ГАВ-ГАВ-ГАВ-ГАВ-ГАВ-ГАВ-ГАВ')


Kirill = Human('Kirill', 28, 80, 195, True, 2, 'black', 195)
Kit = Cat('Cat', 3, 15, 40, True, 4, 'brown-white')
Dogy = Dog('Dog', 8, 30, 50, False, 4, 'brown')

for mammals in (Kirill, Kit, Dogy):
    mammals.say()
