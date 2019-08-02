year = int(input("请输入年份："))

if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print("%d年为闰年" % year)
else:
    print("%d年不是闰年" % year)