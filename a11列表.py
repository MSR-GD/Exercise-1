#列表的俩种创建方式

s1 = ['World',66,32.32]

s2 = list([21,22,23,25,21,'qwe'])

print(s2)

#输出索引值

print(s1[0])#与c一致

#第二种，倒叙输出,从-1开始右向左

print(s1[-1])
print(s1[-3])
#index输出指定数的索引值
print(s1.index(66))
print(s2.index(21,1,6))#输出位于1-6区间拥有这个值的 的索引值

lst = [10,20,30,40,50,60,70,80]

lst2 = lst[0:5:1]#[初始位置，终止位置，步长]
print(lst2)

lst3 = lst[::-1]#负数情况
lst4 = lst[::-2]#
lst5 = lst[5:0:-1]#步长为负数，初始位置和终止位置调换
print(lst3)
print(lst4)
print(lst5)

#用in 或者 not in 判断列表内是否存在某个元素
print(10 in lst5)
print(20 not in lst5)

#append在最后一个位置插入一个内容
lst1 = [10,20,30]
print('添加元素之前：'+str(lst1))
lst1.append(40)
print('添加元素之后：'+str(lst1))
lst11 = [15,25]
#lst1.append(lst11)#可以引用列表,
#extend在最后一个位置插入多个内容
lst1.extend(lst11)
print(lst1)
#insert在x坐标插入一个数
lst1.insert(2,50)
print(lst1)
#切片
#在x坐标之后的内容被替换
lst1[1:] = lst2
print(lst1)

#列表删除指定内容
lst1.remove(10)
print(lst1)

#列表删除指定坐标内容
lst1.pop(2)
print(lst1)

#pop默认删除最后一个
lst1.pop()
print(lst1)

#切片创建新列表
lst1a = lst1[1:3]
print(lst1a)
print(lst1)

#用切片删除指定内容（变空）
lst1[1:3] = []
print(lst1)

#删除列表所有内容
lst1.clear()
print(lst1)

#删除列表
del lst1

#改变列表指定的内容的值

lst1 = [11,22,33,44,55]
lst1[0] = 777
print(lst1)

#改变列表指定范围的值

lst1[1:3] = [135,876,22362,45]
print(lst1)

#排序列表   升序  改变原列表

lst1.sort()#等价于sort(reverse=False)
print(lst1)

#降序

lst1.sort(reverse=True)
print(lst1)

#不改变原列表 sorted

a = sorted(lst1)
print(lst1)
print(a)
a = sorted(a,reverse=True)
print(a)

#列表生成式
a = [i for i in range(1,10)]
print(a)
a = [i*2 for i in range(1,10)]
print(a)