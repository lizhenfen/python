from django.contrib import admin

import models


class HostAdmin(admin.ModelAdmin):
    list_display = ['hostname','ip_addr','port','idc','system_type','enabled']
    search_fields = ['hostname','ip_addr']
    list_editable = ('port',)
    list_filter  = ['idc','system_type']
class BindHostToUserAdmin(admin.ModelAdmin):
    filter_horizontal = ('hostgroup',)
admin.site.register(models.Host,HostAdmin)
admin.site.register(models.IDC)
admin.site.register(models.HostUser)
admin.site.register(models.HostGroup)
admin.site.register(models.BindHostToUser,BindHostToUserAdmin)
