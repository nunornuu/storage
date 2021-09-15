name = 'root'
psw = 'admin'
# 次数
num = 3

while num > 0:
    a = input('用户名：')
    b = input('密码:')
    if name != a and psw != b:
        num = num - 1
        print('用户名或密码错误')
    else:
        print('登录成功')
        break
    if num == 0:
        print('再见')

