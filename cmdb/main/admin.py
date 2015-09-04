from django.contrib import admin
from .models import Hostgroup,Host,Region,Search

# Register your models here.

admin.site.register(Hostgroup)
admin.site.register(Host)
admin.site.register(Region)
admin.site.register(Search)
