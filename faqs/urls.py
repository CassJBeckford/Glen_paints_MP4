from django.urls import path
from . import views

urlpatterns = [
    path('', views.faqs_page, name='faqs_page'),
]
