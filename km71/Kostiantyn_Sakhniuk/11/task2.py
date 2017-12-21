def func(s, i, smallest):
    if i < len(s) and s[i] <= smallest:
        smallest = s[i]
    if i < len(s):
        i += 1
        smallest = func(s, i, smallest)
    return smallest


a = int(input("Кількість елементів"))
s = [int(input("Введіть елемент списку")) for i in range(a)]
i = 0
print(func(s, i, s[0]))