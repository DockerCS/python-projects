from django.contrib import admin
from .models import View, ViewNum


# Register your models here.
@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    """view recorder admin"""
    list_display = ('content_type', 'object_id', 'ip_address', 'user', 'view_time')
    ordering = ('-view_time',)

@admin.register(ViewNum)
class ViewNumAdmin(admin.ModelAdmin):
    """view num admin"""
    list_display = ('content_type', 'object_id', 'view_num')


# admin.site.register(Recorder, RecorderAdmin)
# admin.site.register(ViewNum, ViewNumAdmin)

# Register your models here.
