from django.contrib import admin
from .models import User, Closet
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'name', 'gender',)


class ClosetAdmin(admin.ModelAdmin):
    list_display = ('dress_img',)


admin.site.register(User, UserAdmin)
admin.site.register(Closet, ClosetAdmin)
