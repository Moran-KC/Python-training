# QUESTION 1
def summary(num: int):
    sum1 = 0
    flag = False
    if num < 0:
        flag = True
        num *= -1
    while num != 0:
        if num // 10 == 0 and flag is True:
            num *= -1
            sum1 += num
            break
        sum1 += num % 10
        num = num // 10
    return sum1


print(summary(12345))
print(summary(0))
print(summary(1))
print(summary(-1735))
