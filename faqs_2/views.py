from django.shortcuts import render
# from .models import FAQ


def faqs_page_2(request):
    """ A view to return the FAQs page """
    # faqs = FAQ.objects.all()
    return render(request, 'faqs/faqs_page_2.html')
