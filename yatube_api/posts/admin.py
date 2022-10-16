from django.contrib import admin

from .models import Comment, Follow, Group, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'post',
        'author',
        'text',
    )
    search_fields = ('text', 'author', 'post')
    list_filter = ('post',)


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
    )
    search_fields = ('user',)


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
    )
    list_editable = ('slug',)
    search_fields = ('title',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
