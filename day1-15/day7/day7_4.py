#练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。


list1 = [42, 52, 36, 36, 363, 645]
list2 = [22, 52, 36, 36, 36, 6]

def max2(list):
    tmp = sorted(list, reverse=True)

    return tmp

def main():
    print(max2(list1)[0:2])
    print(max2(list2)[0:2])

if __name__ == '__main__':
    main()