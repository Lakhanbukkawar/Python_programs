from threading import *
import time
class Test:
    def display(self):
        for i in range(10):
            time.sleep(1)
            print("Child Thread-2")

obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Tharead-2")
    
