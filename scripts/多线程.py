from  threading import Thread
import threading
import time
'''
class MyThread(Thread):
    def run(self):
        print 'hello'
        Thread.run(self)

if __name__ == '__main__':
    def do(i):
        print i
    for i in range(20):
        m = MyThread(target=do,args=(i,))
        m.start()
        '''
'''
lock = threading.RLock()
gl_num= 0
def show(arg):
    lock.acquire()
    global gl_num
    time.sleep(1)
    gl_num += 1
    print 'Thread'+str(arg)
    print gl_num
    lock.release()
for i in range(20):
    m = Thread(target=show,args=(i,))
    m.start()
print "Thread stopd"
'''

def do(event):
    print 'start '
    event.wait()
    print 'execute'
event_obj = threading.Event()
for i in range(20):
    m = threading.Thread(target=do,args=(event_obj,))
    m.start()
event_obj.clear()
inp = raw_input('input some thing:')
if inp == "True":
    event_obj.set()