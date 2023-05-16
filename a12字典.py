a1 = {"MSR":10,"qwe":11}
print(a1)
a1 = {}
print(a1)
a1 = {'MSR':1111}
print(a1)

print(type(a1))
a1 = dict(name='MSR',name2='qwe')
print(a1)

#获取字典的元素
print(a1["name"])


print(a1.get('name'))

#若无存在数据，第一种方法会报错，第二种会报默认值None
#若要None改为其他值，看下面例题
print(a1.get('namee'),8)


s1 = {'张三':100,'李四':97,'王五':11}
print('张三' in s1)
print('张三' not in s1)

del s1['张三']
print(s1)
#s1.clear()
#print(s1)
#新增元素
s1['陈六']=22
print(s1)
#修改元素
s1['陈六']=33
print(s1)