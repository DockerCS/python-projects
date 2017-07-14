from django.contrib import admin
from .models import Category, Article, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'Author', 'comment_num', 'category', 'created_time')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'id', 'parent_comment_id', 'created_time', 'content', 'poll_num')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.
