"""
当程序创建进程时，子进程复制了父进程及其所有的数据结构，每个子进程都有自己独立的数据结构
也就是说2个进程中各有一个counter，所以会各打印10次

"""
from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main():
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main()