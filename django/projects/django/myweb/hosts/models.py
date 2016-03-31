#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Host(models.Model):
    hostname = models.CharField(max_length=128)
    ip_addr  = models.GenericIPAddressField(unique=True)
    port     = models.IntegerField(default=22)
    idc      = models.ForeignKey('IDC')
    system_type_choice = (
        (0,'linux'),
        (1,'windows')
    )
    system_type = models.IntegerField(choices=system_type_choice)
    enabled   = models.BooleanField(default=True)
    modify_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return "%s(%s)" % (self.hostname,self.ip_addr)
    class Meta:
        verbose_name = u"主机列表"
        verbose_name_plural = u"主机列表"
class IDC(models.Model):
    name = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'机房'
        verbose_name_plural = u'机房'
class HostUser(models.Model):
    auth_type_choice = (
        ('ssh-password','SSH/PASSWORD'),
        ('ssh-key','SSH/KEY'),
    )
    auth_type = models.CharField(choices=auth_type_choice,max_length=64,default='ssh-password')
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128,blank=True,null=True)
    def __unicode__(self):
        return "%s(%s)" % (self.auth_type,self.username)
    class Meta:
        unique_together = ('auth_type','username','password')
        verbose_name     = u'远程用户'
        verbose_name_plural = u'远程用户'
class HostGroup(models.Model):
    name = models.CharField(unique=True,max_length=64)
    memo = models.TextField(blank=True,null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'主机组'
        verbose_name_plural = u'主机组'
class BindHostToUser(models.Model):
    host = models.ForeignKey('Host')
    user = models.ForeignKey('HostUser')
    hostgroup = models.ManyToManyField('HostGroup')
    def __unicode__(self):
        return "%s:%s" % (self.user.username,self.host.ip_addr)
    class Meta:
       unique_together = ('host','user')
       verbose_name = u'用户主机关系'
       verbose_name_plural = u'用户主机关系'
