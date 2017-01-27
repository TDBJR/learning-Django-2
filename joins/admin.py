from django.contrib import admin
from .models import Join



class JoinAdmin(admin.ModelAdmin):
#  list_display = adds in the attributes in a formatted table to the admin page
    list_display = ['email', 'friend', 'timestamp', 'updated']
    class Meta:
        model = Join


#this allows you to alter the Join class in the admin page
admin.site.register(Join, JoinAdmin,)









