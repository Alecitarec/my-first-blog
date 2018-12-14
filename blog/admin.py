from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    search_fields = ("author","title",)
    list_display = ("author","title","text","published_date",)
