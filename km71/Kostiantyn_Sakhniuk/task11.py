print("Сахнюк Костянтин Олександрович \nKM-71")
x1 = int(input("Введіть перше ціле число від 1 до 8"))
y1 = int(input("Введіть друге ціле число від 1 до 8"))
x2 = int(input("Введіть третє ціле число від 1 до 8"))
y2 = int(input("Введіть четверте ціле число від 1 до 8"))
if abs(x1-x2) == 2 and abs(y1-y2) == 1 or abs(x1-x2) == 1 and abs(y1-y2) == 2:
 print("YES")
else:
 print("NO")