#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
import telnetlib
import pandas as pd
class OperateSw():
    global handler
    def __init__(self,swip,passwd,enable):
        self.swip = swip
        self.passwd= passwd
        self.enable= enable

    def Swlogin(self):  #login switch
        try:
            global handler
            handler = telnetlib.Telnet(self.swip)
        except Exception:
            pass #return {'rc':-1}
        handler.read_until("Password: ")
        handler.write(self.passwd + "\n")
        handler.write("enable\n")
        handler.read_until("Password: ")
        handler.write(self.enable + "\n")
        return {'result':handler}
    def swOptPort(self,port,opt):   #operate the port of shutdown or no shutdown
        handler.write("configure t\n")
        handler.write("int fa0/%s\n" % port)
        handler.write("%s\n" % opt)
        handler.write("end\n")
        time.sleep(1)
        handler.write("write\n")
        return {'rc':0}
    def swVlanStatus(self,cmd):
        handler.read_until('#')
        handler.write( cmd + "\n")
        #ret = handler.read_until('#', 1)
        while True:     #show all informatons 
            ret = handler.read_until('#', 1)
            if "#" in ret:
                break
            for i in range(5):
                    handler.write(' ')
                    time.sleep(0.1)
                    return ret
                    #return {'rc':0,'result':ret}
        
if __name__ == "__main__":
    #opt = OperateSw('192.168.200.254','axcxe6w3','large55')
    opt = OperateSw('192.168.200.254','98amssy37','15cisco43')
    opt.Swlogin()
    res = opt.swVlanStatus("show ip arp")
    print '-------------------------'
    data = pd.DataFrame(res)
    print data
