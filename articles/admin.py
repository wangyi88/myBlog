from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    # 表头
    list_display = ("title","author","img","abstract","created_at")


admin.site.register(Articles,ArticlesAdmin)