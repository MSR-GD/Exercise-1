a = int(input("输入成绩："))
if 100 >= a >= 90:
    print("A")
elif 90 > a >= 80:
    print("B")
elif 80 > a >= 60:
    print("C")
elif 60 > a >= 0:
    print("D")
else:
    print("输入错误！")
#三元操作
a = 7 if 20 < 10 else 14
print(a)
#断点错误判断
assert 3>4