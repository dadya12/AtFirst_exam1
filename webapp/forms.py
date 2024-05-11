from django import forms
from webapp.models import GuestBook


class BookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ['author_name', 'author_gmail', 'text']
