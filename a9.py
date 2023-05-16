for i in 'Python':
    print(i)

for a in range(10):
    print(a)

for _ in range(5):
    print("人生苦短！")

sum = 0
for i in range(0,101,2):
    sum+=i
print(sum)

#水仙花数
for i in range(100,1000):
    a = i%10
    b = (i//10)%10
    c = i//100
    if(a**3 + b**3 + c**3 == i):
        print(i)
#break
for i in range(3):
    a = input('密码：')
    if a == '888':
        print('密码正确')
        break
    else:
        print("请重新输入")


#continue

for i in range(51):
    if i % 5 != 0:
        continue
    print(i)
