from django.contrib import admin
from .models import User, Closet
# Register your models here.


class ClosetInLine(admin.StackedInline):
    model = Closet
    extra = 2


class UserAdmin(admin.ModelAdmin):
    inlines = (ClosetInLine,)
    list_display = ('username', 'email', 'gender',)


class ClosetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'dress_img',)


admin.site.register(User, UserAdmin)
admin.site.register(Closet, ClosetAdmin)
