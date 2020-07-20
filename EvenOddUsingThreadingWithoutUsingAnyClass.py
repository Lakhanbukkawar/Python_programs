from threading import *
def even():
    for i in range(0,11,2):
        print(i)


teven=Thread(target=even)
teven.start()

#def odd():
   # for i in range(1,10,2):
     #   print(i)

#todd=Thread(target=odd)
#todd.start
