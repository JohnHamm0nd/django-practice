from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('id','author_id')  # id, author_id 필드 추가
    
admin.site.register(Post, PostAdmin)
