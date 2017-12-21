def distance(x1, y1, x2, y2):
    c = ((y1-y2)**2 + (x1 - x2)**2)**(1/2)
    return c
x1 = float(input("Введіть перше дійсне число"))
y1 = float(input("Введіть друге дійсне число"))
x2 = float(input("Введіть третє дійсне число"))
y2 = float(input("Введіть четверте дійсне число"))
print(distance(x1, y1, x2, y2))
