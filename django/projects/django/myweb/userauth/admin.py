#-*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import MyUser

from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.

class UserCreationForm(forms.ModelForm):
    first_password = forms.CharField(label="密码",widget=forms.PasswordInput)
    second_password = forms.CharField(label="密码确认",widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('email','name')
    def clean_password(self):
        first_password = self.cleaned_data.get('first_password')
        second_password = self.cleaned_data.get('second_password')
        if first_password and second_password and first_password != second_password:
            raise forms.ValidationError('密码不匹配')
        return second_password
    def save(self,commit=True):
        user = super(UserCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['first_password'])
        if commit:
            user.save()
        return user

   
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = MyUser
        fields = ('email','name','password', 'is_active', 'is_admin')
    def clean_password(self):
        return self.initial['password']

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['email','name','phone','is_admin']
    list_filter = ('is_admin',)
    fieldsets = [
      (None,{'fields':('email','password')}),
      ('个人信息',{'fields':('name','qq','phone')}),
      ('可管理主机',{'fields':('host','hostgroup')}),
      ('权限',{'fields':('is_admin','is_active')}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_password', 'second_password')}
        ),
    ]
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('host','hostgroup')
admin.site.unregister(Group)
admin.site.register(MyUser,UserAdmin)
