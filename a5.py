print(9//2)

#解包赋值,必须是左右数量相等
a,b,c = 10,20,30
print(a,b,c)

a1=a2=a3=15#链式赋值,指向同一个对象地址id
print(a1,id(a1))
print(a2,id(a2))
print(a3,id(a3))

a,b = 10,20#python的交换
a,b = b,a
print(a,b)

a1 = 10
b1 = 10

print(a1 == b1)
print(a1 is b1)#比较id是否相等
print(a1 is not b1)#不相等id

s1 = [11,22,33,44]
s2 = [11,22,33,44]
print(s1 == s2)#比较的是值
print(s1 is s2)#不相等的
print(id(s1),id(s2))