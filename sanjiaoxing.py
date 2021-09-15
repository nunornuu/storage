
# 三边
a = int(input('输入第一条边的长度：'))
b = int(input('输入第二条边的长度：'))
c = int(input('输入第三条边的长度：'))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b or a == c or b == c:
        if a == b == c:
            print('等边三角形')
        else:
            print('等腰三角形')
    elif a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2:
        print('直角三角形')
    else:
        print('普通三角形')
else:
    print('不能构成三角形')

A = 56
B = 78
print(f'\nA={A}\nB={B}')
C = abs(A-B)
A = A + C
B = B - C
print(f'A={A}\nB={B}')

