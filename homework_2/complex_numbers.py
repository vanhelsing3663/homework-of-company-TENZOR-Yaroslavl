import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")

a = complex(input("Введите коэффициент a = "))
b = complex(input("Введите коэффициент b = "))
c = complex(input("Введите коэффициент c =  "))

discr = b ** 2 - 4 * a * c
print(f"Дискриминант D = {discr}") # На комплексной оси всегда есть корни

x1 = (-b + (discr ** 0.5)) / (2 * a)
x2 = (-b - (discr ** 0.5)) / (2 * a)
print(f"x1 = ({round(x1.real, 10)}, {round(x1.imag, 10)}) \nx2 = ({round(x2.real, 10)}, {round(x2.imag, 10)})")
