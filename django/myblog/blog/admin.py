<<<<<<< HEAD
from django.contrib import admin

# Register your models here.
=======
from django.contrib import admin
from .models import User, Author, Category, Article, Comment


class UserAdmin(admin.ModelAdmin):
    list_display = ('name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'Author', 'category', 'created_time')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'article_id', 'parent_comment', 'created_time', 'content', 'poll_number')


admin.site.register(User, UserAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)


# Register your models here.
>>>>>>> 1b5e7a883400ace46340ae9fbbd6a1fe6d1c7b60
