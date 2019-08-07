#输入一个数，判断是否为完美数


import math
num  = int(input("请输入一个数: "))

list = []


for i in range(1, num):
    if num % i == 0:
        list.append(i)

print("num的约数为：", list)

sum = 0
for x in list:
    sum += x

if sum == num:
    print("你输入的num是个完美数")
else:
    print("你输入的num不是个完美数")