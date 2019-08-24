"""
静态方法和类方法都是通过发消息来调用的
使用@staticmethod来声明

静态方法可以直接通过类名来调用方法
也可以通过发消息来调用类方法，但是在参数中必须指定类名
t = Triangle(a, b, c)
print(Triangle.perimeter(t))

个人理解：
（1）静态方法不需要对象，可以通过类名来调用
（2）非静态方法必须需要一个对象，要直接使用对象的方法调用，要不用类名调用，传入对象
"""

from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')


if __name__ == '__main__':
    main()