print("Сахнюк Костянтин Олександрович \nKM-71")
x = int(input("Введіть кільксть чисел"))
z = []
a = ""
m = 0
for i in range(x):
 print("Введіть", i + 1, "число")
 y = input()
 for n in range(len(z)):
  if float(z[n]) == float(y):
   m = m + 1
 z = z + [y]
print(m)