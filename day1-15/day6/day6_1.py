def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)


a = int(input("请输入数字a: "))
b = int(input("请输入数字b: "))

print("gcd(a, b) = ", gcd(a, b))
print("lcm(a, b) = ", lcm(a, b))
