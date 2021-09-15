print('\t  *  \t')
print('\t * * \t')
print('\t* * *\t')
print('   * * * *   ')
print('  * * * * *  ')
print(' * * * * * * ')
print('* * * * * * *\n')
# 13
# 6+6
# 5+5
# 4+4
# 3+3

a = 1
bb = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while a < 10:
    for b in bb:
        if b > a:
            print('.........\t', end='')
        else:
            print(f'{b} * {a} = {a*b}\t', end='')
    print('\n')
    a = a + 1

