from django.contrib import admin
from .models import Author, Category, Post, PostCategory
from modeltranslation.admin import TranslationAdmin # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'authorRating')
    list_filter = ('authorUser', 'authorRating')
    search_fields = ('authorUser', 'authorUser')


class CategoryAdmin(TranslationAdmin):
    model = Category


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('categoryType', 'postTitle', 'pubData')
#     list_filter = ('categoryType', 'postTitle', 'pubData')
#     search_fields = ('postTitle', 'postTitle' )


admin.site.register(Author, AuthorAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Post, PostAdmin)


class PostAdmin(TranslationAdmin):
    model = Post


admin.site.register(Post)
admin.site.register(Category)