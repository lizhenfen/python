#coding:utf8
from django.db import models

from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

class MyUserManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email = self.normalize_email(email),
            name  = name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password=None):
        user = self.create_user(email,name=name,password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
from hosts.models import Host,HostGroup
class MyUser(AbstractBaseUser):
    email = models.EmailField(u"邮件地址",max_length=255,unique=True)
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    name = models.CharField(u'姓名',max_length=255,blank=True,null=True)
    qq   = models.CharField(u"QQ",max_length=30,blank=True,null=True)
    phone= models.CharField(u'手机',max_length=15,blank=True,null=True)
    objects = MyUserManager()

    host = models.ManyToManyField(Host,blank=True)
    hostgroup = models.ManyToManyField(HostGroup,blank=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name']
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def has_perm(self,perm,obj=None):
       return True
    def has_module_perms(self,app_label):
       return True
    @property
    def is_staff(self):
       return self.is_admin
    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = u"用户信息"

