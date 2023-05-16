a = 'qwertyui'
for i in a:
    print(i,end = ' ')
m = ['qwe','asdsd','12q3','q']
for i in m:
    print(i,len(i))
#for i in range(10):
#    print(i)
for i in range(0,10,2):
    print(i)

a = list(range(0,100,5))
print(a)

for i in range(0,100,1):
    if i - 95 == 0:
        break
    else:
        if i == 50:
            continue
        else:
            print(i)

