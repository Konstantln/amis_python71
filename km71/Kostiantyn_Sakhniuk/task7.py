print("Сахнюк Костянтин Олександрович \nKM-71")
x = int(input("Введіть перше ціле число від 1 до 8"))
y = int(input("Введіть друге ціле число від 1 до 8"))
if float(x//2) == float(x/2) and float(y//2) == float(y/2) or float(x//2) != float(x/2) and float(y//2) != float(y/2):
 print("YES")
else:
 print("NO")