import random


# 数和
sum1 = 0
# 次数
a = 1

while a <= 10:

    b = int(input(f"请输入第{a}个数字："))
    a = a+1
    sum1 += b

print(f"\n输入的10个数和为：{sum1}")

# 随机数
d = random.randint(50, 150)
print(d)
