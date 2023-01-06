from django.contrib import admin

# Register your models here.
from .models import News

class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ["slug", "post_date",]


admin.site.register(News, NewsAdmin)
