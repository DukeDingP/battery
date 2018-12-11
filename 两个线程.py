from multiprocessing import Process
import time

def worker1():
    while(1):
        time.sleep(1)
        print("worker1")

def worker2():
    while(1):
        time.sleep(0.5)
        print("worker2")

if __name__ == '__main__':
    p1=Process(target=worker1)
    p2=Process(target=worker2)
    p1.start()
    p2.start()