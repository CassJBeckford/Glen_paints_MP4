from django.shortcuts import render
from .models import faq


def faqs_page_2(request):
    """ A view to return the FAQs page """
    faqs = faq.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'faqs/faqs_page_2.html', context)
