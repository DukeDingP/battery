from threading import Thread
import time

def worker1():
    while(1):
        time.sleep(1)
        print("worker1")

def worker2():
    while(1):
        time.sleep(1)
        print("worker2")

if __name__ == '__main__':
    p1=Thread(target=worker1)
    p2=Thread(target=worker2)
    p1.start()
    time.sleep(1)
    p2.start()