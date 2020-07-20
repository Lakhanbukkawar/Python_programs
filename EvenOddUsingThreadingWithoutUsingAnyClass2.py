from threading import *
import time
def even():
    for i in range(0,11,2):
        time.sleep(1)
        print(i)

te=Thread(target=even)
te.start()


def odd():
    for i in range(1,10,2):
        print(i)

to=Thread(target=odd)
to.start()
