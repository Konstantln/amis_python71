print("Сахнюк Костянтин Олександрович \nKM-71")
students = input("Введіть кількість учнів(Не включаючи Петю)")
allhight = []
for i in range(int(students)):
 print("Введіть зріст", i + 1, "-го учня(Натуральні числа від 100 до 200)")
 hight = int(input())
 if allhight == []:
  allhight = [hight]
 else:
  for n in range(len(allhight)):
   if int(hight) >= int(allhight[n]) and  int(hight) <= int(allhight[n - 1]):
    allhight = allhight[:n] + [hight] + allhight[n:]
    break
   elif n == len(allhight) - 1:
    allhight = allhight + [hight]
    break
   elif int(hight) >= int(allhight[0]):
    allhight = [hight] + allhight
    break
X = int(input("Введіть зрст Петі"))
for i in range(len(allhight)):
 if int(allhight[-(i + 1)]) >= X:
  m = len(allhight[:-i]) + 1
  if -i == 0:
   m = len(allhight) + 1
   break
  break
 elif X > allhight[0]:
  m = 1
  break
print("Номер Петі ", m)
