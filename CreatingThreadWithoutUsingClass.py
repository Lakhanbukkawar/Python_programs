from threading import *
def display():
    for i in range(10):
        print("Child Thread")
t=Thread(target=display) #Creating thread object
t.start()   #starting of thread
for i in range(1,11):
    print("Main Thread")

