#!/usr/bin/env python
#-*- coding:utf-8 -*-
card_file = "card.txt"

def mk_md5(strs):
    import hashlib
    str_md5 = hashlib.md5()
    str_md5.update(strs)
    return str_md5.hexdigest()
def  getcard():
    card_username = raw_input("姓名：")
    card_passwd  = raw_input("密码：")
    card_no    = raw_input("卡号(6位)：")
    telphone  = raw_input("电话：")
    card_quota = str(15000)
    current_quota = card_quota
    with open(card_file,'a+') as f:
        if card_no.isdigit():
            card_passwd = mk_md5(card_passwd)
            line = ' '.join([card_username,card_passwd,card_no,card_quota,current_quota,telphone,'\n'])
            f.write(line)



def login():
    login_count = 0
    while login_count < 3:
        user_name = raw_input("请输入姓名( 或卡号)：")
        if len(user_name.strip()) == 0:
            continue
        passwd = raw_input("密码：")
        login_count += 1
        with open(card_file) as f:
            for line in f.xreadlines():
                if user_name in line:
                    if mk_md5(passwd.strip()) == line.strip().split()[1]:
                        print "欢迎登录信用卡中心"
                        return True
                    else:
                        print "密码错误"
                        break
            else:
                print "用户(或卡号)不存在."
                continue
    else:
        print "您已经超过三次,请稍后再试"
def display_card_opt():
    card_dic = {
        '领取信用卡':'getcard',

    }
    card_opt = ['领取信用卡','还款']
    for num,k in enumerate(card_opt):
        print num,k
    select_num = raw_input("输入您的操作: ").strip()
    if select_num.isdigit():
        select_num = int(select_num )
        if select_num < len(card_opt):
            func_opt = card_dic.get(card_opt[select_num])
    else:
        func_opt =card_dic.get(select_num)
    return func_opt

if __name__ == "__main__":
    getcard()
    #modify_card_passwd()
    #print display_card_opt()