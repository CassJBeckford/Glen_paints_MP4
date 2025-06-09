from django.shortcuts import render
from .models import FAQ


def faqs_page(request):
    """ A view to return the FAQs page """
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'faqs/faqs_page.html', context)
