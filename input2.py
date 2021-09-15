# 数和
sum1 = 0
# 循环次数
a = 1
# 最大数
maxS = 0


while a <= 10:

    b = int(input(f"请输入第{a}个数字："))
    a = a+1
    if b > maxS:
        maxS = b

    sum1 += b

print(f"\n输入的10个数和为：{sum1}")
print(f"输入的10个数最大值：{maxS}")
print(f'平均值{sum1/10}')
