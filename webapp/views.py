from django.shortcuts import render, redirect
from webapp.models import GuestBook


def home_page(request):
    book = GuestBook.objects.all().filter(status='active').order_by('-created_at')
    context = {'book': book}
    return render(request, 'home_page.html', context)
