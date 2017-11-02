print("Сахнюк Костянтин Олександрович \nKM-71")
N = int(input("Введіть кільксть кеглів"))
Ni = ""
for i in range(1, N +1):
 Ni = str(Ni) + "I"
K = int(input("Введіть кількість кинутих куль"))
for i in range(1 ,K + 1):
 print("Введіть першу кеглю, яку збила", i, "куля(від 1 до", N ,")")
 li = int(input())
 print("Введіть останню кеглю, яку збила", i, "куля(від", li,"до", N ,")")
 ri = int(input())
 for n in range(li , ri + 1):
  Ni = Ni[:n - 1] + "." + Ni[n:]
print(Ni)