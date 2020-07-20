from threading import *
def even():
    for i in range(0,11,2):
        print(i)


teven=Thread(target=even)
teven.start()


