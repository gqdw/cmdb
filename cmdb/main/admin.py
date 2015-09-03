from django.contrib import admin
from .models import Hostgroup,Host,Region

# Register your models here.

admin.site.register(Hostgroup)
admin.site.register(Host)
admin.site.register(Region)
