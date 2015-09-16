from django.contrib import admin
from .models import Hostgroup,Host,Region,Search,Os,Dbtype,Rds

# Register your models here.
class HostAdmin(admin.ModelAdmin):
	list_display = ('hostname','eth0','eth1','group','os')
	#search_fields= ['group']
	search_fields= ['hostname','eth0']
	#search_fields= ('hostname','eth0','eth1','group')
	list_field = ('group',)
#	filter_horizontal = ('Region',)

admin.site.register(Hostgroup)
#admin.site.register(Host)
admin.site.register(Host,HostAdmin)
admin.site.register(Region)
admin.site.register(Rds)
admin.site.register(Dbtype)
#admin.site.register(Search)
admin.site.register(Os)
