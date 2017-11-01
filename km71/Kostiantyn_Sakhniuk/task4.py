print("Сахнюк Костянтин Олександрович \nKM-71")
year = int(input("Введіть рік"))
if float(year//4) == float(year/4) and float(year//100) != float(year/100):
 print("LEAP")
elif float(year//400) == float(year/400):
 print("LEAP")
else:
 print("COMMON")