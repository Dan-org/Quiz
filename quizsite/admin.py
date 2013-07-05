from django.contrib import admin

### Unregsiter Clutter ###
#from django.contrib.sites.models import Site
#admin.site.unregister(Site)

from django.contrib.auth.models import Group
admin.site.unregister(Group)