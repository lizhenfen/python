import netsnmp
from netsnmp.client import Session
from netsnmp.client import Varbind,VarList
class Switch(Session):
  def __init__(self,desthost,version=2,community='public'):
    self.Version = version
    self.DestHost = desthost
    self.Community= community
    self._host = self.DestHost
    self._com  = self.Community
    super(Switch,self).__init__(Version=self.Version,DestHost=self.DestHost,Community=self.Community)
  def set_manage_ip(self,ip,community='public'):
    self.newip = ip
    super(Switch,self).__init__(Version=self.Version,DestHost=self.newip,Community=self.Community)
  def set_community(self,vlan):
    self.newcomm = '{}@{}'.format(self.Community,vlan)
    super(Switch,self).__init__(Version=self.Version,DestHost=self.DestHost,Community=self.newcomm)
  def del_community(self):
    super(Switch,self).__init__(Version=self.Version,DestHost=self._host,Community=self._com)  
  def _set_oid(self,tag=None,iid=None,val=None,type=None):
    return VarList(Varbind(tag,iid,val,type))
  def get_one(self,tag=None,iid=None,val=None,type=None):
    oid = self._set_oid(tag,iid,val,type)
    return self.get(oid)
  def get_many(self,tag=None,iid=None,val=None,type=None):
    oid = self._set_oid(tag,iid,val,type)
    return self.walk(oid)
if __name__ == "__main__":
  s = Switch('192.168.200.22',community='public@27')
  #print s.get_many('ipNetToMediaPhysAddress')
  #print s.get_one('.1.3.6.1.2.1.3.1.1.2','62.1.192.168.27.252')
  #print set(s.get_many('.1.3.6.1.4.1.9.9.68.1.2.2.1.2'))
  int_mac="176.131.254.175.118.81"
  #print s.get_many('.1.3.6.1.2.1.17.4.3.1.2.{}'.format(int_mac))
  print s.get_one('.1.3.6.1.2.1.17.4.3.1.2',int_mac)
