from threading import *
import time
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread-1")

t=MyThread()
t.start()
for i in range(10):
    time.sleep(1)
    print("Main Thread-1")
    
