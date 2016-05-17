#!/usr/bin/env python
#coding: utf8
def lazy(num):
    """
        懒惰算法
    """
    i = 0
    while i < len(num):
        if i == 0 or num[i-1] <= num[i]:
            i += 1
        else:
            num[i-1],num[i] = num[i],num[i-1]
            i -= 1
    return num



def t_split(num):
    """
        #二分算法
    """
    len_num = len(num)/2
    lft_num = num[:len_num]
    rht_num = num[len_num:]
    if len(lft_num) > 1: lft_num = t_split(lft_num)
    if len(rht_num) > 1: rgt_num = t_split(rht_num)
    res = []
    while lft_num and rht_num:
        if lft_num[-1] >= rht_num[-1]:
            res.append(lft.pop())
        else:
            res.append(rht_num.pop())
        res.reverse()
        #print lft_num,'rht',rht_num
    return (lft_num or rht_num) + res

print t_split(range(100))