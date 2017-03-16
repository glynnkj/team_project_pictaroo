from django.contrib import admin
from pictaroo.models import Category, Image, Comment
from pictaroo.models import UserProfile


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image')



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'image', 'author')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(UserProfile)

