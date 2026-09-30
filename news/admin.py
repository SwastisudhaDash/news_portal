from django.contrib import admin
from .models import Article, Category, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "is_featured", "is_breaking", "is_published", "views", "created_at")
    list_filter = ("category", "is_featured", "is_breaking", "is_published")
    search_fields = ("title", "summary", "content", "author")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_featured", "is_breaking", "is_published")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "article", "created_at")
    search_fields = ("name", "email", "message")
