def func(s, i, k):
    k += [s[-(i+1)]]
    i += 1
    if len(k) == len(s):
        return k
    k = func(s, i, k)
    return k


a = int(input("Кількість елементів"))
s = [int(input("Введіть елемент списку")) for i in range(a)]
i = 0
k = []
print(func(s, i, k))