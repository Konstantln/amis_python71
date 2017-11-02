print("Сахнюк Костянтин Олександрович \nKM-71")
x = int(input("Введіть перше ціле число"))
y = int(input("Введіть друге ціле число"))
z = int(input("Введіть третє ціле число"))
if x == y == z:
 print(3)
elif x == y and x != z or x == z and x != y or y == z and y != x:
 print(2)
else:
 print(0)