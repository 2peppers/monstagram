from django.contrib import admin

from Main.models import Post, Like


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'url', 'image_path', 'added_at', 'modified_at')
    list_display_links = ('url', 'id', 'image_path')
    list_editable = ('title', 'author')
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Like)
