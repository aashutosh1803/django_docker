from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.conf import settings
import time
import redis

cache = redis.Redis(host='redis-database', port=6379,charset="utf-8",decode_responses=True)
cache.config_set('maxmemory-policy', 'allkeys-lru')

def get_all_books(request):
    books = Book.objects.all()
    bookList = []
    for book in books:
        bookList.append(
            {'id': book.id, 'name': book.name, 'description': book.description, 'created_at': book.created_at}
        )
    return JsonResponse({'books': bookList})


def create_sample_book(request):
    book = Book(name='sample name', description='sample description')
    book.save()
    cache.set(book.id, str(int(time.time())))
    return JsonResponse({'book': model_to_dict(book)})


def get_book(request, id):
    book = Book.objects.get(id=id)
    cache.set(book.id, str(int(time.time())))
    if book:
        return JsonResponse({'book': model_to_dict(book)})
    else:
        return JsonResponse({'book': {}})

def get_cache_values(request):
    value_dict = {}
    for key in cache.keys():
        value_dict[key] = cache.get(key)
    return JsonResponse({'cache': value_dict})