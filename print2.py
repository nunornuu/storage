a = 9
bb = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while a > 0:
    for b in bb:
        if b > a:
            print('.........\t', end='')
        else:
            print(f'{b} * {a} = {a*b}\t', end='')
    print('\n')
    a = a - 1
