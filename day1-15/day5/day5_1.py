#输入一个数，判断是否为水仙花数

from math import pow
num = int(input("请输入一个三位数: "))

while not 100 <= num and num < 1000:
    num = int(input("请重新输入一个三位数: "))

a = int(num % 10)        #个位
b = int(num % 100 / 10)  # 十位
c = int(num / 100)       #百位
print ("a = %d, b = %d, c = %d" % (a, b, c))
if a**3 + b**3 + c**3 == num:
    print("你输入的数字为: ", num, " 是个水仙花数")
else:
    print("你输入的数字为: ", num, " 不是个水仙花数")

print("-------------------分隔线------------------------------")
#三位数的水仙花数
print("三位数的水仙花数：")
for num in range(100, 1000):
    a = int(num % 10)  # 个位
    b = int(num % 100 / 10)  # 十位
    c = int(num / 100)  # 百位
    if a**3 + b**3 + c**3 == num:
        print (num , "是个水仙花数")
    pass
pass

