
from django.contrib import admin
from .models import Post
from django.utils import timezone 

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'published_date')
    list_filter = ['published_date']
    search_fields = ['title']
admin.site.register(Post, PostsAdmin)