#输入一个整数，输入该数范围内的“斐波拉切数列”。

num = int(input("请输入一个整数（将输出该范围内的“斐波拉切数列”）："))
n1 = 1
n2 = 1

flag = True;
if num == 1:
    print("[ 1 ]")
    exit
if num >= 2:
    print("[ 1 ][ 1 ]", end="")

while flag:
    index = n1 + n2
    if index >= num:
        flag = False
    else:
        print("[", index, "]", end="")
        n1 = n2
        n2 = index
