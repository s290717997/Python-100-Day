"""
对json格式数据进行序列化然后存储到data.json中，
自己加段程序把文件里的数据在打印出来

"""
import json

def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')

    print('解析数据!')
    with open('data.json', 'r', encoding='utf-8') as fs:
        cls = json.load(fs)
        print('type cls = ', type(cls))
        for dict in cls:
            print(dict, ":", cls[dict]);

if __name__ == '__main__':
    main()