from .models import Category, Post
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('categoryname',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('postTitle', 'postText', 'postTitle', 'postText',)