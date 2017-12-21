sp = input("Введіть послідовність чисел через пробіл")
k = -1
i = 0
lh = ""
ch = ""
big = ""
pr = ""
biggest = ""
def func(sp, ch, lh, i, k, pr, big, biggest):
    ch = ""
    if sp[i] != " " and i > k:
        k = i
        while sp[k] != " ":
            ch += sp[k]
            k += 1
            if k == len(sp):
                break
        if big == "":
            big += ch
            lh = ch
        elif ch == lh:
            big += ch
        elif ch != lh and len(big) > len(biggest):
            biggest = big
            big = ch
            lh = ch
        elif ch != lh:
            big = ch
            lh = ch
    i += 1
    if i == len(sp) and len(big) > len(biggest):
        biggest = big
        return biggest
    elif i == len(sp):
        return biggest
    biggest = func(sp, ch, lh, i, k, pr, big, biggest)
    return biggest
print("Відповідь", len(func(sp, ch, lh, i, k, pr, big, biggest)),"- група", (func(sp, ch, lh, i, k, pr, big, biggest)[0] + " ") * len(func(sp, ch, lh, i, k, pr, big, biggest)))
