"""
打开文件的基本操作，'r'为只读，encoding为编码方式
"""

def main():
    f = open('致橡树.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()