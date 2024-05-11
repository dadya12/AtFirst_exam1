from django.urls import path
from webapp.views import home_page, create_book


urlpatterns = [
    path('', home_page, name='home_page'),
    path('create_book/', create_book, name='create_book'),
]
