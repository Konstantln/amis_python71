print("Сахнюк Костянтин Олександрович \nKM-71")
x = int(input("Введіть кільксть елементів в списку"))
z = []
a = ""
delete = []
for i in range(x):
 print("Введіть", i + 1, "елемент")
 y = input()
 for n in range(len(z)):
  if str(z[n]) == str(y):
   z = z[:n] + z[n + 1:]
   delete = delete + [y]
   break
 z = z + [y]
 for n in range(len(delete)):
  if y == delete[n]:
   z = z[:-1]
for i in range(len(z)):
 if a != "":
  a = a + " " + str(z[i])
 else:
  a = a + str(z[i])
print(a)
