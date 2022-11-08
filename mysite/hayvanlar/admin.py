from django.contrib import admin
from .models import Hayvan


class HayvanAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_date','isAvailable')
    list_filter = ('created_date',)
    list_editable = ('isAvailable',)
    search_fields = ('id','name')
    list_per_page = 5

admin.site.register(Hayvan,HayvanAdmin)
