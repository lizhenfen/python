send:
	仅发送单个包
	IP(src="sourceIp",dst="destinationIp",ttl=128)
	ICMP(type=0)  #0表示应答
	TCP(sport=666,dport=[20,80,443],flags="S") 
		# 多个端口TCP(dport=[20,21,22]),S表示SYN scan
		# A表示 SYN ACK
		# RandShort() #随机端口
		#inter=0.5   #间隔时间
		#retry = 2   #重试次数
		#timeout =1  #超时时间
	DNS(rd=1,qd=DNSQR(qname="www.baidu.com"))
	#rd=1  允许recusion
	#qd=DNSQR  DNS question recoer , 
	#	qname 域名 qtype="NS"  默认A记录，可以更改
	traceroute([destinationIp,],maxttl=20)  #可以一次发送多个
	#maxttl=  最大ttl
	#dport=   目标端口
	arping("net.*")  #发送arp包
读写pacap:
	内置的过滤：sniff()  #过滤所有的 
				w_pkts = sniff(iface="eth0",filter="icmp",count=10)  #filter="tcp and port 80"
				pkts = rdpcap("/path/to/file")
				#pkts.summary() #查看详细
				#pkts[n]  #查看第n个
				wrpcap("/path/to/file",w_pkts)
				
	显示详细：
		a = _
		a.summary()  #汇总的详细
		a[n]   #显示第n个包
	package number(0000), frame type(Ether) , Internet layer(IP), Transfer layer(TCP)
	application layer(DNS) , packet data()
包层：
	a=Ether()
	b=IP()
	c=TCP()
	sendp(a/b/c)  #二层发送
冻结包：
	send(IP(dst="")/fuzz(UDP()/NTP(version=4),loop=1))
	send(Ether(dst=clientMAC)/ARP(op="who-has",psrc=gateway,pdst=client),iter=RandNum(10,40),loop=1)
	send(Ether(dst=clientMAC)/Dot1Q(vlan=1)/Dot1Q(vlan=2)/ARP(op="who-has",psrc=gateway,pdst=client),iter=RandNum(10,40),loop=1
	arpcacheposion(target,victim,interval=60) #发送本机 的arp到目标主机
	sendp(Ether()/Dot1Q(vlan=3)/Dot1Q(vlan=7)/IP(dst=target)/ICMP)
	#vlan=3是本机的vlan,vlan=7是目标vlan
	
Sending and Receiving:
  默认源端口是： 22 或 ftp_data
  三层：
	sr(): 返回应答 和 未知的应答的包，简陋
		例：
			p = sr(IP(dst="destinationIp")/TCP(dport=22))  #>>>p  显示汇总消息
			ans,unans = _  #_ 表示最近一次的结果
			ans.summary()  #显示详细汇总信息
			unans.show()   #显示未应答的详细信息
			SA: syn-ack
			RA: rst-ack   reset&&acknowledge  #无应答 
	sr1(): 只返回应答的包,比较详细
		查看结果： 
			package_name = sr1(dst="destinationIp"/ICMP())
			package_name.show()
		例：
			>>> m.show()
			###[ IP ]###
			  version= 4L
			  ihl= 5L
			  tos= 0x0
			  len= 28
			  id= 23106
			  flags= 
			  frag= 0L
			  ttl= 63
			  proto= icmp
			  chksum= 0x700f
			  src= 192.168.20.66
			  dst= 192.168.27.253
			  \options\
			###[ ICMP ]###
				 type= echo-reply
				 code= 0
				 chksum= 0xffff
				 id= 0x0
				 seq= 0x0
			###[ Padding ]###
				load= '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            查看具体的某个的内容： m[IP].dst
  二层：
	srp():返回应答 和 未知的应答的包
重要：
	ls(): 显示所有的协议，或 协议的参数
	lsc(): 显示所有的命令