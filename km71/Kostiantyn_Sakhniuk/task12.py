print("Сахнюк Костянтин Олександрович \nKM-71")
n = int(input("Введіть перше натуральне число(перша сторона шоколадки)"))
m = int(input("Введіть друге натуральне число(друга сторона шоколадки)"))
k = int(input("Введіть третє натуральне число(кількість клітин)"))
if (n-1)*m > k or n*(m-1) > k:
 print("YES")
elif n == 1 and m > 1:
 if m - 1 >= k:
  print("YES")
 else:
  print("NO")
elif m == 1 and n > 1:
 if n - 1 >= k:
  print("YES")
 else:
  print("NO")
elif n == 1 and m == 1:
 print("Шоколад не може бути розділений")
else:
 print("NO")