from django.contrib import admin
from client.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('prenom',)


admin.site.register(User, UserAdmin)