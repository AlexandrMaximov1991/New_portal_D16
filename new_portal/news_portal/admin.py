from django.contrib import admin
from .models import Author, Category, Post, PostCategory


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'authorRating')
    list_filter = ('authorUser', 'authorRating')
    search_fields = ('authorUser', 'authorUser')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryname',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('categoryType', 'postTitle', 'pubData')
    list_filter = ('categoryType', 'postTitle', 'pubData')
    search_fields = ('postTitle', 'postTitle' )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
