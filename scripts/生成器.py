filename = 'yield_l.txt'

def Lreadlines(fd):
    seek =0
    while True:
        with open(fd) as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return
for line in Lreadlines(filename):
    print line