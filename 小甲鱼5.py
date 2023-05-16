a = ['qwe','ewq','atm','奥特曼']#列表
print(a)
a2 = ['qwe',12,32,'aaaa']#混合列表
print(a2)
a3 = []#空列表
print(a3)
a.append('ewq')#添加一个列表内容
a.append(13)
print(a)
a.extend(['aaaa','aaaa',32,75])#添加多个列表内容
print(a)
a.insert(1,'1')#在x位置插入一个内容
print(a)
a.insert(5,'MSR')
print(a)
temp = a[0]#交换
a[0] = a[1]
a[1] = temp
print(a)
print(a[0])#输出单个
a.remove('1')#删除指定的某个内容
print(a)
del a[1]#删除指定位置的内容
print(a)
a.pop()#删除最后一个内容
print(a)
a.pop(1)#删除指定位置的内容
print(a)
print(a[1:3])#输出指定区域的内容
print(a[:])#全输出
print(a[:5])#从起点到x输出
print(a[5:])#从x输出到末尾