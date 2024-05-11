from django.shortcuts import render, redirect, get_object_or_404
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
            )
            return redirect('home_page')
        else:
            return render(request, 'create_book.html', {'form': form})


def change_book(request, pk):
    book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = BookForm(initial={
            'author_name': book.author_name,
            'author_gmail': book.author_gmail,
            'text': book.text,
        })
        return render(request, 'update_book.html', {'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.author_name = form.cleaned_data.get('author_name')
            book.author_gmail = form.cleaned_data.get('author_gmail')
            book.text = form.cleaned_data.get('text')
            book.save()
            return redirect('home_page')
        else:
            book.save()
            return render(request, 'update_book.html', {'form': form})


def delete_book(request, pk):
    book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_book.html', {'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('home_page')