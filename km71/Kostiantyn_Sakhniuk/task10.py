print("Сахнюк Костянтин Олександрович \nKM-71")
x1 = int(input("Введіть перше ціле число від 1 до 8"))
y1 = int(input("Введіть друге ціле число від 1 до 8"))
x2 = int(input("Введіть третє ціле число від 1 до 8"))
y2 = int(input("Введіть четверте ціле число від 1 до 8"))
if x1 == x2 and x1 != y2 or y1 == y2 and y1 != x2:
 print("YES")
elif abs(x1-x2) == abs(y1-y2) != 0:
 print("YES")
else:
 print("NO")