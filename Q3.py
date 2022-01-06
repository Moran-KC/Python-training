def digitindex(num: int, s: str):
    for i in range(len(s)):
        if i == num:
            print(s[i])
            break


digitindex(2, "abcdefg")

