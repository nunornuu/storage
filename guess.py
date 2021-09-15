import random


a = random.randint(0, 80)
# 计数器
counter = 1
print(a)
while True:
    b = int(input('请输入你的答案：'))
    if b == a:
        print('恭喜你答对了')
        break
    else:
        if a > b:
            print('猜的数太小了')
            counter += 1
        elif b > a:
            print('猜的数太大了')
            counter += 1

print(f'共用{counter}次猜中')
