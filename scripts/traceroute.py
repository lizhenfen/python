import socket
socket.setdefaulttimeout(3)
def man(host):
   host_addr = socket.gethostbyname(host)
   icmp = socket.getprotobyname('icmp')
   udp = socket.getprotobyname('udp') 
   ttl = 1
   port= 33434   #33534
   while True:
     recv_data = socket.socket(socket.AF_INET,socket.SOCK_RAW,icmp)
     send_data = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,udp)
     recv_data.bind(('',port))
     send_data.setsockopt(socket.SOL_IP,socket.IP_TTL,ttl)
     ttl += 1
     send_data.sendto('',(host,port))
     try:
         _,addr = recv_data.recvfrom(512)
     except:
         pass
     finally:
         recv_data.close()
         send_data.close()
     if addr[0] is not None:
         print addr[0]
     if addr[0] == host_addr or ttl == 30:
         break
if __name__ == "__main__":
  man('www.baidu.com')


