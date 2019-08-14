#返回文件的后缀名

file = "hell.c"
file2 = "wang.cpp"
file3 = "cai.pptx"


def getSuffix(file):
    pos = file.rfind('.' ,0, len(file))
    return file[pos:]

def main():
    print(getSuffix(file))
    print(getSuffix(file2))
    print(getSuffix(file3))
if __name__=='__main__':
    main()