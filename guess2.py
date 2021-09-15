import random


a = random.randint(0, 80)
# 次数限制
x = 3
print(a)
while x > 0:
    b = int(input('请输入你的答案：'))
    if b == a:
        print('恭喜你答对了')
        break
    else:
        if a > b:
            print('猜的数太小了')
            x -= 1
        elif b > a:
            print('猜的数太大了')
            x -= 1
    if x == 0:
        print('你没机会了-·-')
