print("Сахнюк Костянтин Олександрович \nKM-71")
N = int(input("Введіть кількість студентів"))   #Введення кількості студентів
K = int(input("Введіть кількість яблук"))   #Введення кількості яблук
M = int(K/N)   #Розрахунок кількості яблук, які отримає кожен студент
print("Кожен студент отримає яблук:", M ,"\nЗалишиться яблук:", K - M*N)   #Виведення віповіді на екран