def pascal(n):
    lis = [1]
    for i in range(n):
        for j in range(0, int(n - i)):
            print('  ', end='')
        print(lis, end='')
        print()
        print(' ', end='')
        n_lis = lis + [1]
        for col in range(0, len(lis) - 1):
            n_lis[col + 1] = lis[col] + lis[col + 1]
        lis = n_lis


pascal(6)