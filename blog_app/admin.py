from django.contrib import admin
from blog_app.models import *
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', 'status')

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    readonly_fields = ('preview_image',)
    list_display = ('preview_image', 'title', 'sub_title')


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('copyright', 'facebook')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'article_author', 'posted_on')
    search_fields = ('title', 'article_author', 'posted_on')
    list_filter = ('article_author',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name',)