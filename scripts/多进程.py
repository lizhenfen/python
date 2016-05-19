from multiprocessing import Process,Pool
import time

p = Pool(5)

def show(i):
    time.sleep(1)
    return i+2
def say(arg):
    print arg

for i in range(20):
    p.apply_async(func=show,args=(i,),callback=say)
print "end"
p.close()
p.join()