from django.contrib import admin

from .models import User



class UserAdmin(admin.ModelAdmin):
    search_fields = ['apellidos']
    list_display = ('id','apellidos','nombres','username')



# Register your models here.

admin.site.register(User, UserAdmin)