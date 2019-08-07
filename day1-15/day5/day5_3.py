
for a in range(0, 100):
    for b in range(0, 100):
        if a*14 + 8*b - 200 == 0 and 100 - a - b >= 0:
            print("公鸡%d只, 母鸡%d只，雏鸡%d只" % (a, b, 100-a-b))