sp = input("Введіть послідовність чисел через пробіл")
k = -1
i = 0
lh = ""
ch = ""
pr = ""
def func(sp, ch, lh, i, k, pr):
    ch = ""
    if sp[i] != " " and i > k:
        k = i
        while sp[k] != " ":
            ch += sp[k]
            k += 1
            if k == len(sp):
                break
        if lh == "":
            lh = float(ch)
            pr = 1
        elif float(ch) > lh:
            pr = 1
            lh = float(ch)
        elif float(ch) == lh:
            pr += 1
    i += 1
    if i == len(sp):
        return pr
    pr = func(sp, ch, lh, i, k, pr)
    return pr
print(func(sp, ch, lh, i, k, pr))
