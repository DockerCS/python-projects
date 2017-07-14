from django.contrib import admin
from .models import User, Author

# 用户
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile')

# 作者
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile')


admin.site.register(User, UserAdmin)
admin.site.register(Author, AuthorAdmin)
# Register your models here.
