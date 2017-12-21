def power(a, n, c):
    if n != 0:
        c = c * a
        n = n - 1
        c = power(a, n, c)
    return c
o = float(input("Введіть дійсне додатнє число"))
n = int(input("Введіть ціле додатнє число"))
c = 1
print(power(o, n, c))
