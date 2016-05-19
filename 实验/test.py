card_file = "c.txt"
'''
lizhen 123 111111 1500 1500 123444444
xiaobao 123 222222 1500 1500 123444444
with open(card_file,'w') as f：
    f.write(line)
'''
with open(card_file,"rb+") as f:
        for line in f:
           line = line.replace('222222','333333')
           #print line,
           f.write(line)