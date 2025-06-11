from django.shortcuts import render
from .models import faq


def faqs_page(request):
    """ A view to return the FAQs page """
    faqs = faq.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'faqs/faqs_page.html', context)
