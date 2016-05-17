#!/usr/bin/env python
#coding: utf8
# date: 2016-05-17
# __auther__:
'''
    主要用于查看cisco的 交换机的配置和数据
    
'''

from telnetlib import Telnet

def showdata(data):
    #展示数据
    print data

# 此装饰器用于登录系统
def wrapper(func):
    def _deco(ip,port,passwd,cmd,finish='>'):
        tel = Telnet(ip,port)
        tel.read_until('Password: ')
        tel.write(passwd+'\n')
        tel.read_until(finish)
        tel.write(cmd+'\n')
        data = tel.read_until(finish)
        ret = func(ip,port,passwd,cmd,finish)
        showdata(data)
        return ret
    return _deco

# 操作网络设备
@wrapper
def func(ip,port,passwd,cmd,finish):
  print "func function called"
  print "cmd: ",cmd


if __name__ == "__main__":
  #测试运行
  func('192.168.200.24',23,'****','sh ip interface')