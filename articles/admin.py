from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    # 表头
    list_display = ("title","author","img","abstract","created_at")
    # 搜索
    search_fields = ("title","author","abstract","content")
    list_filter = list_display

admin.site.register(Articles)