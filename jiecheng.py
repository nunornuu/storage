a = 20
b = 0
c = 1
# 和
sum1 = 0

while a > 0:
    if b < a:
        # 1 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6  5 4 3 2 1
        c = c * (a - b)
        b = b + 1

    else:
        sum1 += c
        a = a - 1
        b = 0
        c = 1

print(f'\n{sum1}')
