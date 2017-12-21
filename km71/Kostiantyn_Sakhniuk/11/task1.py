def InputN():
    n = input("n")
    if  not n. isdigit():
        return InputN()
    if int(n) <= 1:
        return InputN()
    return int(n)


def InputX(n):
    x = input("x")
    if  not x. isdigit():
        return InputX(n)
    if float(x) == float(n):
        return InputX(n)
    return float(x)


def Summ(x, n):
    a = 0
    for i in range(1, n + 1):
        a = (x ** i + n) / (x - n) + a
    return  a


def Check():
    assert (Summ(2, 1) == 3)
    assert (Summ(4, 2) == 12)
    print("Вірно")
n = InputN()
x = InputX(n)
print(Summ(x, n))
