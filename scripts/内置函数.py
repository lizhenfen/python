#_*_coding:utf-8 -*-

#常用方法：
'''
__name__ == "__main__"
__file__  文件名
__doc__  文档说明

'''
#定义变量
a = [ str(i) for i in range(10) ]
#显示变量的可用属性
print dir(a)
#显示变量的可用属性和值, 字典形式
print vars()
#查看帮助
print help(a)
#查看内存地址
print id(a),id(a[0])
#查看变量类型
print type(a)

#导入模块
import sys
#重新导入模块
reload(sys)

#比较
print cmp(1,2)

#绝对值
print abs(-1)

#换算数据成bool类型
print bool(0),bool(-1)

#除法; 可用于分页
print divmod(2,1)

#最大,最小,求和
print max(a),min(a),sum([int(i) for i in a])
#指数, 2的11次方
print pow(2,11)

#求长度
print len(a)
#所有为真返回为真，任何为真返回真
print all([0,1,2])
print all(a)
print any(a)

#把数字转化成ASCII码
print chr(78)
#把ASCII码转化成数字
print ord('A')
#十六进制，八进制，二进制
print hex(10),oct(10),bin(10)

#生成列表
print range(10)
for i in xrange(10):
    print i

#生成序列号
for i in enumerate(a,1):
    print i
#格式化
s = "i am {0} {1}"
print s.format('lizhen',1)

#使用函数
def func(*b):
    print b
apply(func,(a))