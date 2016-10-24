from django.contrib import admin

from Main.models import Post, Like


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'url', 'image', 'added_at')
    list_display_links = ('url', 'id')
    list_editable = ('title', 'author')

admin.site.register(Post, PostAdmin)
admin.site.register(Like)
