
def find(num: int, digit: int):
    digit = str(digit)
    num = str(num)
    return num.count(digit)


print(find(1231237123, 123))