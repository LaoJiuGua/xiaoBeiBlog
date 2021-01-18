from django.contrib import admin
from .models import *
from mdeditor.widgets import MDEditorWidget
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    list_display = ('title', 'author', 'category', 'created_time', 'modified_time')


    list_filter = list_display


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

    list_filter = list_display


@admin.register(Category)
class CateAdmin(admin.ModelAdmin):
    list_display = ('name',)

    list_filter = list_display


admin.site.site_header = '小北博客管理后台'
admin.site.site_title = '小北博客管理后台'
admin.site.index_title = '欢迎登录小北博客管理后台'