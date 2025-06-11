from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import NewsLetterForm


def news_letter(request):
    """ A view to render news letter page and submit the form """
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been added to our News letter!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to submit form')
    else:
        form = NewsLetterForm()

    template = 'news_letter.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
