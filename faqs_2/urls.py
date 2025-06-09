from django.urls import path
from .views import faqs_page_2

urlpatterns = [
    path('', faqs_page_2, name='faqs_page_2'),
]