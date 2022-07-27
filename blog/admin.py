from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Message

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'published', 'created')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published', 'status')
    summernote_fields = ('content')
    actions = ['publish_post']

    def publish_post(self, request, queryset):
        queryset.update(published=True)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'body', 'received', 'accepted')
    search_fields = ('post', 'author', 'body')
    actions = ['accept_comments']

    def accept_comments(self, request, queryset):
        queryset.update(approved=True)