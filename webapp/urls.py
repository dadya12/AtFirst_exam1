from django.urls import path
from webapp.views import home_page


urlpatterns = [
    path('', home_page, name='home_page'),
]
