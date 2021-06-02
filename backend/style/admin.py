from django.contrib import admin
from .models import Style
# Register your models here.


class StyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'style_img', 'feature',)


admin.site.register(Style, StyleAdmin)
