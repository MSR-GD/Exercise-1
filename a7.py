#a = input('是否是会员Y/N：')
b = int(input('消费金额：'))
'''
if a == 'Y':
    if b >= 200:
        print('总花费为:',str(b*0.8))
    else:
        print('总花费为:',str(b))
else:
    print('不是会员贵10倍！：',str(b*10))
'''
#条件表达式
a = 10 if 5 < 10 else 20
print(a)
#pass语句就是暂时占个位置，以便后续使用

if a > 5:
    pass
#空语句，方便以后填充