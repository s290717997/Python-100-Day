#练习5：计算指定的年月日是这一年的第几天

days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def if_leap_year(year):

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def which_day(year, month, day):
    sum = 0
    for i in range(1, month):
        sum += days_of_month[i-1]
        if i == 2 and if_leap_year(year):
            sum += 1
    pass
    return sum + day


def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))


if __name__ == '__main__':
    main()