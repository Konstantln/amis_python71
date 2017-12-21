def power(a, n):
    c = 1
    if n > 0:
     while n != 0:
         c = c * a
         n = n - 1
     return c
    elif n < 0:
        n = - n
        while n != 0:
            c = c * a
            n = n - 1
        return 1 / c
    else:
        return 1
o = float(input("Введіть дійсне додатнє число"))
n = int(input("Введіть ціле число"))
print(power(o, n))
