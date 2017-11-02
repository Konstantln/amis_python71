print("Сахнюк Костянтин Олександрович \nKM-71")
z = ""
m = 0
for i in range(8):
 if m == 1:
  break
 print("Введіть координату по горизонталі для", i + 1, "-го ферзя(число від 1 до 8, не вводіть однакові кординати)")
 x = input()
 print("Введіть координату по вертикалі для", i + 1, "-го ферзя(число від 1 до 8, не вводіть однакові кординати)")
 y = input()
 z = str(z) + str(x) + str(y)
for i in range(len(z) - 1):
 l = 0
 if m == 1:
  break
 if float(i // 2) == float(i / 2):
  for n in range(len(z[:i])):
   if m == 1:
    break
   l = l + 1
   if float(n // 2) == float(n / 2):
    f1 = abs(int(z[i]) - int(int(z[n])))
    f2 = abs(int(z[i + 1]) - int(z[n + 1]))
   else:
     f1 = abs(int(z[i]) - int(z[n - 1]))
     f2 = abs(int(z[i + 1]) - int(z[n]))
   if f1 == f2 or f1 == 0 or f2 == 0:
    m = 1
    print("YES")
    break
  for n in range(l + 2, len(z)):
   if float(n // 2) == float(n / 2):
    f1 = abs(int(z[i]) - int(int(z[n])))
    f2 = abs(int(z[i + 1]) - int(z[n + 1]))
   else:
    f1 = abs(int(z[i]) - int(z[n - 1]))
    f2 = abs(int(z[i + 1]) - int(z[n]))
   if f1 == f2 or f1 == 0 or f2 == 0:
    m = 1
    print("YES")
    break
if m == 0:
 print("NO")










