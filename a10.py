for i in range(3):
    a = input('请输入密码')
    if a == '88':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print("密码皆错误，电脑自爆中！")
#与for对应的else是在全部循环发生之后的内容
#while也是一样的可以用else

#嵌套循环1
for i in range(1,5):
    for j in range(1,4):
        print("*",end=' ')
    print()
#嵌套循环2
for i in range(1,10):
    for j in range(1,i+1):
        print(i * j,'\t',end='')
    print()

