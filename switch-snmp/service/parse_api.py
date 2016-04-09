#!/usr/bin/env python
from cisco import *
import re
import os
os.environ.setdefault('LD_LIBRARY_PATH','/usr/local/lib/')
def parse_net(ip):
  ip_re = re.compile(r'((\d{1,3}\.){3})(\d{1,3}$)')
  match = ip_re.match(ip)
  if match:
    net = match.groups(0)
    return net[0].rstrip('.')
def parse_ip_to_mac(s,ip):
  sub_net = parse_net(ip)
  index   = get_manage_vlan_index(s,sub_net)
  if index is not None:
    return (index,get_mac(s,index,ip))
def parse_switch_ip_port(s,ip):
  s.del_community() 
  index,mac = parse_ip_to_mac(s,ip)
  vlan  = get_vlan(s,index)
  if '/' in vlan:
      return vlan
  s.set_community(vlan)
  port_i = port_index(s,mac) 
  if port_i is None:
    return
  index_port = base_in_port_index(s,port_i)
  swtich_manage_ip = neibor_ip(s,index_port)
  core_port = get_s_port(s,mac)
  s.set_manage_ip(swtich_manage_ip)
  port = get_s_port(s,mac)
  return (core_port,swtich_manage_ip,port,mac)
 
def parse_all(s):
  data = get_all_ip_mac(s)
  data_dict = {}
  for ip in data:
    if not ip[0].endswith('.254'):
       data_dict[ip[0]] = parse_switch_ip_port(s,ip[0])
       yield data_dict
if __name__ == "__main__":
  import os
  from opt import Switch
  s = Switch('192.168.200.254')
  for i in parse_all(s):
    print i
