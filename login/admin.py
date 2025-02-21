from django.contrib import admin

from login.models import login
class loginList(admin.ModelAdmin):
    list_display = ('id','user', 'password')
    list_display_links = ('id', 'user')
    search_fields = ('user',)

admin.site.register(login, loginList)
