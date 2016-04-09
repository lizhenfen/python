from switchclass import Switch

def _mac_parser(asc_mac):
  if asc_mac[0] is None: return
  def to_hex_mac(hmac):
    return ":".join([ hex(ord(hm))[2:] for hm in hmac ])
  return map(to_hex_mac,asc_mac)
def _int_mac(hmac):
  h_num_list = hmac.split(":")
  return '.'.join(map(lambda hmac: str(int(hmac,16)),h_num_list))
def _asc_to_ip(asc):
  return '.'.join([ str(ord(ip)) for ip in asc ])


def get_vlans(s):
  vlans = set(s.get_many('.1.3.6.1.4.1.9.9.68.1.2.2.1.2'))
  return tuple(vlans)
def get_vlan(s,vlan_index):
  vlan = s.get_one('1.3.6.1.2.1.31.1.1.1.1',vlan_index)
  return vlan[0][2:]
def get_manage_vlan_index(s,ip_net):
  index = s.get_many('ipAdEntIfIndex.{}'.format(ip_net))
  if index and index[0]:
    return index[0]
def get_mac(s,index,ip):
   mac = s.get_one('.1.3.6.1.2.1.3.1.1.2','{}.1.{}'.format(index,ip))
   return _mac_parser(mac)[0]

def port_index(s_vlan,mac):
  # same the get_s_port
  int_mac = _int_mac(mac)
  index = s_vlan.get_one('.1.3.6.1.2.1.17.4.3.1.2',int_mac)
  return index[0]
def base_in_port_index(s_vlan,port_index):
  index_port = s_vlan.get_one('.1.3.6.1.2.1.17.1.4.1.2',port_index)
  return index_port[0]
def core_port(s_vlan,index_port):
  port = s_vlan.get_one('1.3.6.1.2.1.31.1.1.1.1',index_port)
  return port[0]


def neibor_ip(s,index_port):
  ip = s.get_many('1.3.6.1.4.1.9.9.23.1.2.1.1.4',index_port)
  if ip:
    return _asc_to_ip(ip[0])

def _get_mac_index_1(s_vlan,mac):
   int_mac = _int_mac(mac)
   index = s_vlan.get_one('.1.3.6.1.2.1.17.4.3.1.2',int_mac)
   if len(index) == 0:
     return 
   return index[0]
def _get_mac_index_2(s_vlan,i_1):
   index =  s_vlan.get_one('.1.3.6.1.2.1.17.1.4.1.2',i_1)
   if len(index) == 0:
     return
   return index[0]
def get_s_port(s_vlan,mac):
  index_1 = _get_mac_index_1(s_vlan,mac)
  if index_1 is None:
    return
  index   = _get_mac_index_2(s_vlan,index_1)
  if index is None:
    return
  port = s_vlan.get_one('.1.3.6.1.2.1.31.1.1.1.1',index)
  return port[0]
def get_all_ip_mac(s):
  macs = _mac_parser(s.get_many('mib-2.3.1.1.2'))
  ips  = s.get_many('mib-2.3.1.1.3')
  types= s.get_many('ipNetToMediaType')
  return zip(ips,macs,types)
if __name__ == "__main__":
  s = Switch('192.168.200.254')
  s1 = Switch('192.168.200.254',community='public@27')
  s2 = Switch('192.168.200.130',community='public@27')
  ip = '192.168.27.26'
  #print  get_vlan(s,62)
  vlan_index  = get_manage_vlan_index(s,'192.168.27')
  print 'vlan_index: ',vlan_index
  mac   = get_mac(s,vlan_index,ip)
  print 'mac: ',mac
  print "oct_mac: ",_int_mac(mac)
  index_port= port_index(s1,mac) 
  print "index_port:",index_port
  vlan_id = get_vlan(s,vlan_index)
  print 'vlan_id: ',vlan_id
  #print get_s_port(s2,mac)
  index_1 = base_in_port_index(s1,index_port)
  #asc = neibor_ip(s,31)
  #print _asc_to_ip(asc)
  #print get_all_ip_mac(s)
