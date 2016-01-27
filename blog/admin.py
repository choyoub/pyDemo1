from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.site_header = '디장고 블로그'
admin.site.register(Post)