def remove(num: int):
    s = " "
    flag = False
    if num < 0:
        flag = True
        num *= -1
    while num > 0:
        if num // 10 == 0 and flag is True and (num % 10) % 2 == 0:
            s += str(num)
            s += "-"
            break
        elif (num % 10) % 2 == 0:
            s += str(num % 10)
        num //= 10

    return int(s[::-1])


print(remove(456789))
