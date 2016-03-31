#coding:utf-8
from gevent.pool import Pool
from gevent.subprocess import Popen, PIPE
import os
import sys
import gevent
 
def worker():
    print 'start'
    sub = Popen(['sleep 10'], stdout=PIPE, shell=True)
#    sub = Popen(['top'], stdout=PIPE, shell=True)
    out, err = sub.communicate()
    print 'end'
    return out.rstrip()
 
def run():
    for i in range(10):
        print i
        g = gevent.spawn(worker)
    g.join()
 
if '__main__' == __name__:
    '''ºÄÊ± 10.0609869957
    '''
    import time
    start_at = time.time()
    run()
    print time.time() - start_at