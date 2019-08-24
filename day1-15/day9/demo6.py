"""
这个Pet为一个抽象类，抽象类就是不能够创建对象的类，专门用来给别人继承，例子里Dog和Cat继承了Pet
Dog和Cat分别重新了父类的make_voice方法，当Dog和Cat的对象调用make_voice方法是，会产生多态行为，
当Dog和Cat会分别去调用make_voice方法是会分别调用对应子对象中的方法


"""

from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()