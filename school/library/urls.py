from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_books, name='get_all_books'),
    path('get_book/<id>', views.get_book, name='get_book'),
    path('get_cache_values', views.get_cache_values, name='get_cache_values'),
    path("create_book", views.create_sample_book, name='create_sample_book'),
]
