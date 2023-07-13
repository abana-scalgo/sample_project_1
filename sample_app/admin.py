from django.contrib import admin
from .models import CMS
# Register your models here.

class AdminCMS(admin.ModelAdmin):
    list_display = ('heading', 'content', 'created_date')

admin.site.register(CMS,AdminCMS)
