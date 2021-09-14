
# 相乘函数
def fun2(x, y):
    x = float(x)
    y = int(y)
    return round(x*y, 3)


# 总销售额计算
total = 0
# 销售数量和
day = 0
# 平均每日销售数量
meiDay = 0
# 种类列表
list1 = []

with open('copy.txt', encoding='utf-8') as f_o:
    # print(f_o.read())
    # 复制数组
    other = f_o.readlines()[1:]
    for line in other:
        # 字符串转列表
        a = line.split()
        # print(a)
        # 每天的销售额
        b = fun2(a[2], a[4])
        # print(b)
        if a[1] not in list1:
            list1.append(a[1])

        day += int(a[4])
        total += b
    meiDay = day/len(other)

print(f'总销售额：{total}')
print(f'平均每日销售数量：{meiDay}')
print(list1)
# T血
s1 = (63+45+129+63+58+48+63)/day
# 衬衫
s2 = 120/day
# 风衣
s3 = (43+25+43+60+43+78)/day
# 牛仔裤
s4 = (60+72+35+90+60+60+140)/day
# 皮草
s5 = (63+24+63+57)/day
# 羽绒服
s6 = (10+69+140+10+10)/day

print(f't恤占比：{s1},\n衬衫占比：{s2}，\n风衣占比：{s3}，\n牛仔裤占比：{s4}，\n皮草占比：{s5}，\n羽绒服占比：{s6}')
