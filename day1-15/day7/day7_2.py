#随机生成验证字符

import random

def generate_code(code_len = 4):
    digitCnt = range(1, code_len+1)
    charCnt = code_len - digitCnt



    print("digit = ", digitCnt, " charCnt = ", charCnt)



def main():
    code = generate_code(5)
    print(code)


if __name__ == '__main__':
    main()