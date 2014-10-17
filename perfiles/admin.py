# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import perfiles

# Register your models here
class perfilInline(admin.StackedInline):
    model = perfiles

class perfilAdmin(UserAdmin):
    inlines = (perfilInline,)
    #list_display = ('username','first_name','email')
    #search_fields = ('username','first_name','email')
admin.site.unregister(User)
admin.site.register(User,perfilAdmin)
