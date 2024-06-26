from django.urls import path
from webapp.views import home_page, create_book, change_book, delete_book


urlpatterns = [
    path('', home_page, name='home_page'),
    path('create_book/', create_book, name='create_book'),
    path('change_book/<int:pk>/', change_book, name='change_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
