print("Сахнюк Костянтин Олександрович \nKM-71")
x = int(input("Введіть перше ціле число"))
y = int(input("Введіть друге ціле число"))
z = int(input("Введіть третє ціле число"))
if x < y and x < z:
 print(x)
elif y < x and y < z:
 print(y)
elif z < x and z < y:
 print(z)
else:
 print("Числа однакові")