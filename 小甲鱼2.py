
a = int(input('输入成绩：'))
if 100>= a >=0:
    if a >= 90:
        print("A")
    else:
        if a>=80:
            print("B")
        else:
            if a >=60:
                print("C")
            else:
                print("D")
else:
    print("输入不合理！")