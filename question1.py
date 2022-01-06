number = 4


# QUESTION 1

def rec(num: int):
    calc = 0
    if num == 0:
        return 0
    if num > 0:
        calc += num * 3
    return calc + rec(num - 1)


# QUESTION 2

def sumnum(num: int):
    s = 0
    if num == 0:
        return 0
    if num > 0:
        s += num
    return s + sumnum(num - 1)

print(rec(number))  # QUESTION1--CHECK
print(sumnum(number))  # QUESTION2--CHECK
