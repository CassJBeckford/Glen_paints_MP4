from django.contrib import admin
from .models import FAQ_2


@admin.register(FAQ_2)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')
    search_fields = ('question', 'category', 'answer')
