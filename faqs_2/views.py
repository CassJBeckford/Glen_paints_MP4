from django.shortcuts import render
# from .models import FAQ_2


def faqs_page_2(request):
    """ A view to return the FAQs page """
     # faqs = FAQ_2.objects.all()
    return render(request, 'faqs/faqs_page_2.html')
