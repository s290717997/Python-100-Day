#练习1：输入一个数判断是不是素数。

from math import sqrt

num  = int(input("请输入一个整数："))
print("您输入的整数为：", num)
is_prime = True
for x in range(2, int(sqrt(num)) + 1):
    if num % x == 0:
        is_prime = False;
        break
if is_prime and num != 1:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)
