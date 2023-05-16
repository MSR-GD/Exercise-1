a = 3.1415
print(a,type(a))
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1+n2)#浮点数有不准确性
print(n1+n3)
#避免不准确性代码
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
#字符串
#''不行     ""不行      """可以在多行用
#多行注释

"""
嘿嘿，我就是多行注释
"""

