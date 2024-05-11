from django.shortcuts import render, redirect
from webapp.models import GuestBook
from webapp.forms import BookForm


def home_page(request):
    book = GuestBook.objects.all().filter(status='active').order_by('-created_at')
    context = {'book': book}
    return render(request, 'home_page.html', context)


def create_book(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})
    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            GuestBook.objects.create(
                author_name=form.cleaned_data.get('author_name'),
                author_gmail=form.cleaned_data.get('author_gmail'),
                text=form.cleaned_data.get('text'),
                status=form.cleaned_data.get('status')
            )
            return redirect('home_page')
        else:
            return render(request, 'create_book.html', {'form': form})
