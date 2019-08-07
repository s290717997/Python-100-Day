#练习2：输入两个正整数，计算最大公约数和最小公倍数。

from math import *

a = int(input("请输入整数a:"))
b = int(input("请输入整数b:"))

if a > b:
    a, b = b, a

for factor in range(a, 0, -1):
    if a % factor == 0 and b % factor == 0:
        print("%d和%d的最大公约数%d" % (a, b, factor))
        print("%d和%d的最小公倍数%d" % (a, b, a * b //factor))
        break;