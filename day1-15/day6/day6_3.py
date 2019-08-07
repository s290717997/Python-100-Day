def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

a = int(input("请输入数字："))
if is_prime(a):
    print("你输入的是素数")
else:
    print("你输入的不是素数")