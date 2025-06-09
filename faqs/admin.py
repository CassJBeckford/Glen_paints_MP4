from django.contrib import admin
from .models import faq


@admin.register(faq)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')
    search_fields = ('question', 'category', 'answer')
