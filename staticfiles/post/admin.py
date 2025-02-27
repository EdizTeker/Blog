from django.contrib import admin

from .models import Post
from django.utils.text import slugify
#from post.models import Post

class PostAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'publishing_date', 'slug']
    list_display_links = ['title', 'publishing_date']
    list_filter = ['publishing_date', 'title']
    search_fields = ['title', 'content']

    class Meta:
        model = Post    

admin.site.register(Post, PostAdmin)
