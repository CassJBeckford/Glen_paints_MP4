from django.shortcuts import render
from .models import FAQ


def faqs_page(request):
    """ A view to return the FAQs page """
    faqs = FAQ.objects.all()
    return render(request, 'faqs/faqs_page.html', {'faqs': faqs})
