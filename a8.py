r = range(10)
print(r)
print(list(r))#输出整个列表

r = range(5,20)
print(r)
print(list(r))

r = range(2,20,5)
print(r)
print(list(r))

#判断指定数字是否存在于数列中
#用in 或者 not in
print(10 in r)
print(2 in r)
print(3 not in r)

print(range(1,10))
print(list(range(2,12)))
a = 0
sum = 0
while a < 5:
    sum+=a
    a +=1
print(sum)
a = 0
sum = 0
while a <= 100:
    sum+=a
    a+=2
print(sum)

a = 0
sum = 0
while a <= 100:#奇数加
    if a%2:#加not bool为偶数和 
        sum+=a
    a+=1
print(sum)