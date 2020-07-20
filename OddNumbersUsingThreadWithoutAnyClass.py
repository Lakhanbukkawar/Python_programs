from threading import *
def odd():
    for i in range(1,10,2):
        print(i)

to=Thread(target=odd)
to.start()
