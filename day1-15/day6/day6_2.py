def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

a = int(input("请输入数字："))

if is_palindrome(a):
    print("你输入的是回文数")
else:
    print("你输入的不是回文数")